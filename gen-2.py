# Генерация выборок
np.random.seed(42)

# Выборка из нормального распределения N(4, 2)
sample_normal = np.random.normal(4, 2, 25)

# Выборка из распределения Лапласа с параметрами (1, 2)
sample_laplace = np.random.laplace(1, 2, 25)

print("Sample from Normal Distribution N(4, 2):")
print(sample_normal)
print("\nSample from Laplace Distribution (1, 2):")
print(sample_laplace)