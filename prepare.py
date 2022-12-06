import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")


#%%
def makedatetime(df):
    '''This Function takes in a time series dataframe and makes the time coulmn a datetime type and sets it as index, as well as adding two new columns for month and day of the week. '''
    df.sale_date = pd.to_datetime(df.sale_date)
    df['month'] = df.sale_date.dt.month
    df['day'] = df.sale_date.dt.day
    # Sort rows by the date and then set the index as that date
    df = df.set_index("sale_date").sort_index()

def plots(df,column):
    plot = df.column
    plot.plot()

def add_sales_total(df):
    df['sales_total'] = df.sale_amount * df.item_price