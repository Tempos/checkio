"""Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'

Input: Time in a 24-hour format (as a string).
Output: Time in a 12-hour format (as a string).
Precondition:
'00:00' <= time <= '23:59'"""


def time_converter(time):
    h, m = (int(s) for s in time.split(':'))
    return "{}:{:02d} {}".format(h % 12 if h % 12 != 0 else 12, m, 'a.m.' if (h < 12) else 'p.m.')


if __name__ == '__main__':
    print(time_converter('00:00'))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
