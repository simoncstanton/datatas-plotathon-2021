#!/usr/bin/env python3
'''
DataTas Plot-A-Thon!
File: himalaya_deaths_heatmap.py
@author: Simon C Stanton
Date: 21/11/2021

'''
import numpy as np
import pandas as pd
import plotly.graph_objects as go

members=pd.read_csv('data/members.csv')

'''
    Heatmap of deaths in the Himalayas
    Peak by Season
    
    Only using members dataset
    - extract records of died
    - filter out all cols except peak_name and season
    - drop records with missing values (if any)
    
    - iterate and count
    - plotly heatmap
    
'''

deaths = members[members['died'] == True]
deaths = deaths[['peak_name', 'season']]
deaths.dropna(inplace=True)

x_values = deaths.peak_name.unique()
x_values.sort()

'''
    Can programmatically obtain seasons:
        y_values = deaths.season.unique()
    or, just build with desired sort to begin with...
'''
y_values = np.array(["Winter", "Spring", "Summer", "Autumn"]) 

'''
    Create matrix of peaks x seasons
'''
deaths_z = [[0] * len(x_values) for i in range(len(y_values))]

'''
    iterate over recordset and accumulate counts for each cell in matrix
'''

for index, row in deaths.iterrows():
    x = np.where(x_values == row['peak_name'])[0]
    y = np.where(y_values == row['season'])[0]
    deaths_z[int(y)][int(x)] += 1
    
'''
    Build a plotly heatmap
'''
fig = go.Figure(data=go.Heatmap(
    z=deaths_z, x=x_values, y=y_values,
    colorscale=[[0.0, "rgb(49,54,149)"],
                [0.025, "rgb(69,117,180)"],
                [0.05, "rgb(116,173,209)"],
                [0.1, "rgb(171,217,233)"],
                [0.2, "rgb(224,243,248)"],
                [0.3, "rgb(254,224,144)"],
                [0.5, "rgb(253,174,97)"],
                [0.7, "rgb(244,109,67)"],
                [0.8, "rgb(215,48,39)"],
                [1.0, "rgb(165,0,38)"]],
    ))
    
fig.update_layout(
    title="Deaths by Season and Peak in the Himalayas (1905-2019)",
    xaxis_title="Peak",
    yaxis_title="Season",
    legend_title="Deaths",
    font=dict(
        family="Arial",
        size=12,
        color="RebeccaPurple"
    )
)
fig.show()


exit()




