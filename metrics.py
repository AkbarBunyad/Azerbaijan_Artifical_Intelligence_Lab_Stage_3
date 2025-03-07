def levenshtein_distance(s1, s2):
    """
    Calculate the Levenshtein distance between two strings.
    
    Implementation using DP approach.
    
    Parameters:
    s1, s2 : str
        Strings to compare.
    
    Returns:
    int
        LD between two strings.
    """
    # creating a matrix of size len(s1) + 1 x len(s2) + 1
    rows, cols = len(s1) + 1, len(s2) + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    # initializing first row and column
    for i in range(rows):
        dp[i][0] = i
    
    for j in range(cols):
        dp[0][j] = j
    
    # filling the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # taking the minimum of:
                # 1. deleting a character from s1
                # 2. inserting a character into s1
                # 3. substituting a character in s1
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    # returning the last element of the matrix
    return dp[rows-1][cols-1]

def damerau_levenshtein_distance(s1, s2):
    """
    Calculate the Damerau-Levenshtein distance between two strings.
    This accounts for insertions, deletions, substitutions, and transpositions.
    
    Parameters:
    s1, s2 : str
        Strings to compare.
    
    Returns:
    int
        DL distance between two strings.
    """
    rows, cols = len(s1) + 1, len(s2) + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # initializing first row and column
    for i in range(rows):
        dp[i][0] = i
    for j in range(cols):
        dp[0][j] = j
    
    # filling the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            dp[i][j] = min(
                dp[i-1][j] + 1,      # deletion
                dp[i][j-1] + 1,      # insertion
                dp[i-1][j-1] + cost  # substitution
            )
            
            # checking for transposition
            if i > 1 and j > 1 and s1[i-1] == s2[j-2] and s1[i-2] == s2[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-2][j-2] + cost)
    
    return dp[rows-1][cols-1]

def jaro_similarity(s1, s2):
    # handling edge cases for identical or empty strings
    if s1 == s2:   #if completely the same, complete similarity, else 0, logically.
        return 1.0
    if not s1 or not s2:
        return 0.0

    len1 = len(s1)
    len2 = len(s2)
    # calculating the matching window based on longer string
    w = max(len1, len2) // 2 - 1

    # finding matching characters within the window
    s1_matched = []
    s2_matched = []
    s2_used = set()
    for i in range(len1):
        start = max(0, i - w)
        end = min(len2, i + w + 1)
        for j in range(start, end):
            if s1[i] == s2[j] and j not in s2_used:
                s1_matched.append(i)
                s2_matched.append(j)
                s2_used.add(j)
                break

    m = len(s1_matched)
    # returning 0 if no matches are found
    if m == 0:
        return 0.0

    # counting transpositions by comparing matched positions
    sorted_s2_matched = sorted(s2_matched)
    mismatches = sum(1 for orig, sort in zip(s2_matched, sorted_s2_matched) if orig != sort)
    t = mismatches // 2

    # calculating similarity using the jaro formula in the LaTex document
    similarity = (m / len1 + m / len2 + (m - t) / m) / 3
    return similarity

def jaro_winkler_similarity(s1, s2, p=0.1):
    """
    Calculate the Jaro-Winkler similarity between two strings.
    
    Parameters:
    s1, s2 : str
        Strings to compare.
    p : float
        Scaling factor for how much the score is adjusted for common prefixes.
        Default is 0.1.
    
    Returns:
    float
        Jaro-Winkler similarity score (0-1)
    """
    # calculating basic Jaro similarity
    jaro_sim = jaro_similarity(s1, s2)
    
    # finding length of common prefix (up to 4 characters)
    prefix_len = 0
    max_len = min(len(s1), len(s2), 4)
    
    for i in range(max_len):
        if s1[i] == s2[i]:
            prefix_len += 1
        else:
            break
    
    # calculating Jaro-Winkler similarity
    jw_sim = jaro_sim + (prefix_len * p * (1 - jaro_sim))
    
    return jw_sim

# converting similarity scores to distances (1 - similarity)
def jaro_distance(s1, s2):
    return 1 - jaro_similarity(s1, s2)

def jaro_winkler_distance(s1, s2):
    return 1 - jaro_winkler_similarity(s1, s2)