import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = "date", parse_dates = True)

# Clean data
df_sorted = df.sort_values("value")
two_point_five = round(len(df_sorted)*(1/40))
top2point5_index = (df_sorted.head(two_point_five)).index
bottom2point5_index = (df_sorted.tail(two_point_five)).index
df = df.drop(top2point5_index)
df = df.drop(bottom2point5_index)


def draw_line_plot():
    # Draw line plot
    fig, axes = plt.subplots(figsize = (18, 6))
    
    axes.plot(df.index, df.value, color = 'red')
    
    axes.set_xlabel("Date")
    axes.set_ylabel("Page Views")
    
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace = True)
    df_bar['Years'], df_bar['Months'] = df_bar['date'].dt.year, df_bar['date'].dt.month
    df_bar.sort_values('Months', inplace = True)
    df_bar = pd.DataFrame(df_bar.groupby(['Years', 'Months']).value.mean())
    df_bar.rename(columns = {'value': 'AveragePageViews'}, inplace = True)
    df_bar = df_bar.AveragePageViews
    df_bar = df_bar.unstack()
    col = ["January", "February", "March", "April", "May", "June", 
       "July", "August", "September", "October", "November", "December"]
    df_bar.columns = col
    df_bar.columns.rename('Months', inplace = True)

    # Draw bar plot
    fig, ax = plt.subplots()
    
    df_bar.plot(kind = 'bar', figsize = (9, 9), ax = ax)
    
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    
    ax.legend()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df_box_sorted = df_box.copy()
    df_box_sorted['month'] = [d.month for d in df_box_sorted.date]
    df_box_sorted.sort_values(by = 'month', inplace = True)
    df_box_sorted['month'] = [d.strftime('%b') for d in df_box_sorted.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize = (30, 10))

    sns.set_style("whitegrid") 
    sns.boxplot(x = "year", y = 'value', data = df_box, ax = axes[0])
    sns.boxplot(x = "month", y = 'value', data = df_box_sorted, ax = axes[1])

    axes[0].grid(False)
    axes[1].grid(False)

    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
