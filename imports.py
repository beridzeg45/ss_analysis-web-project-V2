import pandas as pd
import numpy as np

import datetime as dt

import warnings

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash
from dash import dcc,html
from dash.dependencies import Input,Output


pd.options.display.max_columns=100
warnings.filterwarnings('ignore')


app = dash.Dash(__name__)
server=app.server


intro_text="""👋 Welcome to my personal project : Tbilisi Apartment Prices Analysis - Dashboard which provides analtical insights into Tbilisi apartment prices by city part, constraction status and renovation condition. 

The data is scraped from famous Georgian online real estate marketplace using python's BeautifulSoup and Selenium libraries.
The dashboard and graphs are powered by python's dash and plotly libraries.
        
For other projects, feel free to visit my Github account 👀 : https://github.com/beridzeg45"""
