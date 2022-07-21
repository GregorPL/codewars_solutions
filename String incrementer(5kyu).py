import re

def increment_string(strng):
    reg_num = r'[0-9]+$'

    n = re.search(reg_num, strng)

    if n:
        rest = strng.replace(n[0], '')

        return rest + str(int(n[0]) + 1).zfill(len(n[0]))
    else:
        return strng + '1'

print(increment_string("UcHhLqk87054917"))


    