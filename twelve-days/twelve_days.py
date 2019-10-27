GIFTS = [   "twelve Drummers Drumming",
            "eleven Pipers Piping",
            "ten Lords-a-Leaping",
            "nine Ladies Dancing",
            "eight Maids-a-Milking",
            "seven Swans-a-Swimming",
            "six Geese-a-Laying",
            "five Gold Rings",
            "four Calling Birds",
            "three French Hens",
            "two Turtle Doves",
            "a Partridge in a Pear Tree"
        ]
ORDINAL = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
           'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
def verse(day_number):
    gifts = GIFTS[-day_number:]
     # print("length of gift {} larger than 1 or not".format(gifts))
    if len(gifts) > 1:
        gifts[:-1]=[', '.join(gifts[:-1])] # join gift before the last one
        # ['three French Hens, two Turtle Doves', 'a Partridge in a Pear Tree']
        # print("length of gift {} larger than 1".format(gifts))
    gifts = ', and '.join(gifts)
    # print("gift {} after join".format(gifts))
    return 'On the {} day of Christmas my true love gave to me: {}.'.format(
        ORDINAL[day_number], gifts
    )
def recite(start_verse, end_verse):
    return[verse(n) for n in range(start_verse, end_verse + 1)]

# print(recite(1,3))
