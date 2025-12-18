import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_day_int():
    """Gets the day filter as an integer (Style 1), mapping 1-7 to full day names."""
    day_map = {1: 'sunday', 2: 'monday', 3: 'tuesday', 4: 'wednesday', 5: 'thursday', 6: 'friday', 7: 'saturday'}
    
    while True:
        day_input = input("Which day? Please type your response as an integer (1=Sunday to 7=Saturday, or 0 for All): ")
        try:
            day_int = int(day_input)
            if day_int == 0:
                return 'all'
            elif 1 <= day_int <= 7:
                return day_map[day_int]
            else:
                print("Invalid integer. Please enter a number from 1 to 7, or 0 for All.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_day_abbr():
    """Gets the day filter as an abbreviation (Style 2), mapping to full day names."""
    abbr_map = {'m': 'monday', 'tu': 'tuesday', 'w': 'wednesday', 'th': 'thursday', 'f': 'friday', 'sa': 'saturday', 'su': 'sunday', 'all': 'all'}
    
    while True:
        day_input = input("Which day? Please type a day M, Tu, W, Th, F, Sa, Su. ").lower()
        if day_input in abbr_map:
            return abbr_map[day_input]
        else:
            print("Invalid abbreviation. Please use M, Tu, W, Th, F, Sa, Su, or type 'all'.")


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze, with custom prompts and error handling.

    Returns:
        (str) city - name of the city to analyze ('chicago', 'new york city', or 'washington')
        (str) month - name of the month to filter by, or "all"
        (str) day - name of the day of week to filter by, or "all"
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
  
    while True:
       
        city_input = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        
       
        if city_input == 'new york' or city_input == 'new york city':
            city = 'new york city'
            break
        elif city_input in CITY_DATA:
            city = city_input
            break
        else:
            print("Invalid input. Please choose from: Chicago, New York City, or Washington.")
            
    print(f"Looks like you want to hear about {city.title()}! If this is not true, restart the program now!\n")
            
   
    filter_options = ['month', 'day', 'both', 'none']
    while True:
        filter_type = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter. ').lower()
        if filter_type in filter_options:
            if filter_type != 'none':
                 print(f"We will make sure to filter by {filter_type}!")
            break
        else:
            print("Invalid filter choice. Please enter 'month', 'day', 'both', or 'none'.")

    month = 'all'
    day = 'all'
    
   
    if filter_type in ['month', 'both']:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        while True:
            month = input("Which month? January, February, March, April, May, or June? Please type out the full month name. ").lower()
            if month in months:
                break
            else:
                print("Invalid month. Please choose from: January through June.")

   
    if filter_type in ['day', 'both']:
        
        if city == 'chicago' and filter_type == 'day':
            day = get_day_abbr()
        else:
            day = get_day_int() 
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    print("\nJust one moment... loading the data")
    
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour
    
  
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_index = months.index(month) + 1 
        df = df[df['month'] == month_index]

        
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df, filter_type):
    """Displays statistics on the most frequent times of travel, with questions and gaps."""

    print('\nCalculating the first statistic...')
    print("\nWhat is the most popular hour for travel?")
    start_time = time.time()

    popular_hour_stats = df['hour'].value_counts().nlargest(1)
    popular_hour = popular_hour_stats.index[0]
    count = popular_hour_stats.values[0]
 
    print(f"Most popular hour:{popular_hour}, Count:{count}, Filter:{filter_type}\n") 
    
    print(f"That took {time.time() - start_time} seconds.")


def station_stats(df, filter_type):
    """Displays statistics on the most popular stations and trip, with questions and gaps."""

    print('\nCalculating the next statistic...popular_station')
    print("\nWhat are the most popular start and end stations?")
    start_time = time.time()

    most_common_start_station = df['Start Station'].mode()[0]
    start_count = df['Start Station'].value_counts().max()
    
    most_common_end_station = df['End Station'].mode()[0]
    end_count = df['End Station'].value_counts().max()
    
  
    print(f"Start Station:{most_common_start_station}, Count:{start_count} - End Station:{most_common_end_station}, Count:{end_count}, Filter:{filter_type}\n") 

    print('\nCalculating statistic...') 
    print("\nWhat was the most popular trip from start to end?") 
    start_time_trip = time.time() 
    
    df['Route'] = df['Start Station'] + " & " + df['End Station']
    most_common_route_stats = df['Route'].value_counts().nlargest(1)
    most_common_route = most_common_route_stats.index[0]
    route_count = most_common_route_stats.values[0]
    
  
    print(f"Trip:('{most_common_route}'), Count:{route_count}, Filter:{filter_type}\n") 

    print(f"That took {time.time() - start_time_trip} seconds.")


def trip_duration_stats(df, filter_type):
    """Displays statistics on the total and average trip duration, with questions and gaps."""

    print('\nCalculating the next statistic...trip_duration')
    print("\nWhat is the total and average trip duration?")
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    trip_count = len(df)
    
    # Result with line break appended
    print(f"Total Duration:{total_travel_time:.1f}, Count:{trip_count}, Avg Duration:{mean_travel_time:.10f}, Filter:{filter_type}\n") 
    
    print(f"That took {time.time() - start_time} seconds.")


def user_stats(df, filter_type):
    """Displays statistics on bikeshare users, with questions and gaps."""

    print('\nCalculating statistic...') 
    print("\nWhat is the breakdown of users?")
    start_time_user_type = time.time()

    user_type_counts = df['User Type'].value_counts()
    
    output_string = ', '.join([f"{name}s:{count}" for name, count in user_type_counts.items()])
 
    print(f"{output_string}, Filter:{filter_type}\n")
    
    print(f"That took {time.time() - start_time_user_type} seconds.")

    print('\nCalculating statistic...')
    print("\nWhat is the breakdown of gender?")
    start_time_gender = time.time()

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        gender_output_string = ', '.join([f"{name}:{count}" for name, count in gender_counts.items()])
     
        print(f"{gender_output_string}, Filter:{filter_type}\n")
    else:
        print("No gender data to share.")

    print(f"That took {time.time() - start_time_gender} seconds.")

    print('\nCalculating statistic...')
    print("\nWhat is the oldest, youngest, and most popular year of birth, respectively?")
    start_time_birth = time.time()

    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        
      
        print(f"({earliest_year:.1f}, {most_recent_year:.1f}, {most_common_year:.1f})\n")
    else:
        print("No birth year data to share.")

    print(f"That took {time.time() - start_time_birth} seconds.")


def display_raw_data(df):
    """
    Displays 5 lines of raw data upon user request, formatted vertically for readability.
    """
    i = 0
    while True:
        if i >= len(df):
            print("\nNo more raw data to display.")
            break
            
        view_data = input('\nWould you like to view individual trip data? Type \'yes\' or \'no\'.\n').lower()
        
        if view_data == 'yes':
            raw_batch = df.iloc[i:i+5]
            
            for index, row in raw_batch.iterrows():
                record_dict = row.to_dict()
                
                print("--- Record Start ---")
                for key, value in record_dict.items():
                    if pd.isna(value):
                        print(f"'{key}': '',")
                    elif key == 'Birth Year':
                        print(f"'{key}': '{value:.1f}',")
                    else:
                        print(f"'{key}': '{value}',")
                print("--- Record End ---\n")

            i += 5
            
        elif view_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main():
    while True:
        city, month, day = get_filters()
        
       
        if month != 'all' and day != 'all':
            filter_type = 'both'
        elif month != 'all':
            filter_type = 'month'
        elif day != 'all':
            filter_type = 'day'
        else:
            filter_type = 'none'

        start_time_main = time.time() 
        
        df = load_data(city, month, day)

        time_stats(df, filter_type)
        station_stats(df, filter_type)
        trip_duration_stats(df, filter_type)
        user_stats(df, filter_type)
        
        display_raw_data(df)

        print(f"\nTotal analysis took {time.time() - start_time_main:.2f} seconds.")
        
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()