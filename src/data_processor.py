# src/data_processor.py
def input_numbers():
    print("Введите целые числа через пробел:")
    try:
        return list(map(int, input().strip().split()))
    except ValueError:
        print("Ошибка! Вводите только целые числа.")
        return []

def input_string():
    print("Введите строку:")
    return input().strip()

def process_numbers(numbers):
    if not numbers:
        return {"error": "Список чисел пуст"}
    return {
        "numbers": numbers,
        "sum": sum(numbers),
        "average": round(sum(numbers) / len(numbers), 2),
        "max": max(numbers),
        "min": min(numbers),
        "count": len(numbers)
    }

def process_string(s):
    if not s:
        return {"error": "Строка пустая"}
    return {
        "length": len(s),
        "words": len(s.split()),
        "uppercase": s.upper(),
        "lowercase": s.lower(),
        "has_digit": any(c.isdigit() for c in s)
    }

def main():
    print("=== Модуль обработки данных ===\n")
    
    nums = input_numbers()
    print("\nРезультат чисел:", process_numbers(nums))
    
    text = input_string()
    print("\nРезультат строки:", process_string(text))

if __name__ == "__main__":
    main()
