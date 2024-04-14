import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    fig,ax = plt.subplots(figsize=(12,12))
    ax = plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    X1 = df["Year"]
    Y1 = df["CSIRO Adjusted Sea Level"]
    fit1 = linregress(x=X1, y=Y1)
    x_plot = pd.Series([i for i in range(1880, 2051)])
    y_pred1 = fit1.intercept + fit1.slope * x_plot
    plt.plot(x_plot, y_pred1, color="red")

    # Create second line of best fit
    X2 = df["Year"][df["Year"] >= 2000]
    Y2 = df["CSIRO Adjusted Sea Level"][df["Year"] >= 2000]
    fit2 = linregress(x=X2, y=Y2)
    new_x_plot = pd.Series([j for j in range(2000, 2051)])
    y_pred2 = fit2.intercept + fit2.slope * new_x_plot
    plt.plot(new_x_plot, y_pred2, color="yellow")
    # Add labels and title
    plt.xticks(
        [1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]
    )
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()



