def getSideDigits(s):
    equal_pos = s.find('=')
    digits = []
    digitsAfterEqual = {}

    left_side = s[:equal_pos]
    right_side = s[equal_pos + 1:]

    i = 0
    while i < len(left_side):
        if left_side[i].isspace():
            i += 1
            continue
        if i >= 2 and left_side[i-2:i] == 'X^':
            i += 1
            continue
        if left_side[i].isdigit() or left_side[i] in '-':
            num = ''
            if left_side[i] in '+-':
                num = left_side[i]
                i += 1
            while i < len(left_side) and left_side[i].isspace():
                i += 1
            while i < len(left_side) and left_side[i].isdigit():
                num += left_side[i]
                i += 1
            if i < len(left_side) and left_side[i] == '.':
                num += '.'
                i += 1
                while i < len(left_side) and left_side[i].isdigit():
                    num += left_side[i]
                    i += 1
            if num and num != '+' and num != '-':
                digits.append(num)
        i += 1

    i = 0
    count = 0
    while i < len(right_side):
        if right_side[i].isspace():
            i += 1
            continue
        if i >= 2 and right_side[i-2:i] == 'X^':
            i += 1
            continue
        if right_side[i].isdigit() or right_side[i] in '-':
            num = ''
            if right_side[i] in '+-':
                num = right_side[i]
                i += 1
            while i < len(right_side) and right_side[i].isspace():
                i += 1
            while i < len(right_side) and right_side[i].isdigit():
                num += right_side[i]
                i += 1
            if i < len(right_side) and right_side[i] == '.':
                num += '.'
                i += 1
                while i < len(right_side) and right_side[i].isdigit():
                    num += right_side[i]
                    i += 1
            if num and num != '+' and num != '-':
                digitsAfterEqual[str(count)] = num
                count += 1
        i += 1

    return digits, digitsAfterEqual


def calculateType(x, x1):
    if x.find('.') != -1 and x1.find('.') != -1:
        return round(float(x) - float(x1), 1)
    elif x.find('.') != -1:
        return round(float(x) - int(x1), 1)
    elif x1.find('.') != -1:
        return round(int(x) - float(x1), 1)
    else:
        return int(x) - int(x1)


def reduceFunct(s):
    sideDigits = getSideDigits(s)
    print(sideDigits)
    left_side = sideDigits[0]
    right_side = sideDigits[1]
    i = 0
    while i < len(left_side):
        if str(i) in right_side:
            left_side[i] = str(calculateType(left_side[i],
                                             right_side[str(i)]))
        i += 1
    return left_side


def changeSign(s):
    if s.find('.'):
        return float(s) * -1
    else:
        return int(s) * -1


def printReduced(reducedf):
    sign = {}
    s = ""
    i = 0
    while i < len(reducedf):
        if reducedf[i].find('-') != -1:
            sign[i] = "-"
            reducedf[i] = changeSign(reducedf[i])
        else:
            sign[i] = "+"

        if i == 0:
            s += f"{reducedf[i]} * X^{i}"
        else:
            s += f" {sign[i]} {reducedf[i]} * X^{i}"
        i += 1

    s += " = 0"
    print(s)
    return i - 1
