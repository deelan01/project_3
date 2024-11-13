from dash import Dash, html, dcc
import pandas as pd
import geopandas as gpd
import plotly.express as px
from sqlalchemy import URL, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# CONNECTION TO THE ENGINE OF THE DATABASE

connection = URL.create(
  'postgresql',
  username=os.getenv("USER"),
  password=os.getenv("PASSWORD"),
  host=os.getenv("HOST"),
  database=os.getenv("DATABASE")
)

engine = create_engine(connection)

#into a dataframe
with engine.connect() as connection:
    data = pd.read_sql("SELECT * FROM earthquake",connection)
    df = pd.DataFrame(data)
# #APP SETUP
app = Dash(__name__)
equation = pd.to_numeric(df['mag'])
fig = px.scatter_mapbox(df,
                        lat='lat',
                        lon='long',
                        size= equation + 100,
                        hover_name='place',
                        hover_data='time_',
                        color='mag_type',
                        color_discrete_sequence=px.colors.qualitative.Bold,
                        mapbox_style='open-street-map',
                        zoom=1,
                        width=1600,
                        height=1000)



#legend traces
fig.update_traces(name='body_wave', selector=dict(name='mb'))
fig.update_traces(name='moment_w-phase(based_on_scale 5 or greater at 0<90 degrees)', selector=dict(name='mww'))
fig.update_traces(name='moment_regional', selector=dict(name='mwr'))
fig.update_traces(name='centroid_type', selector=dict(name='mwc'))
fig.update_traces(name='long_period_time', selector=dict(name='mwb'))
fig.update_traces(name='measurment_by_quntitative_moment_based(quake by the moment)', selector=dict(name='mw'))
fig.update_traces(name='mag_scale_by_local', selector=dict(name='ml'))
# app init
app.layout = html.Div([
    html.Thead([
        html.Title('Earthquake Data')
    ]),
    html.H1('Earthquake Data for the Year 2015'),
        dcc.Graph(figure=fig)])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)