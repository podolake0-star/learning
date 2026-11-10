import numpy as np
import sklearn

from sklearn.linear_model import LinearRegression

# Генерация синтетических данных
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Добавляем столбец из единиц для свободного члена
X_b = np.c_[np.ones((100, 1)), X]

# Вычисляем оптимальные параметры с помощью нормального уравнения
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Выводим найденные коэффициенты
print("Коэффициенты модели (свободный член, наклон):", theta_best.flatten()



      )
