# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Input: s = "anagram", t = "nagaram"
# Output: true
# Input: s = "rat", t = "car"
# Output: false
# Input: s = "aaab", t = "aabb"
# Output: false
# Input: s = "rat", t = "rrat"
# Output: false
# Don't use sorting. Ideal answer time complexity is O(n)

def check_anagram(s, t):
    len_s, len_t = len(s), len(t) #1
    if len_s != len_t: #1
        return False #1
    hash_s = {}
    hash_t= {}
    i = 0
    while i < len_s:
        letter_s, letter_t = s[i], t[i]
        if letter_s not in hash_s:
            hash_s[letter_s] = 1
        else:
            hash_s[letter_s] = hash_s[letter_s] + 1

        if letter_t not in hash_t:
            hash_t[letter_t] = 1
        else:
            hash_t[letter_t] = hash_t[letter_t] + 1        
        i +=1
    
    if hash_s == hash_t:
        return True
    return False


if __name__ == '__main__':
    s = input()
    t = input()
    print(check_anagram(s, t))