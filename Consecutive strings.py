# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
    
    words = []
    
    if k > 0 and len(strarr) >= k:
        n = k if k == 1 else (k - 1)

        for i in range(len(strarr[:n])):
            if len(strarr[i]) > 0:
                words.append("".join(strarr[i:i+k]))
    
        return max(words, key=lambda s: len(s))
    
    else:
        return ""


strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
