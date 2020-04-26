
# coding: utf-8

# In[103]:


import pandas as pd

# Download data for USA
df_state = pd.read_csv("D:/GlobalLandTemperaturesByState.csv")
df_state = df_state[(df_state.Country == 'United States')]

# Clean data: delete NaN and adjust names where required
df_state = df_state.dropna()
df_state.loc[df_state['State'] == "Georgia (State)", ['State']] = "Georgia"
df_state.loc[df_state['State'] == "District Of Columbia", ['State']] = "District of Columbia"

# Take only Date, State and Average Temperature
df_state = df_state.drop(columns=['Country', 'AverageTemperatureUncertainty'])

# Splite the whole period into 2 parts: last 10 years and the rest
df_state_last10 = df_state[(df_state.dt >= '2010.01.01')]
df_state_all_wo_last10 = df_state[(df_state.dt < '2010.01.01')]

# Find the average temperature grouped by a state
df_state_last10 = df_state_last10.groupby('State').mean()
df_state_all_wo_last10 = df_state_all_wo_last10.groupby('State').mean()

# Unite 2 data frames
df = pd.concat([df_state_last10, df_state_all_wo_last10], axis=1)
df.columns  = ['AverageTemperatureLast10','AverageTemperatureWoLast10']

# Find the difference
df['Delta'] = df['AverageTemperatureLast10'] - df['AverageTemperatureWoLast10']
df = df.round(2)

df.to_csv("D:/Delta10All.csv")

# df_state_last10.index.tolist()



