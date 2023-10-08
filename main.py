# 1. Calculati suma a n numere naturale
from math import sqrt


def CalcSumN (n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

# 2. Verificati daca n citit de la tastatura este prim
def CheckPrime (n) :
    if (n == 2):
        return True
    if (n < 2):
        return False
    if (n % 2 == 0):
        return False

    for i in range (3, int(sqrt(n)) + 1, 2):
        if (n % i == 0):
            return False

    return True

# 3. Calculati CMMDC a doua numere
def CMMDC (a, b):
    if (b == 0) :
        return a
    return CMMDC(b, a % b)

if __name__ == '__main__':
    n1 = int(input("1. We calculate the sum of n number \n n = "))
    print("The sum is : ", CalcSumN(n1))

    n2 = int(input("2. We check if a given number is prime \n n = "))
    print("True = prime / False = not prime : ", CheckPrime(n2))

    n3 = int(input("3. We calculate CMMDC of a and b \n a = "))
    n4 = int(input("b = "))
    print("The CMMDC is : ", CMMDC(n3, n4))



