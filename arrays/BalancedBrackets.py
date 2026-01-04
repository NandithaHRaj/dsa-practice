'''
    Balanced Brackets:
    Write a function that takes in a string containing brackets: ({[]})
    as well as other alphabet characters and returns True if the brackets
    are balanced, and False if not. 
    
    For example:

    Balanced: (()(){x}[a]{{{()}()}})
    Unbalanced: (([)){

    Time:  O(N), The input array is iterated once.
    Space: O(N), The stack holding the characters

	Last Practiced: 2026-01-04 13:15:08
'''
balancedString='(()(){x}[a]{{{()}()}})'
unbalancedString='(([)){'
def balancedBrackets(string):
    leftBrackets = '({['
    rightBrackets = ')}]'
    bracketMap = {')':'(','}':'{',']':'['}
    stack= []

    for char in string:
        if char in rightBrackets:
            if isStackEmpty(stack):
                return False
            if bracketMap[char] == stack[-1]:
                stack.pop()
            else:
                return False
        if char in leftBrackets:
            stack.append(char)
    return isStackEmpty(stack)

def isStackEmpty(stack):
    return len(stack) == 0

print('First String:',balancedBrackets(balancedString))
print('Second String:',balancedBrackets(unbalancedString))