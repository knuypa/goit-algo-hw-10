import sys
import subprocess

# Перевірка та встановлення пакету PuLP, якщо він не встановлений
try:
    from pulp import LpMaximize, LpProblem, LpVariable
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pulp"])
    from pulp import LpMaximize, LpProblem, LpVariable  # Повторне імпортування після встановлення

# Тепер, коли бібліотека встановлена, продовжуємо з основною частиною програми
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні рішення
x = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
y = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Цільова функція
model += (x + y, "Total_Production")

# Додаємо обмеження
model += (2 * x + y <= 100, "Water_Constraint")
model += (x <= 50, "Sugar_Constraint")
model += (x <= 30, "Lemon_Juice_Constraint")
model += (2 * y <= 40, "Fruit_Puree_Constraint")

# Вирішуємо задачу
model.solve()

# Виведемо результати
print(f"Optimal production of Lemonade: {x.value()}")
print(f"Optimal production of Fruit Juice: {y.value()}")
print(f"Maximum total production: {model.objective.value()}")