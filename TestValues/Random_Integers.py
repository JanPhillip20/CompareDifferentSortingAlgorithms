from random import randint


def get_random_numbers_by_given_length(length):

    list_of_numbers = []
    for x in range(length):
        random = randint(0, 10000)
        list_of_numbers.append(random)

    return list_of_numbers
