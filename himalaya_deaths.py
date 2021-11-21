#!/usr/bin/env python3
'''
DataTas Plot-A-Thon!
File: himalaya_deaths.py
@author: Simon C Stanton
Date: 21/11/2021

'''

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from collections import defaultdict


members=pd.read_csv('data/members.csv')

'''
    !! Python 3.6+ (for ordered dict funtionality !!
    
    Only using members dataset
    For each year, get the number of deaths 
        - total
        - on everest
        - hired
        - on everest and hired
    
    Plot as cumulative count of deaths
    Do a rough plot here.
    Write new dataset to import to R.
    
'''




'''
    Deaths
        - extract rows with a record of death
        - filter out columns we don;t need / keep columns we need
        - remove rows that have missing values (if any)
        - sort rows into year order
        
'''

deaths = members[members['died'] == True]
deaths = deaths[['peak_name', 'year', 'hired']]
deaths.dropna(inplace=True)
deaths.sort_values(by=['year'], ascending=True, inplace=True)



'''
    Create list of all years in range (is same for injuroes and deaths - 1905 - 2019)
    
'''
all_years = [*range(deaths.iloc[0]['year'], deaths.iloc[len(deaths)-1]['year']+1)]







'''
    Deaths
        
'''

# Note dict are ordered in 3.6+
total_death_count_over_years = defaultdict(int)
total_death_count_over_years_everest = defaultdict(int)
total_death_count_over_years_hired = defaultdict(int)
total_death_count_over_years_hired_everest = defaultdict(int)

total_deaths_accum = 0
total_deaths_everest_accum = 0
total_deaths_hired_accum = 0

for index, row in deaths.iterrows():
    
    total_death_count_over_years[row['year']] += 1

    if row['peak_name'] == "Everest":
        total_death_count_over_years_everest[row['year']] += 1
        
    if row['hired'] == True:
        total_death_count_over_years_hired[row['year']] += 1
        
    if row['hired'] == True and row['peak_name'] == "Everest":
        total_death_count_over_years_hired_everest[row['year']] += 1        


# make accumulators

total_deaths_accum = [0] * len(all_years)
total_deaths_everest_accum = [0] * len(all_years)
total_deaths_hired_accum = [0] * len(all_years)
total_deaths_hired_everest_accum = [0] * len(all_years)

t = u = v = w = 0
for i, j in enumerate(all_years):
    t += total_death_count_over_years[j]
    total_deaths_accum[i] = t
    
    u += total_death_count_over_years_everest[j]
    total_deaths_everest_accum[i] = u
    
    v += total_death_count_over_years_hired[j]
    total_deaths_hired_accum[i] = v
    
    w += total_death_count_over_years_hired_everest[j]
    total_deaths_hired_everest_accum[i] = w
    



fig = go.Figure()
fig.add_trace(go.Scatter(x=all_years, y=total_deaths_accum, name='Total Deaths', line=dict(color='firebrick', width=2)))
fig.add_trace(go.Scatter(x=all_years, y=total_deaths_everest_accum, name='On Everest', line=dict(color='yellow', width=2)))
fig.add_trace(go.Scatter(x=all_years, y=total_deaths_hired_accum, name='Hired', line=dict(color='blue', width=2)))
fig.add_trace(go.Scatter(x=all_years, y=total_deaths_hired_everest_accum, name='Hired on Everest', line=dict(color='green', width=2)))

fig.update_layout(title='Deaths in the Himalayas',
                   xaxis_title='Year',
                   yaxis_title='Death Count')


fig.show()

'''
    write to file
'''

deaths_data = pd.DataFrame(
    {
        'years': all_years,
        'total_deaths_accum': total_deaths_accum,
        'total_deaths_everest_accum': total_deaths_everest_accum, 
        'total_deaths_hired_accum': total_deaths_hired_accum, 
        'total_deaths_hired_everest_accum': total_deaths_hired_everest_accum
    }, index=all_years
)
file = "deaths.csv"
deaths_data.to_csv(file, encoding='utf-8', index=True)
    
