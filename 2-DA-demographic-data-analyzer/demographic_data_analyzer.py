import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = round((df.age.loc[df.sex == "Male"]).mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df.education == "Bachelors").sum() / len(df) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df.loc[(df.education == "Bachelors") | (df.education == "Masters") | (df.education == "Doctorate")])
    lower_education = len(df) - higher_education

    # percentage with salary >50K
    higher_education_rich = round(len(df.loc[((df.education == "Bachelors") | (df.education == "Masters") | (df.education == "Doctorate")) &
       (df.salary == ">50K")]) / higher_education * 100, 1)
    lower_education_rich = round((len(df.loc[((df.education != "Bachelors") & (df.education != "Masters") & (df.education != "Doctorate")) &
       (df.salary == ">50K")])) / lower_education * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df.loc[df["hours-per-week"] == df["hours-per-week"].min()])

    rich_percentage = int(round(len(df.loc[(df["hours-per-week"] == df["hours-per-week"].min()) & (df.salary == ">50K")]) / num_min_workers * 100, 1))

    # What country has the highest percentage of people that earn >50K?
    all_country = pd.DataFrame(df["native-country"].value_counts())
    rich_country = pd.DataFrame(df["native-country"].loc[df.salary == ">50K"].value_counts())
    rich_country_percentage = rich_country / all_country.loc[rich_country.index]
    highest_earning_country = rich_country_percentage.loc[rich_country_percentage["native-country"] == rich_country_percentage.max().values[0]]

    highest_earning_country = highest_earning_country.index[0]
    highest_earning_country_percentage = round(rich_country_percentage.max().values[0] * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    occupation_in_india = pd.DataFrame((df["occupation"].loc[(df.salary == ">50K") & (df["native-country"] == "India")]).value_counts())
    occupation_in_india.columns = ["Total"]
    top_IN_occupation = occupation_in_india.loc[occupation_in_india["Total"] == occupation_in_india.max().values[0]]

    
    top_IN_occupation = top_IN_occupation.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
