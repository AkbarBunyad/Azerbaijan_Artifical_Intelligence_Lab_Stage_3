from metrics import (
    levenshtein_distance, 
    damerau_levenshtein_distance, 
    jaro_distance, 
    jaro_winkler_distance
)

def load_dictionary(file_path="unique_words.txt"): 
    with open(file_path, "r", encoding="utf-8-sig") as file:
        return file.read().splitlines()
    
def calculate_distance(word1, word2, metric):
    """
    Calculate distance between two words using the specified metric.
    
    Parameters:
    word1, word2: str
        Words to compare.
    metric: str
        The distance metric to use.
        
    Returns:
    float
        Distance between the two words.
    """
    if not word1 or not word2:
        return None
        
    if metric == "levenshtein":
        return levenshtein_distance(word1.lower(), word2.lower())
    elif metric == "damerau-levenshtein":
        return damerau_levenshtein_distance(word1.lower(), word2.lower())
    elif metric == "jaro":
        return jaro_distance(word1.lower(), word2.lower())
    elif metric == "jaro-winkler":
        return jaro_winkler_distance(word1.lower(), word2.lower())
    else:
        return levenshtein_distance(word1.lower(), word2.lower())

def find_close_matches(word, dictionary, metric="levenshtein", max_results=10):
    """
    Find close matches for a given word in a dictionary using selected metric.
    
    Parameters:
    word: str
        Word to find close matches for.
    dictionary: list
        List of unique words.
    metric: str
        The distance metric to use.
    max_results: int
        Maximum number of results to return.
    
    Returns:
    list
        List of close matches with distances.
    """
    matches = []
    for dict_word in dictionary:
        distance = calculate_distance(word.lower(), dict_word.lower(), metric)
        matches.append((dict_word, distance))

    return sorted(matches, key=lambda x: x[1])[:max_results]
