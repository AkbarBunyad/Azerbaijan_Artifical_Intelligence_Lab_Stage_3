# It computes the Levenshtein distance by directly implemention its recursive definition by calculation distance between parts of strings (s1[0:i], s2[0:j]) and then using the results to calculate the distance between the full strings. This is a rather naive approach and is not efficient for large strings.

def levenshtein_recursive(s1, s2):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    deletion = levenshtein_recursive(s1[:-1], s2) + 1
    insertion = levenshtein_recursive(s1, s2[:-1]) + 1
    substitution = levenshtein_recursive(s1[:-1], s2[:-1]) + (s1[-1] != s2[-1])
    return min(deletion, insertion, substitution)


print(levenshtein_recursive("kitten", "sitting"))