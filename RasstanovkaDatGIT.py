import pyautogui
import random
import time

# ГОД МЕНЯЕТСЯ в 25 строке
# Дается 5 секунд после ввода месяца дальше работает как надо
# Расчитано на 50 итераций

# Функция для ввода месяца
def get_month():
    while True:
        try:
            month = int(input("Введите номер месяца (1-12): "))
            if 1 <= month <= 12:
                return str(month).zfill(2)  # Добавляем ведущий ноль, если нужно
            else:
                print("Введите корректный номер месяца.")
        except ValueError:
            print("Введите число.")


# Функция для печати текста с рандомной ссылкой и нажатия кнопки вправо
def print_text_and_press_right(phase, links, day, month):
    link = random.choice(links)
    text = f"{day}.{month}.25 - ({phase}) - {link}"
    print(text)
    pyautogui.typewrite(text)
    pyautogui.press("right")
    time.sleep(0.5)


# Функция для фазы 1
def phase1(month):
    links = [
        "https://site.com/public",
    ]
    days = sorted(random.choices(range(1, 29), k=30))
    for day in days:
        print_text_and_press_right("TG", links, str(day).zfill(2), month)


# Функция для фазы 2
def phase2(month):
    links = [
        "https://site.com/public",
    ]
    days = sorted(random.choices(range(1, 29), k=10))
    for day in days:
        print_text_and_press_right("OK", links, str(day).zfill(2), month)


# Функция для фазы 3
def phase3(month):
    links = [
        "https://site.com/public",
    ]
    days = sorted(random.choices(range(1, 29), k=10))
    for day in days:
        print_text_and_press_right("VK", links, str(day).zfill(2), month)


# Основная функция
def main():
    month = get_month()
    print("Начало через 5 секунд...")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)

    try:
        phase1(month)
        phase2(month)
        phase3(month)
    except KeyboardInterrupt:
        print("Скрипт остановлен пользователем.")


# Вызов основной функции
if __name__ == "__main__":
    main()
