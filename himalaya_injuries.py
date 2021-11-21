#!/usr/bin/env python3
'''
DataTas Plot-A-Thon!
File: himalaya_injuries.py
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
    For each year, get the number of of injuries:
        - total
        - on everest
        - hired
        - on everest and hired
    
    Plot as cumulative count of injuries
    Do a rough plot here.
    Write new dataset to import to R.
    
'''




'''
    Injuries
        - extract rows with a record of injury
        - filter out columns we don't need / keep columns we need
        - remove rows that have missing values (if any)
        - sort rows into year order
        
'''
injuries = members[members['injured'] == True]
injuries = injuries[['peak_name', 'year', 'hired']]
injuries.dropna(inplace=True)
injuries.sort_values(by=['year'], ascending=True, inplace=True)

'''
    Create list of all years in range 
    
'''
all_years = [*range(injuries.iloc[0]['year'], injuries.iloc[len(injuries)-1]['year']+1)]



    

'''
    Injuries
        
        
'''


total_injured_count_over_years = defaultdict(int)
total_injured_count_over_years_everest = defaultdict(int)
total_injured_count_over_years_hired = defaultdict(int)
total_injured_count_over_years_hired_everest = defaultdict(int)

total_injured_accum = 0
total_injured_everest_accum = 0
total_injured_hired_accum = 0

for index, row in injuries.iterrows():
    
    total_injured_count_over_years[row['year']] += 1

    if row['peak_name'] == "Everest":
        total_injured_count_over_years_everest[row['year']] += 1
        
    if row['hired'] == True:
        total_injured_count_over_years_hired[row['year']] += 1
        
    if row['hired'] == True and row['peak_name'] == "Everest":
        total_injured_count_over_years_hired_everest[row['year']] += 1  
        
total_injured_accum = [0] * len(all_years)
total_injured_everest_accum = [0] * len(all_years)
total_injured_hired_accum = [0] * len(all_years)
total_injured_hired_everest_accum = [0] * len(all_years)

t = u = v = w = 0
for i, j in enumerate(all_years):
    t += total_injured_count_over_years[j]
    total_injured_accum[i] = t
    
    u += total_injured_count_over_years_everest[j]
    total_injured_everest_accum[i] = u
    
    v += total_injured_count_over_years_hired[j]
    total_injured_hired_accum[i] = v
    
    w += total_injured_count_over_years_hired_everest[j]
    total_injured_hired_everest_accum[i] = w
    







fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=all_years, y=total_injured_accum, name='Total Injuries', line=dict(color='firebrick', width=2)))
fig2.add_trace(go.Scatter(x=all_years, y=total_injured_everest_accum, name='On Everest', line=dict(color='yellow', width=2)))
fig2.add_trace(go.Scatter(x=all_years, y=total_injured_hired_accum, name='Hired', line=dict(color='blue', width=2)))
fig2.add_trace(go.Scatter(x=all_years, y=total_injured_hired_everest_accum, name='Hired on Everest', line=dict(color='green', width=2)))

fig2.update_layout(title='Injuries in the Himalayas',
                   xaxis_title='Year',
                   yaxis_title='Death Count')


fig2.show()


'''
    write to file
'''

injuries_data = pd.DataFrame(
    {
        'years': all_years,
        'total_injured_accum': total_injured_accum,
        'total_injured_everest_accum': total_injured_everest_accum, 
        'total_injured_hired_accum': total_injured_hired_accum, 
        'total_injured_hired_everest_accum': total_injured_hired_everest_accum
    }, index=all_years
)
file = "injuries.csv"
injuries_data.to_csv(file, encoding='utf-8', index=True)

