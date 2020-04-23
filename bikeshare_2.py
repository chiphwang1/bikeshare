import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = " "
    city_list = ["chicago","new york city", "washington"]
    while city not in city_list:
        print(city_list)
        city = input(" Enter city to Analyze: ").lower()


    # get user input for month (all, january, february, ... , june)
    month_list = ['january','february','march','april','may','june','all']
    month =" "
    while month not in month_list:
        print(month_list)
        month = input(" Enter month to Analyze: ").lower()



    # get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ['monday','tuesday','wednesday','thursday','friday','saturday',
                'sunday',
                 'all']
    day = " "
    while day not in days_list:
        print(days_list)
        day = input(" Enter day to Analyze: ").lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):


    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek



    # filter by month if applicable
    if month != 'all':
    # use the index of the months list to get the corresponding int
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1

    # filter by month to create the new dataframe
       df = df[df['month'] == month]

    # filter by day of week if applicable
       if day != 'all':
    # filter by day of week to create the new dataframe
          days = ['monday','tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']
          day = days.index(day) + 1
          df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)


    # display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of the week:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['day_of_week'].mode()[0]
    print('Most Common hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    common_start_staion = df['Start Station'].mode()[0]
    print('Most start station:', common_start_staion)


    # display most commonly used end station

    common_stop_staion = df['End Station'].mode()[0]
    print('Most stop station:', common_stop_staion)



    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'].str.cat(df['End Station'],sep=" ")
    popular_trip =  df['trip'].mode()[0]
    print('Most stop station:', popular_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('User Types: ', user_types)

    # Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('Gender Types:\n', gender_types)
    except Exception as e:
        print("No Gender Values in Data")


   # Display earliest, most recent, and most common year of
    try:
        Earliest_Year = df['Birth Year'].min()
        Most_Recent_Year = df['Birth Year'].max()
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()

        print("Earliest_Year: ", int(Earliest_Year))
        print("Most_Recent_Year: ",int(Most_Recent_Year))
        print("Most_Common_Year ", int(Most_Common_Year))
    except Exception as e:
        print("No Birth year Values in Data")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):
    answer = " "
    counter = 0
    while answer != 'n':
        answer = input("Would you like to see the another 5 lines of raw data?  Enter y for yes or n for no: ").lower()
        if answer == "y":
            print(df.iloc[counter:counter + 10])
            counter = counter + 10



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
