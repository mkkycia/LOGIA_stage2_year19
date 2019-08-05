def lustro(liczba, proby):
    for i in range(proby):
        if liczba == int(str(liczba)[::-1]) and i != 0:
            return liczba
        liczba += int(str(liczba)[::-1])
    if liczba == int(str(liczba)[::-1]):
        return liczba
    return -1

print(lustro(434,1))
print(lustro(42,1))
print(lustro(298,3))
print(lustro(989,8))
print(lustro(98319, 5))
print(lustro(98319, 6))
print(lustro(98319, 7))
print(lustro(4,5))
print(lustro(5,2))
print(lustro(66666,2))
print(lustro(9899,8))
