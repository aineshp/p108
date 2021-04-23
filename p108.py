import statistics
import random
import csv
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
data1=pd.read_csv('data.csv')
listavg=data1['Avg Rating'].tolist()
fig=ff.create_distplot([listavg],['Average ratings'])
fig.show()