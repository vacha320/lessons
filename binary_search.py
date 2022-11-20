def binary_search(nambers, item):
    start = 0
    end = len(nambers) - 1

    while start <= end:
        middle = int(start + end) // 2
        target = nambers[middle]

        if target == item:
            return middle

        elif target > item:
            end = middle - 1

        else:
            start = middle + 1

n = list(range(1, 99))
print(binary_search(n, 4))


