import streamlit as st 
import pandas as pd
import base64          #used for managing csv download
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("NBA Stat Explorer")
st.markdown("""
This app performs simple webscraping for NBA stat data.
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

#creating a sidebar in the streamlit webpage
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2024))))

#web scrapping for NBA stats
@st.cache_data    #caching decorator for streamlit , basically makes sure that the data loaded by the function is stored in cache and not reloaded everytime called with same input args
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
    raw = raw.fillna(0)                 #filling empty values with 0
    numeric_cols = ['G', 'PTS', '3P', '3PA', 'FG', 'FGA']
    raw[numeric_cols] = raw[numeric_cols].apply(pd.to_numeric, errors='coerce')
    playerstats = raw.drop(['Rk'], axis=1)        #dropping rk column cuz its useless
    return playerstats
playerstats = load_data(selected_year)

# Sidebar - Team selection
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar - Position selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]  #only showing for teams and positions selected in sidebar
st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')  #updates size of df based on selected teams 
st.dataframe(df_selected_team)

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

#Top 10 Leaderboard
# Sort the DataFrame based on PPG, 3P%, and FG%
top_10_ppg = df_selected_team.sort_values(by='PTS', ascending=False).head(10)
top_10_3p = df_selected_team.sort_values(by='3P', ascending=False).head(10)
top_10_fg = df_selected_team.sort_values(by='FG', ascending=False).head(10)

# Display the leaderboards
st.header('Top 10 Leaderboard')

# Create a columns layout
col1, col2, col3 = st.columns(3)

# Display each leaderboard in a separate column
with col1:
    st.subheader('Points Per Game (PPG)')
    ppg_text = '\n'.join([f"{name}: {score}" for name, score in zip(top_10_ppg['Player'], top_10_ppg['PTS'])])
    st.text(ppg_text)

with col2:
    st.subheader('3-Point Percentage (3P%)')
    p3_text = '\n'.join([f"{name}: {score}" for name, score in zip(top_10_3p['Player'], top_10_3p['3P%'])])
    st.text(p3_text)

with col3:
    st.subheader('Field Goal Percentage (FG%)')
    fg_text = '\n'.join([f"{name}: {score}" for name, score in zip(top_10_fg['Player'], top_10_fg['FG%'])])
    st.text(fg_text)

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    # Excluding non-numeric columns from DataFrame
    non_numeric_columns = df.select_dtypes(exclude=['float64', 'int64']).columns
    numeric_df = df.drop(columns=non_numeric_columns)

    # Calculate correlation for numeric columns
    corr = numeric_df.corr()

    # Create mask for upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(f)