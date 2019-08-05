def szyfruj_znak(znak, klucz):
    return chr((ord(znak) - ord('A') + klucz) % 26 + ord('A'))

def ktora(litera):
    return ord(litera)-ord('A')

def deszyfr(tekst, klucz):
    pom = ""
    dl = len(klucz)
    for i in range(len(tekst)):
        k = ktora(klucz[i % dl])
        pom = pom + szyfruj_znak(tekst[i], 26 - k)
    return pom
