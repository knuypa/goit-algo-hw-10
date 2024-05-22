import numpy as np
import sys
import subprocess

# Спроба імпортувати SciPy, якщо він не встановлений, то встановити
try:
    import scipy.integrate as spi
except ImportError:
    print("SciPy не встановлено. Спроба встановити...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scipy"])
    import scipy.integrate as spi  # Повторне імпортування після встановлення

# Визначення функції для інтегрування
def f(x):
    return x**2

# Межі інтегрування
a = 0
b = 2
upper_bound = f(b)  # Верхня межа функції у вказаному діапазоні

# Кількість випадкових точок для методу Монте-Карло
N = 100000

# Генерація випадкових точок
random_x = np.random.uniform(a, b, N)
random_y = np.random.uniform(0, upper_bound, N)

# Визначення кількості точок під кривою
under_curve = random_y < f(random_x)
estimate = (b - a) * upper_bound * np.mean(under_curve)

print(f"Метод Монте-Карло: {estimate}")

# Точне обчислення інтеграла за допомогою quad
result, error = spi.quad(f, a, b)
print(f"Точний інтеграл: {result}")