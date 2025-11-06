def result(array1, array2):

    answer = int(array1[0])
    for index, element in enumerate(array2):

        if array2[index] == "*":
            answer = answer * int(array1[index+1])

        elif array2[index] == "/":
            answer = answer / int(array1[index+1])

        elif array2[index] == "+":
            answer = answer + int(array1[index+1])

        elif array2[index] == "-":
            answer = answer - int(array1[index+1])
        print(answer)
    return answer
