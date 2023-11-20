def string_calculator(strings, round_value=4):
    operator = ["+", "-", "*", "/", "="]
    strings = strings + "=" if strings[-1] !=  "=" else strings
    last_operator_pos = 0
    string_break = []
    for i, s in enumerate(strings):
        if s in operator:
            v = strings[last_operator_pos : i].strip()
            if v != "":
                string_break.append(v)
                string_break.append(s)
                last_operator_pos = i + 1

    while len(string_break) > 2:
        temp = string_break[0] + string_break[1] +  string_break[2]
        del string_break[0:3]
        string_break.insert(0, str(eval(temp, {}, {})))
        print(string_break)

    result = 0
    if len(string_break) == 2:
        result = float(string_break[0])
    return round(result, round_value)

strings = input("계산식을 입력하세요> ").strip()
result = string_calculator(strings)
print(f"계산 결과: {result}")