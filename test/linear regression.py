
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 1. Подготовка данных
x = np.array([...])  # ваши значения x
y = np.array([...])  # соответствующие значения y

# Преобразуем x через логарифм
log_x = np.log(x)

# Добавляем константу для свободного члена
log_x_with_const = sm.add_constant(log_x)

# 2. Построение регрессионной модели
model = sm.OLS(y, log_x_with_const)
results = model.fit()

# 3. Вывод результатов
print(results.summary())

# 4. Визуализация результата
plt.scatter(log_x, y, label="Данные")
plt.plot(log_x, results.fittedvalues, color='red', label="Линия регрессии")
plt.xlabel("log(x)")
plt.ylabel("y")
plt.legend()
plt.show()