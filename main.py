import random

# 1
print(''.join(random.choice('0123456789') for _ in range(6)))

# 2
import math
son = random.randint(1, 10)
print(son, "! =", math.factorial(son))

# 3
matn = "Python"
print(random.choice(matn))

# 4
son = random.randint(0, 50)
print(son, "→ 7 ga bo'linadi" if son % 7 == 0 else "→ bo'linmaydi")

# 5
natija = random.randint(1, 4)
print("jackpot!!! 🎉" if natija == 1 else "oddiy sovrin 😊")
print("Chiqqan son:", natija)
