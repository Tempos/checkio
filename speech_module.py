"""Stephen's speech module is broken.
This module is responsible for his number pronunciation.
He has to click to input all of the numerical digits in a figure,
so when there are big numbers it can take him a long time.
Help the robot to speak properly and increase his number processing speed
by writing a new speech module for him.
All the words in the string must be separated by exactly one space character.
Be careful with spaces -- it's hard to see if you place two spaces instead one.

Input: A number as an integer.
Output: The string representation of the number as a string.

How it is used: This concept may be useful for the speech synthesis software
or automatic reports systems. This system can also be used when writing a chatbot
by assigning words or phrases numerical values and having a system retrieve
responses based on those values.

Precondition: 0 < number < 1000"""

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    res, num = [], str(number)

    if len(num) > 2:
        res.append(str(FIRST_TEN[int(num[0])-1]))
        res.append(HUNDRED)
    if len(num) > 1:
        if int(num[-2:]) >= 20:
            res.append(OTHER_TENS[int(num[-2]) - 2])
        elif int(num[-2:]) >= 10:
            res.append(SECOND_TEN[int(num[-2:]) - 10])
            return ' '.join(res)
    if int(num[-1]) > 0:
        res.append(FIRST_TEN[int(num[-1]) - 1])
    return ' '.join(res)


if __name__ == '__main__':
    # checkio(12)
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
