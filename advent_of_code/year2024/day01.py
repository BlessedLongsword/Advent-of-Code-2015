# Day 1

# Input

from util.get_input import get_input

def get_lists():
    lists = list(list(map(int, line.split('   '))) for line in get_input(2024, 1).splitlines())
    return [entry[0] for entry in lists], [entry[1] for entry in lists]


# Part 1

def calculate_distance_between_lists(left_list, right_list):
    left_list.sort()
    right_list.sort()
    return sum(max(a, b) - min(a, b) for a,b in zip(left_list, right_list))

print(f'The total distance between the lists is {calculate_distance_between_lists(*get_lists())}')


# Part 2

from collections import Counter

def calculate_similarity_score(left_list, right_list):
    occurrences = Counter(right_list)
    return sum(entry * occurrences[entry] for entry in left_list)

print(f'The similarity score between the lists is {calculate_similarity_score(*get_lists())}.')
