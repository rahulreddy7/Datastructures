

def calculate(input):

    i = 0
    j = len(input) - 1
    while (i < j):
        if input[i] == input[j]:
            i += 1
            j=len(input)-1
        else:
            j -= 1
    return input[i]

input = 'GeeksQuiz'
out=calculate(input)
print(out)
