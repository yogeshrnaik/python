# Write any import statements here
'''
A positive integer is considered uniform if all of its digits are equal. For example, 222222 is uniform, while 223223 is not.
Given two positive integers AA and BB, determine the number of uniform integers between AA and BB, inclusive.
Please take care to write a solution which runs within the time limit.
Constraints
1 \le A \le B \le 10^{12}1≤A≤B≤10
12

Sample test case #1
A = 75
B = 300
Expected Return Value = 5
Sample test case #2
A = 1
B = 9
Expected Return Value = 9
Sample test case #3
A = 999999999999
B = 999999999999
Expected Return Value = 1
Sample Explanation
In the first case, the uniform integers between 7575 and 300300 are 7777, 8888, 9999, 111111, and 222222.
In the second case, all 99 single-digit integers between 11 and 99 (inclusive) are uniform.
In the third case, the single integer under consideration (999{,}999{,}999{,}999999,999,999,999) is uniform.
'''


def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    # Write your code here
    count = 1 if isUniform(A) else 0
    while A < B:
        A = getNextUniform(A)
        count = (count + 1) if A <= B else count

    return count


def isUniform(n: int) -> bool:
    start = str(n)[0]
    for c in str(n)[1:]:
        if c != start:
            return False

    return True


def getNextUniform(n: int) -> int:
    numStr = str(n)
    length = len(numStr)
    first = int(numStr[0])
    newUniformStartsFromFirst = False
    if not isUniform(n):
        for c in numStr[1:]:
            if int(c) < first:
                newUniformStartsFromFirst = True
                break
            elif int(c) > first:
                break

        if newUniformStartsFromFirst:
            return createUniform(first, length)

    if first <= 8:
        return createUniform(first + 1, length)
    else:
        return createUniform(1, length + 1)


def createUniform(first: int, length: int) -> int:
    result = ""
    for i in range(0, length):
        result += str(first)
    return int(result)
