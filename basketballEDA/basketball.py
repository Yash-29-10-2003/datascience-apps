import streamlit as st 
import pandas as pd
import base64          #used for managing csv download
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("NBA Stat Explorer")
st.write("***")
st.markdown("""
This app performs simple webscraping for NBA stat data.
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")
st.write("***")
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
    raw = raw.fillna(0)                      #filling empty values with 0
    numeric_cols = ['Age','G', 'PTS', '3P', '3PA', 'FG', 'FGA','AST','STL','TRB','TOV','BLK','FTA']         #making sure numeric colums have numeric vals
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
st.header('Player Stats :')
st.write('Data Dimensions: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')  #updates size of df based on selected teams 
st.dataframe(df_selected_team)

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

st.write("***")

#Top 10 Leaderboard
# Sorting the DataFrame based on PPG, 3P%, and FG%
top_10_ppg = df_selected_team.sort_values(by='PTS', ascending=False).head(10)
top_10_3p = df_selected_team.sort_values(by='3P', ascending=False).head(10)
top_10_fg = df_selected_team.sort_values(by='FG', ascending=False).head(10)

# Displaying the leaderboards
st.header('Top 10 Leaderboard')

# Columns layout
col1, col2, col3 = st.columns(3)

# Displaying each leaderboard in a separate column
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

st.write("***")

#Attribute based scatters
st.header('Attribute based scatters :')
selected_option = st.selectbox(
    'Select an attribute to get the scatter of :',
    ('Points','Assists','Steals','Rebounds','Turnovers','Blocks','Free-Throw Attempts')
)
#ppg scatter
if selected_option == "Points":
    st.markdown('### PPG Scatter (15+)')
    plt.figure(figsize=(10, 6))
    
    # Filtering the DataFrame to include only players with points above 15
    df_filtered = df_selected_team[df_selected_team['PTS'] > 15]
    plt.scatter(df_filtered.index, df_filtered['PTS'], color='red', alpha=0.5)  # Index represents player, PTS represents points
    plt.title('15+ Points Scatter')
    plt.xlabel('Player Index')
    plt.ylabel('Points')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

#assist scatter
if selected_option == "Assists":
    st.markdown('### AST Scatter (15+)')
    plt.figure(figsize=(10, 6))
    
    # Filtering the DataFrame to include only players with assists above 5
    df_filtered = df_selected_team[df_selected_team['AST'] > 5]
    plt.scatter(df_filtered.index, df_filtered['AST'], color='red', alpha=0.5) 
    plt.title('5+ Assist Scatter')
    plt.xlabel('Player Index')
    plt.ylabel('Assists')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

#steals scatter
if selected_option == "Steals":
    st.markdown('### STL Scatter (1.1+)')
    plt.figure(figsize=(10, 6))
    
    # Filtering the DataFrame to include only players with steals above 1.1
    df_filtered = df_selected_team[df_selected_team['STL'] > 1.1]
    plt.scatter(df_filtered.index, df_filtered['STL'], color='red', alpha=0.5) 
    plt.title('1.1+ Steals Scatter')
    plt.xlabel('Player Index')
    plt.ylabel('Steals')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

#rebounds scatter
if selected_option == "Rebounds":
    st.markdown('### Rebounds Scatter (8+)')
    plt.figure(figsize=(10, 6))
    
    # Filtering the DataFrame to include only players with over 8 rebounds
    df_filtered = df_selected_team[df_selected_team['TRB'] > 8.0]
    plt.scatter(df_filtered.index, df_filtered['TRB'], color='red', alpha=0.5) 
    plt.title('8+ Rebounds Scatter')
    plt.xlabel('Player Index')
    plt.ylabel('Rebounds')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

#turnovers scatter
if selected_option == "Turnovers":
    st.markdown('### Turnovers Scatter (2.5+)')
    plt.figure(figsize=(10, 6))
    
    # Filtering the DataFrame to include only players with over 2.5+ turnovers
    df_filtered = df_selected_team[df_selected_team['TOV'] > 2.5]
    plt.scatter(df_filtered.index, df_filtered['TOV'], color='red', alpha=0.5) 
    plt.title('2.5+ Turnovers Scatter')
    plt.xlabel('Player Index')
    plt.ylabel('Turnovers')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

#blocks scatter
if selected_option == "Blocks":
    st.markdown('### Blocks Scatter (1.1+)')
    plt.figure(figsize=(10, 6))
    
    # Filtering the DataFrame to include only players with 1.1+ blocks
    df_filtered = df_selected_team[df_selected_team['BLK'] > 1.1]
    plt.scatter(df_filtered.index, df_filtered['BLK'], color='red', alpha=0.5) 
    plt.title('1.1+ Blocks Scatter')
    plt.xlabel('Player Index')
    plt.ylabel('Blocks')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

#FTA scatter
if selected_option == "Free-Throw Attempts":
    st.markdown('### Free-Throw Attempts (5+)')
    plt.figure(figsize=(10, 6))
    
    # Filtering the DataFrame to include only players with 5+ freethrow attempts
    df_filtered = df_selected_team[df_selected_team['FTA'] > 5]
    plt.scatter(df_filtered.index, df_filtered['FTA'], color='red', alpha=0.5) 
    plt.title('5+ Free-Throw Attempts')
    plt.xlabel('Player Index')
    plt.ylabel('Free-Throw Attempts')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("***")

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Heatmap Matrix ')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    # Excluding non-numeric columns from DataFrame
    non_numeric_columns = df.select_dtypes(exclude=['float64', 'int64']).columns
    numeric_df = df.drop(columns=non_numeric_columns)

    # Calculating correlation for numeric columns
    corr = numeric_df.corr()

    # Creating mask for upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(f)