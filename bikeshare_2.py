import time
import pandas as pd
import numpy as np
import calendar

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
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city not in ["chicago", "new york city", "washington"]:
            print('Please enter the correct city name')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to filter the data by month? E.g. January, February, March, April, May, or June? or All\n').title()
        #month = month.lower()
        if month not in ["January", "February", "March", "April", "May", "June", "All"]:
            print('Please enter the correct month')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Would you like to filter the data by day? E.g. Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All\n').title()
        #day = day.lower()
        if day not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "All"]:
            print('Please enter the correct month')
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    #extract month, day, hour from start time
    df['month'] = pd.to_datetime(df['Start Time']).dt.month_name()
    df['day'] = pd.to_datetime(df['Start Time']).dt.weekday
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour

    #filter the data by month / day (if any)
    if month != 'All':
        df = df[df['month'] == month];

    if day != 'All':
        day_int = list(calendar.day_name).index(day)
        df = df[df['day'] == day_int];

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(most_common_month))

    # display the most common day of week
    most_common_dayofweek = list(calendar.day_name)[df['day'].mode()[0]]
    print('The most common month is (Monday = 0, Sunday = 6): {}'.format(most_common_dayofweek))

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    df['combine station'] = df['Start Station'] + ' / ' + df['End Station']
    most_frequent_combination = df['combine station'].mode()[0]
    print('most frequent combination is: {}'.format(most_frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum() / 60
    print('total travel time is (in minute): {}'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 60
    print('mean travel time is (in minute): {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('counts of user type: \n{}'.format(count_user_type))

    # Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('counts of gender: \n{}'.format(count_gender))
    else:
        print('Error: no gender column')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year_of_birth = df['Birth Year'].min()
        print('earliest year of birth is: {}'.format(earliest_year_of_birth))

        latest_year_of_birth = df['Birth Year'].max()
        print('most recent year of birth is: {}'.format(latest_year_of_birth))

        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('most common year of birth is: {}'.format(most_common_year_of_birth))
    else:
        print('Error: no birth year column')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def load_5_row(df):
    '''load 5 rows / next 5 rows of raw data if user choose to see'''
    location_of_raw_data = 0
    while True:
        load_raw_data = input('\nWould you like to load 5 lines / next 5 lines of raw data? Enter yes or no.\n')
        if load_raw_data.lower() not in ['yes', 'no']:
            print('Please enter correct command.')
        elif load_raw_data.lower() == 'yes':
            display_raw_data = df.iloc[location_of_raw_data : location_of_raw_data + 5]
            location_of_raw_data += 5
            print(display_raw_data)
        elif load_raw_data.lower() == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        pd.set_option('display.max_columns', None)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        load_5_row(df)

        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() not in ['yes', 'no']:
                print('Please enter correct command.')
            elif restart.lower() == 'yes':
                location_of_raw_data = 0
                break
            elif restart.lower() == 'no':
                break

        if restart.lower() == 'no':
            break


if __name__ == "__main__":
	main()
