#!/usr/bin/env python3
message = 'Your grade is: '
print('What was the numeric grade you received?')
connection = float(input())
if connection >= 90:
    message = message + 'A'
elif connection >= 80 and connection <= 89:
    message = message + 'B'
elif connection >= 70 and connection <= 79:
    message = message + 'C'
elif connection >= 60 and connection <= 69:
    message = message + 'D'
else:
    message = message + 'F'
print(message)
