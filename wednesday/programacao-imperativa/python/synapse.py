

def fatorial(value):
    result = 1
    for fator in range(value,1,-1):
        result *= fator
    return result


def fibonacci(index):
    left, right = 0 , 1
    counter = 0
    for _ in range(index):
        left, right = right, left + right
    return left

def check_prime(index):
    if index <= 1:
        return False
    for i in range(2, index/2):
        x = index % i
        if x == 0:
            return False
    return True