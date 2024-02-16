def get_biggest(numbers):
    if not numbers:
        return -1

    li = [str(i) for i in numbers]
    lenght = len(li)

    for i in range(lenght):
        index = i
        for j in range(i + 1, lenght):
            if li[j] + li[index] > li[index] + li[j]:
                index = j
        li[i], li[index] = li[index], li[i]

    return int(''.join(li))