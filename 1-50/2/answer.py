limit_value = 4_000_000

previous_value = 0
current_value = 1
sum_of_values = 0
while current_value < limit_value:
    if current_value % 2 == 0:
        sum_of_values += current_value

    previous_value, current_value = current_value, previous_value + current_value

print(sum_of_values)