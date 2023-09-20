# Phrase Improvement Engine

The **Phrase Improvement Engine** is a Python script designed to analyze an input text and provide suggestions for improving phrases or sentences by replacing them with standardized phrases from a CSV file. This tool uses spaCy for natural language processing and semantic similarity comparison to make recommendations.

## Table of Contents

1. [Requirements](#requirements)
2. [Usage](#usage)
3. [CSV File Format](#csv-file-format)
4. [How It Works](#how-it-works)
5. [Example](#example)

## Requirements

To run the Phrase Improvement Engine, you need the following:

- Python 3.x
- [spaCy](https://spacy.io/) library with the English model (`en_core_web_md`)
- A CSV file containing standardized phrases (e.g., 'Standardised terms.csv')

You can install spaCy and download the English model using the following command:
```bash
pip install spacy
python -m spacy download en_core_web_md
```

## Usage
To use the Phrase Improvement Engine, follow these steps:

1. Clone or download the repository to your local machine.

2. Place your input text in a plain text file (e.g., input.txt) that you want to improve.

3. Make sure you have a CSV file (e.g., 'Standardised terms.csv') with the standardized phrases you want to compare against.

4. Open a terminal and navigate to the directory containing the script and input file.

5. Run the script with the following command:
   ```cmd

    python main.py --input sample_text.txt
   ```

7. The script will process the input text, split it into phrases, and generate suggestions for improving each phrase.

8. The suggestions, along with their similarity scores, will be displayed in the terminal.


## CSV File Format
The CSV file containing standardized phrases should have one phrase per row. The script reads this file to compare the input phrases with the standardized ones.

Example CSV format:

Standardized Phrase 1  
Standardized Phrase 2  
Standardized Phrase 3
...

## How It Works
The Phrase Improvement Engine works as follows:

It reads the input text and splits it into individual phrases using punctuation marks.

It calculates the semantic similarity between each phrase in the input text and the standardized phrases from the CSV file using spaCy's word vectors.

If the similarity score for a phrase is above a specified threshold (0.95 by default), it suggests the most similar standardized phrase as a replacement.


## Example
Suppose you have an input text file input.txt with the following content:

This is a simple example. I need some suggestions. Improve this text!
And you have a CSV file ('Standardised terms.csv') with standardized phrases like:

simple example  
need suggestions  
improve text


When you run the script with python main.py --input simple_text.txt, it will output suggestions like:

Suggestions:
Original: This is a simple example, Suggestion: simple example, Similarity Score: 0.9734365129470825  
Original: I need some suggestions, Suggestion: need suggestions, Similarity Score: 0.9732131121385361  
Original: Improve this text!, Suggestion: improve text, Similarity Score: 0.9999999377406093

The script identifies phrases in the input text and suggests replacing them with the most similar standardized phrases from your CSV file.

Enjoy using the Phrase Improvement Engine!

Feel free to customize and expand this README to include more specific deta
