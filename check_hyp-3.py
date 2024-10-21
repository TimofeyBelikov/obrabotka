from scipy.stats import ttest_1samp, wilcoxon

# Гипотеза: математическое ожидание равно 4 для нормального распределения
t_stat_normal, p_value_normal = ttest_1samp(sample_normal, 4)
print(f"T-test for Normal Distribution: t_stat = {t_stat_normal:.4f}, p_value = {p_value_normal:.4f}")

# Гипотеза: математическое ожидание равно 1 для распределения Лапласа
w_stat_laplace, p_value_laplace = wilcoxon(sample_laplace - 1)
print(f"Wilcoxon test for Laplace Distribution: w_stat = {w_stat_laplace:.4f}, p_value = {p_value_laplace:.4f}")

# Проверка гипотезы на уровне значимости 0.05
alpha = 0.05
print("\nHypothesis Testing Results:")
print(f"Normal Distribution: {'Reject' if p_value_normal < alpha else 'Fail to reject'} the null hypothesis")
print(f"Laplace Distribution: {'Reject' if p_value_laplace < alpha else 'Fail to reject'} the null hypothesis")