from datetime import datetime,timedelta
import datetime

def week_magic(day = datetime.datetime.today().date()):
    day_of_week = day.weekday()

    to_beginning_of_week = datetime.timedelta(days=day_of_week)
    print(to_beginning_of_week)
    beginning_of_week = day - to_beginning_of_week

    to_end_of_week = datetime.timedelta(days=6 - day_of_week)
    print(to_end_of_week)
    end_of_week = day + to_end_of_week

    return (beginning_of_week, end_of_week)


beginning_of_week , end_of_week = week_magic()

weekno = datetime.datetime.today()
print(weekno)