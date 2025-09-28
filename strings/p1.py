# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
s = "aaabb"
def areOccurrencesEqual(s):
        freq={char :s.count(char)for char in s}
        return len(set(freq.values()))==1


print(areOccurrencesEqual(s))        