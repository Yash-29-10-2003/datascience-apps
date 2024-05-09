import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Iris Flower Prediction App

This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

#adding user inputs in the sidebar for prediction
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

#Displaying the users inputs
st.subheader('User Input parameters')
st.write(df)

#Loading the iris dataset
#Classify iris plants into three species in this classic dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target

#Using random forest for predictions
clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

#Creating columns for o/p
col1, col2, col3 = st.columns(3)

# Displaying Class labels
with col1:
    st.subheader('Class labels')
    st.write(iris.target_names)

# Displaying Prediction
with col2:
    st.subheader('Prediction')
    st.write(iris.target_names[prediction])

# Displaying Probabilities
with col3:
    st.subheader('Probabilities')
    st.write(prediction_proba)