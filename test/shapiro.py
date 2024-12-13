from scipy import stats

# Ваши данные
data = [2.5, 3.6, 2.9, 3.2, 4.1, 2.8, 3.7, 3.3]

# Выполняем тест Шапиро-Уилка
stat, p_value = stats.shapiro(data)

print(f"Статистика теста W: {stat}")
print(f"p-значение: {p_value}")

# Проверяем гипотезу
if p_value > 0.05:
    print("Распределение нормальное (не отвергаем H0)")
else:
    print("Распределение не нормальное (отвергаем H0)")
