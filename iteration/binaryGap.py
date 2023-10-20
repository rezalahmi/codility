"""A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary
representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary
representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no
binary gaps. The number 32 has binary representation 100000 and has no binary gaps. """


def solution(N):
    count = 0
    result = 0
    flag = False
    binary_representation = bin(N)
    for i in range(2, len(binary_representation)):
        if binary_representation[i] == '0':
            count += 1
            flag = True
        elif flag and binary_representation[i] == '1':
            if count > result:
                result = count
            count = 0
    return result
