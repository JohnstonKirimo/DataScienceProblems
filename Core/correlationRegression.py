"""
Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute Karl Pearson’s coefficient of correlation between these scores.
Compute the answer correct to three decimal places.

Output Format

In the text box, using the language of your choice, print the floating point/decimal value required.
Do not leave any leading or trailing spaces.

"""
#Solution

import math

def P(A,B):
    n = float(len(A))
    muA = sum(A)/n
    muB = sum(B)/n
    diffA = map(lambda x: x - muA, A)
    diffB = map(lambda x: x - muB, B)
    stdA = math.sqrt((1/(n-1))* sum([d*d for d in diffA]))
    stdB = math.sqrt((1/(n-1))* sum([d*d for d in diffB]))
    return (sum([A[i]*B[i] for i in range(int(n))]) - n * muA * muB) / ((n-1) * stdA * stdB)

A = [15,12,8,8,7,7,7,6,5,3]
B = [10,25,17,11,13,17,20,13,9,15]
print(P(A,B))
