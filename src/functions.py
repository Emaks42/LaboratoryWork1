def expr(s: str) -> float:
    """
        Функция, которая находит значение арифметического выражения (обработка + и -)
        :param s: арифметическое выражение
        :return: Возвращает значение арфиметического выражения
    """
    s = s.replace(" ", "")
    exp = s.split("+")
    exp_ = [i.split("-") for i in exp]

    for i in range(len(exp_)):
        if len(exp_[i]) == 1:
            exp_[i] = term(exp_[i][0])
        else:
            for j in range(len(exp_[i])):
                exp_[i][j] = term(exp_[i][j])

    for i in range(len(exp_)):
        if type(exp_[i]) == list:
            start_num = exp_[i][0]
            for j in range(1, len(exp_[i])):
                start_num -= exp_[i][j]
            exp_[i] = start_num

    return sum(exp_)


def term(s: str) -> float:
    """
        Функция, которая находит значение арифметического выражения (обработка * и /)
        :param s: арифметическое выражение
        :return: Возвращает значение арфиметического выражения
    """
    s = s.replace(" ", "")
    ter = s.split("*")
    ter_ = [i.split("/") for i in ter]

    for i in range(len(ter_)):
        if len(ter_[i]) == 1:
            ter_[i] = factor(ter_[i][0])
        else:
            for j in range(len(ter_[i])):
                ter_[i][j] = factor(ter_[i][j])

    for i in range(len(ter_)):
        if type(ter_[i]) == list:
            start_num = ter_[i][0]
            for j in range(1, len(ter_[i])):
                start_num /= ter_[i][j]
            ter_[i] = start_num

    term_ans = 1
    for obj in ter_:
        term_ans *= obj
    return term_ans


def factor(s: str) -> float:
    """
        Функция, которая обрабатывает число и возможный знак
        :param s: число
        :return: Возвращает число
    """
    return float(s)
