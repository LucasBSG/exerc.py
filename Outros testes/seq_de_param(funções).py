def soma_todos(*nums):
    soma = 0
    for num in nums:
        soma += num

    return soma

s = soma_todos(4,52,3,26)

print(s)

s2 = soma_todos(3,2,6,62,35)

print(s2)