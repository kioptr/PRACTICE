import sys
import string

l = int(input())
h = int(input())
text = input()
row = [input() for i in range(h)]
print("text :", text, "\nrow :", row, "\nheight :", h, "\nwidth :", l, file=sys.stderr)
text = text.upper()
alphabet = string.ascii_uppercase
answer = ""
for i in range(h):
    for car in text:
        if car.isalpha():
            # print("alphabet.index(car) & car : ", alphabet.index(car), car)
            start = l*(alphabet.index(car))
            answer += row[i][start:start+l]
        else:
            answer += row[i][l*26:]
    answer += "\n"
print(answer)