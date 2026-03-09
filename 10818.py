n = map(int, input().split())

numbers = list(map(int, input().split()))

min_num = numbers[0]
max_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print(min_num, max_num)
