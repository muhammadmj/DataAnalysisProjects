import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df.weight / (df.height/100)**2) > 25
df['overweight'] = df['overweight'].map({True: 1, False: 0})

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
normalize = ["cholesterol", "gluc"]
for _ in normalize:
    df[_] = df[_] > 1
    df[_] = df[_].map({True: 1, False: 0})


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ["cardio"], value_vars = ["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.value_counts())
    df_cat.columns = ["total"]
    df_cat = df_cat.groupby(["cardio", "variable", "value"])[["total"]].sum()
    df_cat = df_cat.reset_index()

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x= "variable", y = "total", hue = "value", col = "cardio", data = df_cat, kind = "bar").fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.copy()
    df_heat = df_heat.drop(list(df_heat.loc[df["ap_lo"] > df["ap_hi"]].index))
    df_heat = df_heat.drop(list(df_heat.loc[df["height"] < df["height"].quantile(0.025)].index))
    df_heat = df_heat.drop(list(df_heat.loc[df["height"] > df["height"].quantile(0.975)].index))
    df_heat = df_heat.drop(list(df_heat.loc[df["weight"] < df["weight"].quantile(0.025)].index))
    df_heat = df_heat.drop(list(df_heat.loc[df["weight"] > df["weight"].quantile(0.975)].index))

    # Calculate the correlation matrix
    corr = df_heat.corr()
    corr = round(corr, 1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (11, 10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data = corr, linewidths = .5, center = 0, vmin = -0.16, vmax = 0.32, 
    annot = True, fmt = ".1f", mask = mask, 
    cbar_kws = {"shrink": .5, "ticks": [-0.08, 0.00, 0.08, 0.16, 0.24]}, ax = ax)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
