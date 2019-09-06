# Indian Number System

name = {
    '0': '-', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
    '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen',
    '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy',
    '80': 'eighty', '90': 'ninety', '00': 'hundred', '000': 'thousand', '00000': 'lakh', '0000000': 'crore'
}


def number_name(n):
    try:
        string = str(int(n))  # Just converting twice to truncate zero from the beginning.
        if len(string) == 1:
            return name[string]
        elif len(string) == 2:
            return f"{name[string[0]+'0']}{name['0']}{name[string[-1]]}"
        elif len(string) == 3:
            return f"{name[string[0]]} {name['00']} {number_name(string[1:])}"
        elif len(string) == 4:
            return f"{name[string[0]]} {name['000']} {number_name(string[1:])}"
        elif len(string) == 5:
            return f"{number_name(string[0:2])} {name['000']} {number_name(string[2:])}"
        elif len(string) == 6:
            return f"{number_name(string[0:1])} {name['00000']} {number_name(string[1:])}"
        elif len(string) == 7:
            return f"{number_name(string[0:2])} {name['00000']} {number_name(string[2:])}"
        elif len(string) == 8:
            return f"{number_name(string[0:1])} {name['0000000']} {number_name(string[1:])}"
        elif len(string) == 9:
            return f"{number_name(string[0:2])} {name['0000000']} {number_name(string[2:])}"
        elif len(string) == 10:
            return f"{number_name(string[0:3])} {name['0000000']} {number_name(string[3:])}"

    except (NameError, ValueError):
        return 'Seems you have entered non-integer value'


print(number_name(8257803929))
