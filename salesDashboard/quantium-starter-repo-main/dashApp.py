from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

sales_data = pd.read_csv('Pink Morsel.csv')

app = Dash(__name__, external_stylesheets=['styles.css'])
app.layout = html.Div(
    style={'background-color': 'black', 
           'height': '100vh', 
           'width' : '100vw' ,
           'font-family': 'monospace' ,
           'display': 'flex', 
           'flex-direction': 'column', 
           'align-items': 'center', 
           'justify-content': 'center'},  
    children=[
        html.H1("Sales Data Visualization", 
                id="sales-header",
                style={'color': '#4f08c2', 
                       'font-size': '44px', 
                       'font-family': 'monospace' ,
                       'margin-bottom': '20px'}),
        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'North', 'value': 'north'}, 
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'}, 
                {'label': 'West', 'value': 'west'}, 
            ],
            value='all',  # Default value
            labelStyle={'display': 'inline-block', 'margin-right': '40px'},
            style={'font-size': '20px', 
                   'font-family': 'monospace' ,
                   'margin-bottom': '14px', 
                   'color': '#4f08c2'}
        ),
        dcc.Graph(
            id='sales-chart',
            style={'width' : '100vw' ,
                   'font-family': 'monospace' }
        )
    ]
)

@app.callback(
    Output('sales-chart', 'figure'),
    [Input('region-radio', 'value')]
)

def update_chart(selected_region):
    #filtering based on region
    if selected_region == 'all':
        sales_fig = px.line(sales_data, 
                            x='Date', 
                            y='Total Sale of Morsel', 
                            title='Total Sales Data')
    else:
        filtered_sales_data = sales_data[sales_data['Region'] == selected_region]
        sales_fig = px.line(filtered_sales_data, 
                            x='Date', 
                            y='Total Sale of Morsel', 
                            title=f'Sales Data for {selected_region.capitalize()} Region')
    
    sales_fig.update_layout(
        plot_bgcolor='black',  # Background color of the plot area
        paper_bgcolor='black',  # Background color of the entire chart including legend and margins
        font=dict(color='#4f08c2', family='monospace' , size=17)
    )
    
    return sales_fig

if __name__ == '__main__':
    app.run_server(debug=True)