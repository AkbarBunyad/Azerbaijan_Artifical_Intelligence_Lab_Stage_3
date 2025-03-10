﻿# String Similarity Explorer

A Python application for exploring string similarity metrics and finding word matches from a dictionary. Built with Gradio for an interactive web interface, all string similarity algorithms are implemented from scratch without external metric computation libraries.

## Features

- Calculate edit distances between two words using multiple metrics:
  - Levenshtein Distance
  - Damerau-Levenshtein Distance
  - Jaro Similarity
  - Jaro-Winkler Similarity
- Find 10 closest dictionary matches for any input word

## Getting Started

### Setting up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\activate

# Activate virtual environment (Linux/Mac)
source venv/bin/activate
```

### Prerequisites

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```
The web interface will be available at `http://127.0.0.1:7860`

## Project Structure

### Core Files
- `main.py` - Entry point and Gradio interface setup
- `metrics.py` - Core implementation of similarity algorithms
- `unique_words.txt` - Preprocessed dictionary file

### Additional Components
- `optimization_computation_methods/` -  Showing LD optimizations
- `requirements.txt` - Project dependencies
- `unique_words.py` - Flexible script to preprocess any dictionary file provided that it is from Kaggle

## Dataset

The dictionary is sourced from [Kaggle's English Dictionary Dataset](https://www.kaggle.com/datasets/anthonytherrien/dictionary-of-english-words-and-definitions). The raw data was preprocessed to extract unique words, creating `unique_words.txt`.

## Demo

Here's the app suggesting matches for "Akbarium" (as a chemical engineer, if I had invented a new element, I would have definitely named it like that. Not a bad one, indeed 😄)

![Application Interface](snap.png)

## License

MIT

## Contributing

Feel free to open issues and submit pull requests!
