import csv

def extract_unique_words(csv_file="dict.csv", output_file="unique_words.txt"):
    """
    Extracts unique words from the first column of a CSV file.
    
    Parameters:
    csv_file: str
        Path to the CSV file.
    output_file: str
        Path to the output text file.
        
    Returns:
    list
        Sorted list of unique words.
    """
    unique_words = set()
    with open(csv_file, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                # capitalizing first letter of each word, then adding to set to remove duplicates
                unique_words.add(row[0].capitalize())
    
    with open(output_file, "w", encoding="utf-8-sig") as file:
        for word in sorted(list(unique_words)):
            file.write(f"{word}\n")

    print(f"Extracted {len(unique_words)} unique words from {csv_file} to {output_file}.")

    return sorted(list(unique_words))

extract_unique_words()