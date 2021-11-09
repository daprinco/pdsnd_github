import time
import pandas as pd
import numpy as np

city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_data = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

day_of_week= ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']
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
        try:
            city = input("\n Please enter name of city: chicago, new york city or washington\n").lower()
            if city not in city_data:
                print("Please enter correct name of city")
            else:
                break
        except:
            print('\nERROR: you entered wrong city name')

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("\n Please enter a month e.g january,february, ... , june or enter 'all' to display results for all months' \n").lower()
            if month not in months_data:
                print("Please enter the correct month i.e january,february, ... , june or 'all' ")
            else:
                break
        except:
            print('\nERROR: you entered a wrong month')

    month = months_data.index(month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("\n Please enter day of week e.g monday,tuesday, ... , sunday or enter 'all' to apply no filter ' \n").lower()
            if day not in day_of_week:
                print("Please enter the correct day i.e monday,tuesday, ... ,sunday or 'all' ")
            else:
                break
        except:
            print('\nERROR: you entered a wrong day')

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
    # read appropriate csv file into a dataframe
    df = pd.read_csv(city_data[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # create new columns for month, hour and day of week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 0:
        # slice original dataframe using selected month to create  new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month from the given fitered data is: " + months_data[common_month].title())

    # display the most common day of week
    common_day= df['day'].mode()[0]
    print("The most common day of week from the given fitered data is: " + common_day)

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour from the given fitered data is hour: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + common_end_station)

    # display most frequent combination of start station and end station trip
    frequent_trip = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_trip.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))

    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types is: \n" + str(user_types))

    # Display counts of gender
    if city_data[city] == 'chicago.csv' or city_data[city] == 'new_york_city.csv':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender is: \n" + str(gender))

        # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth from the given data is: {}\n'.format(earliest_birth))
        print('Most recent birth from the given data is: {}\n'.format(most_recent_birth))
        print('Most common birth from the given data is: {}\n'.format(most_common_birth) )




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display(df):
    """Displays subsequent raw data according to user request.
    Args:
        (DataFrame) df - filtered  DataFrame
    """
    print(df.head())
    next = 0
    while True:
        view_data = input('\nWould you like to view next five row of raw data? Enter yes or no \n').lower()
        if view_data != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            try:

                view_data = input('\nWould you like to disply first 5 rows of  data? Enter yes or no\n').lower()
                if view_data != 'yes':
                    break
                display(df)
                break
            except:
                print('\nWrong entry, Enter yes or no\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
