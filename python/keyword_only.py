def total(initial=5, *numbers):
    count = initial
    for num in numbers:
        count += num
    print(count)

total(10, 1, 2, 3)
total(initial=10)
