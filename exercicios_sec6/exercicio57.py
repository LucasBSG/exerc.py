def multi_numeros(*numeros):
    result = 1
    for num in numeros:
        result *= num

    return result

print(multi_numeros(7,4,2,3))