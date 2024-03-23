'''
Time Calculator

Write a function named add_time that takes in two required parameters and one optional parameter:

 - a start time in the 12-hour clock format (ending in AM or PM)
 - a duration time that indicates the number of hours and minutes
 - (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

TESTS

Calling add_time('3:30 PM', '2:12') should return '5:42 PM'.
Calling add_time('11:55 AM', '3:12') should return '3:07 PM'.
Expected time to end with '(next day)' when it is the next day.
Expected period to change from AM to PM at 12:00.
Calling add_time('2:59 AM', '24:00') should return '2:59 AM (next day)'.
Calling add_time('11:59 PM', '24:05') should return '12:04 AM (2 days later)'.
Calling add_time('8:16 PM', '466:02') should return '6:18 AM (20 days later)'.
Expected adding 0:00 to return the initial time.
Calling add_time('3:30 PM', '2:12', 'Monday')should return '5:42 PM, Monday'.
Calling add_time('2:59 AM', '24:00', 'saturDay') should return '2:59 AM, Sunday (next day)'.
Calling add_time('11:59 PM', '24:05', 'Wednesday') should return '12:04 AM, Friday (2 days later)'.
Calling add_time('8:16 PM', '466:02', 'tuesday') should return '6:18 AM, Monday (20 days later)'.


______________________________________________________________________________________
Thought Process
1. Make a tuple to store the days of the week.
2. Parse the input string and store start time, duration and start day in a list. Like so,
    start = [hours, minutes, time_period]
    duration = [hours, minutes]
    start_day = [start_day]
3. Convert start to 24 hour day format.
    start_hour = hours + (0 if time_period == 'AM' else 12)
4. Compute for total_duration_minutes = duration_hours * 60 + duration_hours_minutes
5. new_time_minutes is computed by 
    new_time_minutes = (int(start_minutes) + total_duration_minutes) % 60
6. new_time_hours is computed by
    (new_time_hours_24 % 12 if new_time_hours_24 not in [0, 12] else 12)
7. increment_day is computed by 
    increment_day = (start_hours + (total_duration_minutes + int(start_minutes)) // 60) // 24.
8  Compute for the new_day and increment_day_counter
9. Convert the new_time to 12-hour format.
10. Format and print the result
'''

days_of_week = ("monday", "tuesday", "wednesday",
                "thursday", "friday", "saturday", "sunday")


def add_time(start, duration, start_day=''):
    start_time, start_time_period = start.split()
    start_hours, start_minutes = start_time.split(':')
    start_hours = int(start_hours) + (0 if start_time_period == 'AM' else 12)

    duration_hours, duration_minutes = duration.split(':')
    total_duration_minutes = int(duration_hours) * 60 + int(duration_minutes)

    new_time_minutes = (int(start_minutes) + total_duration_minutes) % 60
    if len(str(new_time_minutes)) == 1:
        new_time_minutes = '0' + str(new_time_minutes)
    new_time_hours_24 = (
        start_hours + (total_duration_minutes + int(start_minutes)) // 60) % 24
    new_time_hours = (new_time_hours_24 %
                      12 if new_time_hours_24 not in [0, 12] else 12)
    new_time_period = ('PM' if new_time_hours_24 >= 12 else 'AM')

    increment_day = (start_hours + (total_duration_minutes +
                     int(start_minutes)) // 60) // 24.

    if increment_day > 1:
        increment_day_counter = '(' + str(int(increment_day)) + ' days later)'
    elif increment_day == 1:
        increment_day_counter = '(next day)'
    else:
        increment_day_counter = ''

    if start_day:
        start_day = start_day.lower()
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + increment_day) % 7
        new_day = days_of_week[int(new_day_index)].capitalize()
    else:
        new_day = ''

    # Output format - new_hour:new_minute new_time_period new_day (day increment)
    if start_day and increment_day != 0:
        new_time_string = f'{new_time_hours}:{new_time_minutes} {new_time_period}, {new_day} {increment_day_counter}'
    elif increment_day == 0 and new_day:
        new_time_string = f'{new_time_hours}:{new_time_minutes} {new_time_period}, {new_day}'
    elif increment_day > 0:
        new_time_string = f'{new_time_hours}:{new_time_minutes} {new_time_period} {increment_day_counter}'
    else:
        new_time_string = f'{new_time_hours}:{new_time_minutes} {new_time_period}'

    return new_time_string


print(add_time('11:59 AM', '00:01'))
