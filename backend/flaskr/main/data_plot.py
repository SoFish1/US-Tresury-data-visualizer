# Using plotly.express
import plotly.express as px
from .build_query import build_query
import pandas as pd
from plotly.utils import PlotlyJSONEncoder
from json import dumps
from datetime import date,timedelta


def build_plot(field,time_opt,tag,since_year=2):
    
    dataframe=build_query(fieldname=field,since_year=since_year,time_opt=time_opt, tag=tag)

    range_x = [(date.today() - timedelta(days=since_year*365)).isoformat(), date.today().isoformat() ]

    if time_opt == "":
        fig = px.bar(dataframe, x='_time', y="_value", range_x=range_x, labels=dict(_time="Time",_value=field))
    if time_opt == "y":
        fig = px.bar(dataframe, x='_time', y="_value" , range_x=range_x, labels=dict(_time="Time", _value="Cumulated "+field))    
    return dumps(fig, cls=PlotlyJSONEncoder)


# fig = px.line(data_frame, x='_time', y='Total Withdrawals (excluding transfers)', range_x=['2020-07-01','2021-12-31'])

# graphJSON = dumps(fig, cls=PlotlyJSONEncoder)
