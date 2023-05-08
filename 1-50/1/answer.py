def answer_1(target_number):
    return sum([i for i in range(1, target_number + 1) if i % 3 == 0 or i % 5 == 0])


def answer_2(target_number):
    sum_of_multiple_of_3 = get_sum_of_multiples_of(target_number, 3)
    sum_of_multiple_of_5 = get_sum_of_multiples_of(target_number, 5)
    sum_of_multiple_of_15 = get_sum_of_multiples_of(target_number, 15)
    return sum_of_multiple_of_3 + sum_of_multiple_of_5 - sum_of_multiple_of_15


def get_sum_of_multiples_of(target_number, multiplicand):
    num_of_multiple = target_number // multiplicand
    max_multiple = multiplicand * num_of_multiple
    return (multiplicand + max_multiple) * num_of_multiple // 2


target_number = 1000

print(answer_1(target_number))
print(answer_2(target_number))
