import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize = (10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label = 'Datos Observados')


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(1880, 2051)
    line1 = slope * years_extended + intercept
    plt.plot(years_extended, line1, 'r', label='Linea de mejor ajuste (1880-2050)')


    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    year_recent = np.arange(2000, 2051)
    line2 = slope_recent * year_recent + intercept_recent
    plt.plot(year_recent, line2, 'g', label='Linea de mejor ajuste(2000, 2051)')
    


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()