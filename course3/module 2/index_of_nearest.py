def index_of_nearest(numbers, number):
    if not numbers:
        return -1

    closest_index = 0
    closest_difference = abs(numbers[0] - number)

    for i in range(1, len(numbers)):
        difference = abs(numbers[i] - number)
        if difference < closest_difference:
            closest_index = i
            closest_difference = difference

    return closest_index
