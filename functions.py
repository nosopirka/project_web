def perevod(a):
    n = a["num"]
    s1 = a["sis1"]
    s2 = a["sis2"]
    if s1 != 10:
        ch = 0
        for i in range(len(str(n))):
            ch += int(str(n)[i]) * (s1 ** (len(str(n)) - i - 1))
        n = ch
        s1 = 10
    ot = ""
    while n // s2 != 0:
        ot = str(n % s2) + ot
        n //= s2
    ot = str(n % s2) + ot
    return ot


def sequences(a):
    if a["f"] == "a":
        a1 = a["a1/b1"]
        d = a["d/q"]
        n = a["n"]
        s = (2 * a1 + (n - 1) * d) * n / 2
    else:
        b1 = a["a1/b1"]
        q = a["d/q"]
        n = a["n"]
        if n == 1:
            s = b1
        elif n == 0:
            s = 0
        else:
            s = b1 * ((q ** n) - 1) / (q - 1)
    return s


def solving(ur):
    try:
        i1 = ur.find("^")
        if i1 != -1:
            if i1 == 1:
                a = 1
            else:
                a = float(ur[:i1 - 1])
            i2 = ur.rfind("x")
            if i2 > i1:
                b = float(ur[i1 + 5:i2])
                if ur[i1 + 3] == "-":
                    b *= -1
                c = float(ur[i2 + 4:])
                if ur[i2 + 2] == "-":
                    c *= -1
                d = b * b - 4 * a * c
                if d < 0:
                    return "No solutions"
                x1 = (-b + d ** (0.5)) / (2 * a)
                x2 = (-b - d ** (0.5)) / (2 * a)
            else:
                b = 0
                c = float(ur[i1 + 5:])
                if ur[i1 + 3] == "-":
                    c *= -1
                x1 = -((-c) ** (0.5))
                x2 = ((-c) ** (0.5))
        else:
            i2 = ur.find("x")
            if i2 != -1:
                if i2 == 0:
                    b = 1
                else:
                    b = float(ur[:i2])
                c = float(ur[i2 + 4:])
                x1 = x2 = -c / b
            elif float(ur) == 0:
                return "For any x"
        return str(x1) + "%" + str(x2)
    except (TypeError, TypeError):
        return "Can't solve"
