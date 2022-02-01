def add_time(start, duration, day='None'):

    if int(duration.split(':')[1]) >= 60 or int(duration.split(':')[1]) < 0:
        print("Error: Minutes should be a whole number less than 60")
        quit()

    start_hour = start.split(':')[0]
    start_min = start.split(':')[1].split(' ')[0]
    duration_hours = duration.split(':')[0]
    duration_min = duration.split(':')[1]

    if start[-2:] == 'PM':
        start_hour = str(int(start_hour) + 12)

    sum_hour = str(int(start_hour) + int(duration_hours))

    sum_min = str(int(start_min) + int(duration_min))

    if int(sum_min) > 60:
        sum_hour = str(int(sum_hour) + 1)

    new_hour = str(int(sum_hour) % 24)
    if new_hour == '0':
        new_hour = '12'

    suffix = 'AM'

    if int(new_hour) > 12:
        suffix = 'PM'
        new_hour = str(int(new_hour) - 12)

    new_min = str(int(sum_min) % 60)

    if int(new_min) > 0 and int(new_hour) == 12 and start.split(':')[1].split(' ')[1] == 'AM':
        suffix = 'PM'
    if int(new_min) < 10:
        new_min = '0' + new_min

    x = int(sum_min) // 60
    hours = int(duration.split(':')[0]) + x
    day_count = 0
    day_count += hours // 24
    if hours % 24 > 24 - int(start_hour):
        day_count += 1

    if suffix == 'AM' and new_hour == '12' and int(new_min) > 0:
        day_count += 1

    new_time = new_hour + ':' + new_min + ' ' + suffix

    if day != 'None':

        days = [
            'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday'
        ]

        current_day = days.index(day.capitalize())
        sum_days = current_day + day_count
        new_day = days[sum_days % 7]

        new_time += ', {}'.format(new_day)

    if day_count == 1:
        new_time += ' (next day)'

    elif day_count == 0:
        pass

    else:
        new_time += ' ({} days later)'.format(day_count)

    return new_time
