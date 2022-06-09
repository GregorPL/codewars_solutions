num2word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
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
}


def number2words(n):

    def get_hundred(n):
        return num2word[int(n/100)] + " hundred"

    def get_thousand(n):
        return num2word[int(n/1000)] + " thousand"

    n2w = []

    while n > 0:y
        if n >= 1000:
            n2w.append(get_thousand(n))
    return " ".join(n2w)

    # # if n >= 1000:
    # #     n2w += num2word[int(n/1000)] + " " + "thousend"
    #
    # return n2w


print(number2words(22345))