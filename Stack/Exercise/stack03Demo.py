from stack03 import *

def reverse_check(string:str):
    linkedStack = LinkedStack()
    index = 0
    reverseStr = ""
    forwardStr = ""

    while string[index] != "$":
        linkedStack.push(string[index])
        index += 1

    for i in range(index+1, len(string)):
        reverseStr += string[i]             # abc

    for i in range(index):
        forwardStr += linkedStack.pop()     # abc

    print(reverseStr)
    print(forwardStr)

    if forwardStr == reverseStr:
        return True
    else:
        return False

    

print(reverse_check("abc$cba"))
print(reverse_check("abc$cb"))