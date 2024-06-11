def find_password(n):
    password = ''
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

n = int(input("Введите число от 3 до 20: "))
password = find_password(n)
print("Пароль для числа", n, ":", password)