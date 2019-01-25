"""Here you should find the length of the longest substring that consists of the same letter.
For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa".
The last substring is the longest one which makes it an answer.

Input: String.
Output: Int."""


def long_repeat(line):
    last_letter = ''
    max_count = count = 1
    for letter in line:
        if letter != last_letter:
            last_letter = letter
            count = 1
        else:
            count += 1
            if count > max_count:
                max_count = count
    return max_count if line else 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
