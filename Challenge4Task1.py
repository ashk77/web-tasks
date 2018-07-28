# Challenge 4 : Task 1
# Left rotating an array
# warning :: if input is copied and pasted please note that the last character should not be end of file character
#             else the program gets stuck.

# Firstly we input T
t = int(input())
i = 0
while i < t:  # iteration for no of test cases
    i = i + 1
    # getting n and k
    n, k = list(map(int, input().split()))
    k = k % n    # if shift value is more than size of array we avoid full shifts multiple times by taking mod
    # getting the corresponding array
    arr = list(map(int, input().split()))
    rarr = list()
    # creating a new list and inserting elements at appropriate places after resultant shift
    for index in range(n):
        rarr.insert((index - k) % n, arr[index])
    print(*rarr)



