import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Пример данных
np.random.seed(42)
# group1 = np.random.normal(20, 5, 30)
# group2 = np.random.normal(22, 5, 30)
# group3 = np.random.normal(25, 5, 30)
group1 = np.random.rand(30)
group2 = np.random.rand(30)
group3 = np.random.rand(30)
data = pd.DataFrame({
    'value': np.concatenate([group1, group2, group3]),
    'group': ['group1'] * 30 + ['group2'] * 30 + ['group3'] * 30
})

# One-way ANOVA
model = ols('value ~ group', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("One-way ANOVA results:")
print(anova_table)

# Тест Тьюки
tukey = pairwise_tukeyhsd(endog=data['value'], groups=data['group'], alpha=0.05)
print("\nTukey HSD results:")
print(tukey)

# Визуализация результатов Тьюки
import matplotlib.pyplot as plt

tukey.plot_simultaneous()
plt.xlabel('Mean differences')
plt.title('Tukey HSD Test')
plt.show()