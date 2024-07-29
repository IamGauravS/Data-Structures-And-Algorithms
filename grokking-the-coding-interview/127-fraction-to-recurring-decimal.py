def fraction_to_decimal(numerator, denominator):
    if numerator == 0:
        return "0"

    res = []
    if (numerator < 0) != (denominator < 0):  ## check for final negative sign
        res.append("-")

    numerator, denominator = abs(numerator), abs(denominator)
    quotient, remainder = divmod(numerator, denominator)
    res.append(str(quotient))

    if remainder == 0:
        return "".join(res)

    res.append(".")
    remainder_map = {}
    while remainder != 0:
        if remainder in remainder_map:
            res.insert(remainder_map[remainder], "(")  ## find the place where to insert starting bracket
            res.append(")")  ## insert closing bracket
            break

        remainder_map[remainder] = len(res)
        remainder *= 10
        quotient, remainder = divmod(remainder, denominator)
        res.append(str(quotient))

    return "".join(res)