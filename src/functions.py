from re import split


def expr(s: str) -> float:
    """
        Функция, которая находит значение арифметического выражения (обработка + и -)
        :param s: арифметическое выражение
        :return: Возвращает значение арфиметического выражения
    """
    # проверка ошибок
    if s == "":
        raise ValueError
    s_ = s.replace("-", "").replace("+", "").replace(".", "")
    s_ = s_.replace("*", "").replace("/", "")
    if not s_.isdigit():
        raise ValueError

    # предобработка строк
    s = "0+" + s
    s_ = s.replace("+-", "+~").replace("/-", "/~")
    s_ = s_.replace("*-", "*~").replace(" ", "")
    splitten_s = split(r'\s*([+-])\s*', s_)

    # вызовы функции term
    splitten_s_clean = []
    for elem_id in range(len(splitten_s)):
        if splitten_s[elem_id] != "":
            splitten_s_clean.append(splitten_s[elem_id])
    splitten_s = splitten_s_clean
    for elem_id in range(len(splitten_s)):
        if splitten_s[elem_id] != "+" and splitten_s[elem_id] != "-":
            splitten_s[elem_id] = term(splitten_s[elem_id])

    # вычисление итогового значения
    result = 0.0
    prev_elem = 1  # 0 - число, 1 - плюс, 2 - минус
    for elem_id in range(len(splitten_s)):
        if prev_elem == 1:
            if splitten_s[elem_id] == "+":
                raise SyntaxError
            elif splitten_s[elem_id] == "-":
                raise SyntaxError
            else:
                result += float(splitten_s[elem_id])
        elif prev_elem == 2:
            if splitten_s[elem_id] == "+":
                raise SyntaxError
            elif splitten_s[elem_id] == "-":
                raise SyntaxError
            else:
                result -= float(splitten_s[elem_id])
        else:
            if splitten_s[elem_id] != "+" and splitten_s[elem_id] != "-":
                raise SyntaxError

        if splitten_s[elem_id] == "+":
            prev_elem = 1
        elif splitten_s[elem_id] == "-":
            prev_elem = 2
        else:
            prev_elem = 0
    return result


def term(s: str) -> float:
    """
        Функция, которая находит значение арифметического выражения (обработка * и /)
        :param s: арифметическое выражение
        :return: Возвращает значение арфиметического выражения
    """
    # проверка ошибок
    if s == "":
        raise ValueError
    s_ = s.replace("-", "").replace("+", "").replace(".", "")
    s_ = s_.replace("*", "").replace("/", "").replace("~", "")
    if not s_.isdigit():
        raise ValueError

    # предобработка строк
    splitten_s = split(r'\s*([*/])\s*', s)

    # вызовы функции term
    for elem_id in range(len(splitten_s)):
        if splitten_s[elem_id] == "":
            raise SyntaxError
        if splitten_s[elem_id] != "*" and splitten_s[elem_id] != "/":
            splitten_s[elem_id] = factor(splitten_s[elem_id])

    # вычисление итогового значения
    result = 1.0
    prev_elem = 1  # 0 - число, 1 - умножить, 2 - разделить
    for elem_id in range(len(splitten_s)):
        if prev_elem == 1:
            if splitten_s[elem_id] == "*":
                raise SyntaxError
            elif splitten_s[elem_id] == "/":
                raise SyntaxError
            else:
                result *= float(splitten_s[elem_id])
        elif prev_elem == 2:
            if splitten_s[elem_id] == "*":
                raise SyntaxError
            elif splitten_s[elem_id] == "/":
                raise SyntaxError
            else:
                if splitten_s[elem_id] == 0:
                    raise ZeroDivisionError
                result /= float(splitten_s[elem_id])
        else:
            if splitten_s[elem_id] != "*" and splitten_s[elem_id] != "/":
                raise SyntaxError

        if splitten_s[elem_id] == "*":
            prev_elem = 1
        elif splitten_s[elem_id] == "/":
            prev_elem = 2
        else:
            prev_elem = 0
    return result


def factor(s: str) -> float:
    """
        Функция, которая обрабатывает число и возможный знак
        :param s: число
        :return: Возвращает число
    """
    s = s.replace("~", "-")
    if s == "":
        return 0
    return float(s)
