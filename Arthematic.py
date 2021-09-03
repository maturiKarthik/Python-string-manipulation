# checks given number is even or not
def check_number_is_even(number):
    if int(number) % 2 == 0:
        return True
    else:
        return False


# check given number is prime or not
def check_number_is_prime(number):
    count = 0
    for i in range(number):
        if i != 0 and i != 1 and number % i == 0:
            count = count + 1

    if count == 0:
        return True
    else:
        return False
