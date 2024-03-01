# Python uses Lexicographic ordering when comparing strings.

string1 = input().lower()
string2 = input().lower()

# This compares the values of each letter in the lexicographic not the actual length or other charateristic of the string

if string1 > string2:
    print(1)
elif string1 < string2:
    print(-1)
else:
    print(0)
