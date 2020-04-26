# SARIMAX example
from statsmodels.tsa.statespace.sarimax import SARIMAX
from math import sin
from random import random
#import csv
import pandas as pd

import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')

def loadSourceData():
    df = pd.read_csv('GlobalLandTemperaturesByState.csv', sep=",") #change file to filepath
    output = df[(df.Country == 'United States')  & (df['dt'] > '1976-07-04') ]
    
    ds = output.groupby('Country')['Country']
    print(ds)

    return ()

def climateFit():
    # SARIMA example
    # contrived dataset
    #data = [x + random() for x in range(2, 100)]
    data = loadSourceData()['AverageTemperature']
    #print(data)
    # fit model
    model = SARIMAX(data, order=(1, 0, 0), seasonal_order=(2, 1, 0, 12))
    model_fit = model.fit(disp=True)
    # make prediction
    yhat = model_fit.predict(len(data), len(data))
    print(yhat)
    print(model_fit.aic)
    # model_fit.plot_diagnostics(figsize=(18, 8))
    # plt.show()
    # Arima_model=auto_arima(train, start_p=1, start_q=1, max_p=8, max_q=8, start_P=0, start_Q=0, max_P=8, max_Q=8, m=12, seasonal=True, trace=True, d=1, D=1, error_action='warn', suppress_warnings=True, random_state = 20, n_fits=30)
    # Arima_model.summary()
def sampleFit():
    # SARIMA example
    from statsmodels.tsa.statespace.sarimax import SARIMAX
    from math import sin
    from random import random
    # contrived dataset
    data = [x + random() for x in range(1, 100)]
    # fit model
    model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 1))
    model_fit = model.fit(disp=False)
    # make prediction
    yhat = model_fit.predict(len(data), len(data))
    print(yhat)

if __name__ == "__main__":
    # execute only if run as a script
    loadSourceData()
    #climateFit()
    