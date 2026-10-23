# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example 343, (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage

from euler import solution

words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}

@solution
def solve():
    word_list = []
    total_len = 0
    for x in range(1,1001):
        if len(str(x)) == 1:
            word_list.append(words[x])
        elif len(str(x)) == 2:
            if x in words:
                word_list.append(words[x])
            else:
                word_list.append(words[int(str(str(x)[0]+"0"))] + words[int(str(x)[1])])
        elif len(str(x)) == 3:
            if str(x)[-2:] == "00":
                word_list.append(words[int(str(x)[0])]+words[100])
            else:
                if int(str(x)[-2:]) in words:
                    word_list.append(words[int(str(x)[0])]+words[100]+"and"+words[int(str(x)[-2:])])
                else:
                    word_list.append(words[int(str(x)[0])]+words[100]+"and"+words[int(str(str(x)[1]+"0"))] + words[int(str(x)[2])])
        elif len(str(x)) == 4:
            if str(x)[-3:] == "000":
                word_list.append(words[int(str(x)[0])]+words[1000])
    for word in word_list:
        total_len += len(word)
    return total_len

solve()