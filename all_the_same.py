""" In this mission you should check if all elements in the given list are equal.
    Precondition: all elements of the input list are hashable"""

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1
    # return True if not elements or (len(elements) and elements.count(elements[0])) == len(elements) else False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
