import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import streamlit as st

import pip
pip.main(["install", "openpyxl"])

st.set_page_config(page_title="My Plot", page_icon=None, layout="wide")


grosvenor = pd.read_excel("grosvenor_plot10.xlsx")
burton = pd.read_excel("burton_plot14.xlsx")

st.title("Burton Plot 14 VS Grosvenor Road - Plot 10")

column_list_grosvenor = grosvenor.columns[2:] # assuming the first 2 columns are not the columns you want to plot
column_list_burton = burton.columns[2:]

for column_G in column_list_grosvenor:

    for column_B in column_list_burton:

        fig, ax = plt.subplots(figsize=(35, 10), dpi=1000)

        # plot data from data frame 1 in the first subplot
        burton.plot(kind='line', x='Date_Time', y=column_B, marker='.', linestyle='', ax=ax, label='Burton Plot 14', color='red', x_compat=True)

        # plot data from data frame 2 in the second subplot
        grosvenor.plot(kind='line', x='Date and Time', y=column_G, marker='.', linestyle='', ax=ax, label='Grosvenor Plot 10', color='green', x_compat=True)

        plt.xlabel('Date and Time of the month - July')
        plt.ylabel(column_B)
        plt.legend()

        ax.xaxis.set_major_formatter(mdates.DateFormatter("%m.%d.%Y"))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
        plt.gcf().autofmt_xdate()

        st.subheader(column)
        st.pyplot(fig)
