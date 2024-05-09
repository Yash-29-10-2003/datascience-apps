import streamlit as st

st.set_page_config(
    page_title="Multipage App"
)

st.title("Multiple ML web applications.")
st.sidebar.success("Select a page above.")
st.write("This application has 2 different ML regression models incorporated in it.")

st.header("Models Included:")
st.markdown("""
- **Iris Prediction:** This model predicts the species of iris flowers based on sepal and petal measurements.
- **Penguin Prediction:** This model predicts the species of penguins based on various features like flipper length, bill length, etc.

Feel free to explore each model by selecting the respective page from the sidebar.
""")
#we can use the below code to store session state variables which can be used bw multipole
#if "my_input" not in st.session_state:
#    st.session_state["my_input"] = ""
#
#my_input = st.text_input("Input a text here", st.session_state["my_input"])
#submit = st.button("Submit")
#if submit:
#    st.session_state["my_input"] = my_input
#    st.write("You have entered: ", my_input)