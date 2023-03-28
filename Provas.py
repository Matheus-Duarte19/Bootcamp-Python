import numpy as np
import pandas as pd

"""data = {'Animal': ['cat', 'cat', 'snake', 'dog', 'dog',
                   'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no',
                     'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data=data, index=labels)

print(df.sort_index(by='visits'))"""

y_true = np.array([1., 2., 1.])
y_pred = np.array([1.1, 1.98, 1.05])

print(np.sqrt(((y_true-y_pred)**2).mean()))