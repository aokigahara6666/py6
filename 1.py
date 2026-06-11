def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)


assert average_num([1, 1]) == 1.0
assert average_num([2.5, 3.5]) == 3.0
assert average_num([1, 2, 3, 4, 5]) == 3.0
assert average_num([10, 20, 30]) == 20.0
assert average_num(["1", "2", "3"]) == 2.0
assert average_num([1.5, "2", 2.5]) == 2.0
assert average_num(["hello", 1, 2]) == "Bad request"
assert average_num([1, [2], 3]) == "Bad request"

print("Все тесты assert для average_num пройдены успешно!")