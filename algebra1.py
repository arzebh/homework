import time
def q1(a, b, c):
    return a + b - c + b

print(q1(4, 3, 5))
#guess-5

def q2(a, b, c):
    return (a + b) / c * c
#guess-5
print(q2(4, 1, 2))

def q3(a, b, c):
    return a * c / c
#guess- 3
print(q3(3, 1, 2))

def q4(a, b, c):
    return (a - b) / c * c * c
#guess- 4
print(q4(3, 1, 2))

def q5(a, b, c):
    return (a - b + b) / c * c * b
#guess- ?
print(q5(3, 7, 6))

def q6(a, b, c):
    return 2 * a + 4 * b / 6 * c
#guess-28
print(q6(3, 7, 6))

def q7(a, b, c):
    return 4 * a - b / 3 * c
#guess- -2
print(q7(3, 7, 6))

def q8(a, b, c):
    return 4 + a / 4 * 4
#guess-?
print(q8(3, 7, 6))

def q9(a, b, c):
    return 9 + b / c * c
#guess-?
print(q9(3, 7, 6))
