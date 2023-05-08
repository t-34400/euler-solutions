limit_value = 4_000_000

previous_value = 0
current_value = 1
sum_of_values = 0
while True:
    next_value = previous_value + current_value
    if next_value % 2 == 0:
        sum_of_values += next_value
    if next_value >= limit_value:
        break

    previous_value = current_value
    current_value = next_value

print(sum_of_values)