'''
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 1, 3, 5, 3, 2], the output should be solution(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be solution(a) = 2;

For a = [2, 4, 3, 5, 1], the output should be solution(a) = -1.
'''

def solution(a):
    seen = set()
    for n in a:
        if n in seen:
            return n
        if n not in seen:
            seen.add(n)
    
    return -1

'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
solution(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
solution(s) = '_'.

There are no characters in this string that do not repeat.
'''

def solution(s):
    seen = set()
    result = []
    for l in s:
        if l in seen and l in result:
            result.remove(l)
        if l not in seen:
            result.append(l)
            seen.add(l)
        
    if(result != []):
        return result[0]
    else:
        return '_'
            
