import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import streamlit as st

import pip
pip.main(["install", "openpyxl"])

st.set_page_config(page_title="My Plot", page_icon=None, layout="wide")


grosvenor = pd.read_excel("Plot 10_Grosvenor_July&Aug.xlsx")


new_header = grosvenor.iloc[0] #grab the first row for the header
grosvenor = grosvenor[1:] #take the data less the header row
grosvenor.columns = new_header #set the header row as the df header

st.title("Grosvenor Road - Plot 10")

column_list = grosvenor.columns[2:] # assuming the first 2 columns are not the columns you want to plot

weeks = [g for n, g in grosvenor.groupby(pd.Grouper(key='Date and Time',freq='W'))]

df_0 = weeks[0]
df_1 = weeks[1]
df_2 = weeks[2]
df_3 = weeks[3]
df_4 = weeks[4]

for column in column_list:
    fig, ax = plt.subplots(figsize=(35, 10), dpi=1000)

    # plot data from data frame 1 in the first subplot
    df_0.plot(kind='line', x='Date and Time', y=column, ax=ax, label='Week 1', x_compat=True)

    # plot data from data frame 2 in the second subplot
    df_1.plot(kind='line', x='Date and Time', y=column, ax=ax, label='Week 2', x_compat=True)

    # plot data from data frame 3 in the second subplot
    df_2.plot(kind='line', x='Date and Time', y=column, ax=ax, label='Week 3', x_compat=True)

    # plot data from data frame 4 in the second subplot
    df_3.plot(kind='line', x='Date and Time', y=column, ax=ax, label='Week 4', x_compat=True)

    # plot data from data frame 5 in the second subplot
    df_4.plot(kind='line', x='Date and Time', y=column, ax=ax, label='Week 5', x_compat=True)

    #grosvenor.plot(kind='line', x='Date and Time', y=column, ax=ax, label=column, x_compat=True)
    plt.xlabel('Date and Time of the month - July')
    plt.ylabel(column)

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m.%d.%Y"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    plt.gcf().autofmt_xdate()

    st.subheader(column)
    st.pyplot(fig)
