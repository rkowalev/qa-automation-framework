def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if score in range(90, 100):
        return "A"
    if score in range(80, 89):
        return "B"
    if score in range(70, 79):
        return "C"
    if score in range(60, 69):
        return "D"
    if score in range(0, 59):
        return "F"
    
print(get_grade(76, 34, 98))

def longest(a1, a2):
    a3 = a1 + a2
    result = ""
    for i in a3:
        if i not in result:
            result += i
    return "".join(sorted(result))