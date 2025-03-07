# It uses a divide-and-conquer approach to compute the LD by splitting one string in half, then using a single row to find the best matching split in the other string by computing distances forward and backward, and recusrively solves the smaller pieces. Think of it as cleverly guessing the middle of the edit path and working outward with minimal memory.

def hirschberg(s1, s2):
    def compute_row(s1, s2):
        n, m = len(s1), len(s2)
        row = [0] * (m + 1)
        for j in range(m + 1):
            row[j] = j
        for i in range(1, n + 1):
            prev = row[0]
            row[0] = i
            for j in range(1, m + 1):
                temp = row[j]
                cost = 0 if s1[i-1] == s2[j-1] else 1
                row[j] = min(row[j-1] + 1, prev + 1, prev + cost)
                prev = temp
        return row

    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if len(s1) == 1:
        return len(s2) if s1[0] not in s2 else len(s2) - 1
    mid = len(s1) // 2
    left = compute_row(s1[:mid], s2)
    right = compute_row(s1[mid:][::-1], s2[::-1])[::-1]
    split = min(range(len(s2) + 1), key=lambda j: left[j] + right[j])
    return hirschberg(s1[:mid], s2[:split]) + hirschberg(s1[mid:], s2[split:])

print(hirschberg("kitten", "sitting"))