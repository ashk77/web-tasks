# Challenge 4 : Task 2


# Firstly we input T
t = int(input())
operators = ['+', '-', '*', '/', '^']
priority_map = dict()
priority_map["+"] = 1
priority_map["-"] = 1
priority_map["*"] = 2
priority_map["/"] = 2
priority_map["^"] = 3

i = 0
while i < t:  # iteration for no of test cases
    i = i+1
    line = input()
    stack = list()
    for j in range(len(line)):
        if line[j] == '(':
            stack.insert(len(stack), line[j])

        elif line[j] == ')':
            while stack != []:
                k = stack.pop()
                if k != "(":
                    print(k, end='')
                else:
                    break
        elif line[j] not in operators:
            print(line[j], end='')
        else:
            while stack != []:
                k = stack.pop()
                if k in operators:
                    if priority_map[k] >= priority_map[line[j]]:
                        print(k, end='')
                    else:
                        stack.insert(len(stack), k)
                        break
                else:
                    stack.insert(len(stack), k)
                    break
            stack.insert(len(stack), line[j])
    while stack != []:
        print(stack.pop(), end='')
    print()




