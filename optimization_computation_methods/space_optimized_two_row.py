# Optimizes space by using only two rows of the matrix to store the values: one for the previous row and ove for the current row. It computes the distance iteratively by updating the values in the two rows. For the record, this approach is more memory efficient than the DP approach, which uses a matrix of size len(s1) + 1 x len(s2) + 1 to store the values.

def levenshtein_two_row(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1 # s1 should be the longer string
    n, m = len(s1), len(s2)
    prev_row = list(range(m + 1)) #initializing first row
    for i in range(1, n + 1):
        curr_row = [i] + [0] * m
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            curr_row[j] = min(curr_row[j - 1] + 1, prev_row[j] + 1, prev_row[j - 1] + cost)
        prev_row = curr_row
    return prev_row[m]

print(levenshtein_two_row("kitten", "sitting"))