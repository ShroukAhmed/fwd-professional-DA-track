#!/usr/bin/env python
# coding: utf-8

# In[308]:


import time
import pandas as pd
import numpy as np
from IPython.display import display
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
    city_in=''
    while city_in not in CITY_DATA.keys():
        city_in= input('Please specify the city name:').lower()
        
        if city_in not in CITY_DATA.keys():
            print('please enter chicago or new york city or washington as provided on the screen\n')

    # get user input for month (all, january, february, ... , june)
    month_in=''
    month_data={'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    while month_in not in month_data.keys():
        month_in= input('Which month you want to browse - January, February, March, April, May, or June?\n').lower()
        if month_in not in month_data.keys():
            print('Error: Check CapsLock button or any typos, Please Try again \n')
        
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_in=''
    days_of_week=['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    while day_in not in days_of_week:
        day_in=input('Which day you want to browse?\n').lower()
        if day_in not in days_of_week:
            print('Error: Check CapsLock button or any typos, Please Try again \n')
    

    print('-'*40)
    return city_in, month_in, day_in


# In[309]:


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
    
    df = pd.read_csv(CITY_DATA [city])
    df['Start Time'] = pd.to_datetime (df ['Start Time'])
    df['month'] = df ['Start Time'].dt.month       #لو عاوزة اظهر اسم الشهر في الداتافريم استخدم dt.month_name()
    df['Day of Week'] = df ['Start Time'].dt.day_name() 
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
        
    if day != 'all':
        
        df = df[df['Day of Week']== day.title()]
    
    return df

    
#load_data('new york city','june','Monday')


# In[310]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    cmmn_month=df['month'].mode()[0]
    print('common month is: ', cmmn_month)

    # display the most common day of week
    cmmn_day= df['Day of Week'].mode()[0] 
    print('Common Day is: ', cmmn_day)
    
    # display the most common start hour
    cmmn_hr= df['Start Time'].dt.hour.mode()
    print('Common start hour is: ', cmmn_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#time_stats(load_data('new york city','june','monday'))


# In[311]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    cmmn_ststation= df['Start Station'].mode()[0]
    print('Common used start station is: ', cmmn_ststation)
    
    # display most commonly used end station
    cmmn_edstation=df['End Station'].mode()[0]
    print('\n Common used ending station is: ', cmmn_edstation)
    
    # display most frequent combination of start station and end station trip
    df['start to end']= df['Start Station'].str.cat(df['End Station'], sep='  to  ')
    cmmn_fr= df['start to end'].mode()[0]
    
    print('\n most frequent combination of start station and end station is: \n', cmmn_fr)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#station_stats(load_data('new york city','june','monday'))


# In[312]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_TT=df ['Trip Duration'].sum()
    print('total travel time is: ', total_TT)

    # display mean travel time
    avg_time=df ['Trip Duration'].mean()
    print('mean travel time is:', avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#trip_duration_stats(load_data('new york city','june','monday'))


# In[313]:


def user_stats(df,city_in):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    usr_type_count= df['User Type'].value_counts()
    print('counts of user types are:\n', usr_type_count)
    
    # Display counts of gender
    if city_in != 'washington':
        Gender_Count=df['Gender'].value_counts()
        print('\ncounts of genders are:\n', Gender_Count)
    
    # Display earliest, most recent, and most common year of birth
    
        earliest= df['Birth Year'].min()
        print('\n earliest Birth Year is:',earliest)
    
        most_recent= df['Birth Year'].max()
        print('\n most recent Birth Year:',most_recent)
        
        cmmn_birth_year= df['Birth Year'].mode()[0]
        print('\n Most Common Birth Year is:',cmmn_birth_year)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#user_stats(load_data('new york city','june','monday'), 'new york city')


# In[315]:


def raw_data(df,city_in):
    """if the user want to view raw data
    Returns a pandas datafrae
    """
    answer=input(f"Do you want to view the first 5 rows of {city_in}? enter yes or no\n\n").lower()
    #loophere
    start_loc=0
    while (answer!='no'):
        print(df.loc[start_loc:start_loc+4])
        start_loc+=5
        answer=input(f"\nDo you want to see the next 5 rows of {city_in} data?\n").lower()
        if(answer=='no'):
            break
    
#raw_data(load_data('new york city','all','all'),'new york city')


# In[316]:


def main():
    while True:
        city_in, month_in, day_in = get_filters()
        df = load_data(city_in, month_in, day_in)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city_in)
        raw_data(df,city_in)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
#to me: Remember that variables are globally seen by the functions because of the main function
if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




