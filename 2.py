def is_palindrome(text: str) -> bool:
    clean_text = "".join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]


assert is_palindrome("шалаш") == True
assert is_palindrome("привет") == False
assert is_palindrome("Лёша на полке клопа нашёл") == True
assert is_palindrome("А роза упала на лапу Азора!") == True
assert is_palindrome("12321") == True
assert is_palindrome("12345") == False

print("Все тесты assert для is_palindrome пройдены успешно!")