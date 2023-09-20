import argparse
import spacy
import re
import csv
standardized_phrases = []

# Specify the path to your CSV file
csv_file_path = 'Standardised terms.csv'

# Open and read the CSV file
with open(csv_file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    # Iterate through each row in the CSV and append the phrase to the list
    for row in csv_reader:
        # Assuming each row contains only one phrase    
        standardized_phrases.append(row[0])

# Function to calculate semantic similarity between a phrase and standardized phrases
def calculate_similarity(phrase, nlp):
    similarities = [phrase.similarity(nlp(std_phrase)) for std_phrase in standardized_phrases]
    max_similarity = max(similarities)
    if max_similarity < 0.95:  # Set a threshold for similarity
        most_similar_index = similarities.index(max_similarity)
        return standardized_phrases[most_similar_index], max_similarity
    return None, 0.0

# Function to split the input text into phrases
def split_text_into_phrases(input_text):
    # Use regular expressions to split the text into phrases based on punctuation marks
    phrases = re.split(r'[.!,?;]', input_text)
    # Remove empty phrases and strip whitespace
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]
    return phrases

# Function to process the input text and generate suggestions for phrases
def process_input_text(input_text, nlp):
    phrases = split_text_into_phrases(input_text)
    suggestions = []
    for phrase_text in phrases:
        phrase = nlp(phrase_text)
        most_similar, similarity_score = calculate_similarity(phrase, nlp)
        if most_similar:
            suggestions.append((phrase_text, most_similar, similarity_score))
    return suggestions

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phrase Improvement Engine")
    parser.add_argument("--input", type=str, required=True, help="Path to the input text file")
    args = parser.parse_args()

    # Load spaCy model (you need to download the model if not already installed)
    nlp = spacy.load("en_core_web_md")

    # Read the input text from the file
    with open(args.input, "r") as file:
        input_text = file.read()

    # Process the input text, split it into phrases, and generate suggestions
    suggestions = process_input_text(input_text, nlp)

    # Print suggestions
    print("Suggestions:")
    for original, suggestion, similarity in suggestions:
        print(f"Original: {original}, Suggestion: {suggestion}, Similarity Score: {similarity}")