def findSpecialSubsequencesAG(array, length):

    A = 0
    AG = 0

    for i in range(length):
        if array[i] == 'A':
            A += 1
        elif array[i] == 'G':
            AG += A

    return AG


if __name__ == "__main__":
    array = input()
    length = len(array)
    print(findSpecialSubsequencesAG(array, length))