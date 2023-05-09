def is_prime_number(target, prime_numbers):
    for p in prime_numbers:
        if target % p == 0:
            return False
    return True


def get_next_prime_number(current_prime_number, prime_numbers):
    number = current_prime_number + 1
    while not is_prime_number(number, prime_numbers):
        number += 1
    
    return number


target_number = 600_851_475_143

max_prime_factor = target_number
current_prime_number = 2
prime_numbers = (current_prime_number,)

while (current_prime_number * current_prime_number) < target_number:
    while target_number % current_prime_number == 0:
        target_number //= current_prime_number
        max_prime_factor = current_prime_number
    
    current_prime_number = get_next_prime_number(current_prime_number, prime_numbers)
    prime_numbers += (current_prime_number,)

print(max_prime_factor)