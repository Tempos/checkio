# def count_words(text: str, words: set) -> int:
#     count, text = 0, text.lower()
#     for word in words:
#         if word in text:
#             count += 1
#     return count


def count_words(text: str, words: set) -> int:
    return sum(1 for word in words if text.lower().count(word) > 0)
    # return sum({word: 1 for word in words if text.lower().count(word) > 0}.values())


print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))
