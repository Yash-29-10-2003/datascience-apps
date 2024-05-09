import pandas as pd
penguins = pd.read_csv('D:\Coding\datascience\MLmultiPageApp\pages\penguins\penguins_cleaned.csv')

# Ordinal feature encoding
# https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering
df = penguins.copy()
target = 'species'
encode = ['sex','island']

for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]

target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
    return target_mapper[val]

df['species'] = df['species'].apply(target_encode)

# Separating X and y
X = df.drop('species', axis=1)
Y = df['species']

# Building random forest model
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X, Y)

# Specifing absolute path for saving the model
absolute_path = 'D:/Coding/datascience/MLmultiPageApp/pages/penguins/penguinsModel.pkl'

import pickle
# Saving the model
try:
    with open(absolute_path, 'wb') as file:
        pickle.dump(clf, file)
    print("Model saved successfully at:", absolute_path)
except Exception as e:
    print("Error occurred while saving the model:", e)