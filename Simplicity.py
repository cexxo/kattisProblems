"""
Simplicity (https://open.kattis.com/problems/simplicity)
For a string of letters, define the Simplicity of the string 
to be the number of distinct letters in the string. For 
example, the string string has simplicity 6, and the string 
letter has simplicity 4.
You like strings which have simplicity either 1 or 2. Your 
friend has given you a string and you want to turn it into a 
string that you like. You have a magic eraser which will 
delete one letter from any string. Compute the minimum number 
of letters you must erase in order to turn the string into a 
string with simplicity at most 2.
INPUT:
Each input will consist of a single test case. Note that your 
program may be run multiple times on different inputs. The 
input will consist of a line with a single string consisting 
of at least 1 and at most 100 lowercase letters ‘a’-‘z’.
OUTPUT:
Output a single integer, indicating the minimum number letters
you need to erase in order to give the string a simplicity of
1 or 2.
"""
s = input()
letter = [0]*26
letters = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}
for i in s:
    letter[letters[i]] += 1
simplicity = 0
for i in letter:
    if i != 0:
        simplicity += 1
removals = 0
if simplicity <= 2:
    print(0)
else:
    for i in letter:
        if i == 1 and simplicity > 2:
            removals += i
            simplicity -= 1
            if simplicity <= 2:
                break
        elif i > 1:
            removals += i-1
    print(removals)
