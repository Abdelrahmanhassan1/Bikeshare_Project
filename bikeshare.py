import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # First Trying to get the city with correct typing:
    # we need to recheck the input till the user inputs a true value using while loop
    # don't forget to use .lower method to avoid capital letters errors
    while True:
        city = input("Which city would you like to explore? \n")
        city = city.lower()
        if city.lower() in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Invalid city, Enter a correct name!')

    # TO DO: get user input for month (all, january, february, ... , june)
    # Like what we did for the city name
    while True:
        month = input("Enter the specific month you want to check? if not enter all to apply no month filter! \n")
        month = month.lower()
        if month.lower() in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print('Invalid Month, Enter a correct name!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Like what we did for the city name

    while True:
        day = input("Enter the specific day you want to check? if not enter all to apply no day filter! \n")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print('Invalid day, Enter a correct name!')

    print('-' * 40)
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

    # Getting the right CSV File according to the user demand
    df = pd.read_csv(CITY_DATA[city])

    # WE need to filter the start time column and get month and day from it and add it like a new column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # Getting the data for the specified month

    if month != 'all':  # if month not = to all then we can filter the data else we will ignore it
        # Like what we did in practice problems
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':  # if day not = to all then we can filter the data else we will ignore it
        # Like what we did in practice problems
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month: {} \n".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("the most common day: {} \n".format(df['day'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("the most common hour: {} \n".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most common start station: {} \n".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("the most common end station: {} \n".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("the most common combination_station:  {} \n".format(df['combination'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time: {} \n".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("The mean travel time: {} \n".format(df['Trip Duration'].mean()))

    print("\n This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df.groupby(['User Type'])['User Type'].count()
    print(user_type)

    # TO DO: Display counts of gender
    # Since the data of washigton doesn't have user type column so we need to check that before displaying the count
    if city != "washington":
        user_gender = df.groupby(['Gender'])['Gender'].count()
        print(user_gender)
    else:
        print("Washigton City data doesn't have gender column")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != "washington":
        # The earliest Year
        earliest_year = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        # The most recent year:
        most_recent_year = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        # The most common year:
        most_common_year = df['Birth Year'].mode()[0]

        print("The earliest year of birth is ", earliest_year, "\n")
        print("The most recent year of birth is ", most_recent_year, "\n")
        print("The most common year of birth is ", most_common_year, "\n")
    else:
        print("Washigton City data doesn't have Date of birth column")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    # After that we will ask the user if he wants to see some more raw data:
    x = 1
    while True:
        answer = input("Would You like to see some more raw data of the specified city? (yes, no)!:")
        if answer.lower() == "yes":
            print(df[x:x + 5])
            x = x + 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
