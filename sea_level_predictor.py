# coded by Ramon Medeiro. Please use this content only to knowledge. Try to do this project yourself.
# FREECODECAMP project 5.


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')

    #original data
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create first line of best fit
    slope1, intercept1, r1, p1, se1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series(j for j in range(1880, 2051))
    y_pred1 = intercept1 + slope1*x_pred1

    # Create second line of best fit
    df_2000 = df.copy()
    df_2000['Year'] >= 2000
    new_df = df_2000[df_2000['Year'] >= 2000]
    x_2000 = new_df['Year']
    y_2000 = new_df['CSIRO Adjusted Sea Level']
    slope2, intercept2, r2, p2, se2 = linregress(x=x_2000, y=y_2000)
    x_pred2 = pd.Series(j for j in range(2000, 2051))
    y_pred2 = intercept2 + slope2*x_pred2


    # Add labels, title and plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], c = 'black', lw = 0.1)
    plt.plot(x_pred1, y_pred1, lw = 2)
    plt.plot(x_pred2, y_pred2, lw = 2)
    plt.title('Rise in Sea Level', fontsize=25)
    plt.xlabel('Year', fontsize = 25)
    plt.xticks(fontsize=20)
    plt.ylabel('Sea Level (inches)', fontsize = 25)
    plt.yticks(fontsize=20)
    plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
