import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision = 'legacy')

    # Create scatter plot
    fig, axes = plt.subplots(figsize = (11, 7))

    axes.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    through2050 = [1880 + n for n in range(170)]
    through2050 = pd.Series(through2050)

    axes.plot(through2050, res1.intercept + res1.slope * through2050, 'r')

    # Create second line of best fit
    res2 = linregress(df["Year"][120:], df["CSIRO Adjusted Sea Level"][120:])

    from2000 = [2000 + n for n in range(50)]
    from2000 = pd.Series(from2000)

    axes.plot(from2000, res2.intercept + res2.slope * from2000, 'g')

    # Add labels and title
    axes.set_xlabel("Year")
    axes.set_ylabel("Sea Level (inches)")

    axes.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()