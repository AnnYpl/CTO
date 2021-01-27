def main():
    print("Колькулятор")
    while True:
        print("Что делаем? :\n"
              "Слогаем: +\n"
              "Вычетаем: -\n"
              "Умножаем: *\n"
              "Делим: /\n"
              "Выйти: e\n")
        action = input("Действие: ")
        if action == "e":
            print("Выход из программы")
            break
        if action in ('+', '-', '*', '/'):
            a = float(input("a = "))
            b = float(input("b = "))
            if action == '+':
                print('%.2f + %.2f = %.2f' % (a, b, a+b))
            elif action == '-':
                print('%.2f - %.2f = %.2f' % (a, b, a-b))
            elif action == '*':
                print('%.2f * %.2f = %.2f' % (a, b, a*b))
            elif action == '/':
                if b != 0:
                    print('%.2f / %.2f = %.2f' % (a, b, a/b))
                else:
                    print("Деление на ноль!")


if __name__ == '__main__':
    main()


