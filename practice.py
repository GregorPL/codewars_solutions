def solution(s):
    new_text = ""
    for i, l in enumerate(s):
        if l.isupper():
            new_text += " "
            new_text += l
        else:
            new_text += l
    return new_text


print(solution("abcDaa"))
print(solution("identifier"))
print(solution("breakCamelCase"))