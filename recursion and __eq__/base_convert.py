# int, int -> string
# Given integer num and base b, converts num to a string representation in base b
def convert(num, b):
    if b == 10:
        return str(num)
    elif b is None:
        raise ValueError
    # elif num == 0:
    #     return ''
    elif b < 10:
        remainder = num % b
        return convert(num // b, b) + str(remainder)
    elif 16 >= b > 10:
        remainder = num % b
        if remainder < 10:
            return (convert(num//b, b)) + str(remainder)
        elif remainder == 10:
            return (convert(num//b, b)) + "A"
        elif remainder == 11:
            return (convert(num//b, b)) + "B"
        elif remainder == 12:
            return (convert(num//b, b)) + "C"
        elif remainder == 13:
            return (convert(num//b, b)) + "D"
        elif remainder == 14:
            return (convert(num//b, b)) + "E"
        elif remainder == 15:
            return (convert(num//b, b)) + "F"
