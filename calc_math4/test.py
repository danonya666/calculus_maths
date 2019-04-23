from math import pi, sin
from random import uniform

# задаем модельные значения параметров:
A, B = 10.0, 0.4

# задаём модельную функцию
f = lambda x, a, b: a * sin(b * x)

# задаём шаг дискретной сетки на интервале x = 0...2*pi
h = 0.5

# задаём амплитуду "погрешностей"
distortion = 0.5

# рассчитываем модельные значения функции y = a * sin(b * x)
model = tuple((i * h, f(i * h, A, B)) for i in range(0, int(2 * pi / h) + 1))

# рассчитываем "экспериментальные" значения (модельные значения с погрешностями)
data = tuple((x, y + uniform(-distortion, distortion)) for x, y in model)

# выводим модель на экран
print("--- начальные данные ---")
print("Модельные значения параметров: A = %f, B = %f" % (A, B))
print("Значения модельной функции y = A sin (b x) и \"экспериментальные\" данные (y~):")
print("\n".join("x = %f\ty = %e\ty~=%e" % (m[0], m[1], d[1]) for m, d in zip(model, data)))

# рассчитываем значения параметров по экспериментальным данным
print("--- расчет ---")

# начальное приближение
a, b = 5.0, 1.0

# целевая функция по МНК
F = lambda a, b, data: sum((y - f(x, a, b)) ** 2 for x, y in data)

total_iterations = 0

shift = 1.
for i in range(6):

    shift *= 1e-1
    print("итерации с шагом %f" % shift)

    shifts = (
        (0.0, 0.0),
        (-shift, -shift),
        (0.0, -shift),
        (shift, -shift),
        (shift, 0.0),
        (shift, shift),
        (0.0, shift),
        (-shift, shift),
        (-shift, 0.0)
    )

    iteration = 0
    choices = tuple(F(a + shA, b + shB, data) for shA, shB in shifts)
    choice = choices.index(min(choices))
    while choice != 0 and iteration < 1000:
        a += shifts[choice][0]
        b += shifts[choice][1]
        if not iteration % 10:
            print("итерация %d\tA = %f\tB = %f\tцелевая функция = %e" % (iteration, a, b, choices[choice]))
        iteration += 1
        choices = tuple(F(a + shA, b + shB, data) for shA, shB in shifts)
        choice = choices.index(min(choices))
    print("итерация %d\tA = %f\tB = %f\tцелевая функция = %e" % (iteration - 1, a, b, choices[choice]))
    total_iterations += iteration

# вывод результата
print("--- результат расчета ---")
print("Вычисленные значения параметров: A = %f, B = %f" % (a, b))
print("Значение целевой функции МНК: %e" % F(a, b, data))
print("Количество итераций: %d" % total_iterations)
