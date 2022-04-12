def days_later(days):
  if days == 1:
    return(" (next day)")
  if days >= 2:
    return f" ({days} days later)"
  return ""

def print_day(day, days):
  if day == "":
    return days_later(days)    
  if days == 0:
    return ", " + day.capitalize()
  day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  day_number = day_list.index(day)
  day_number += days
  return ", " + day_list[day_number % 7].capitalize() + days_later(days)

def write_time(total_hours, total_mins):  
  if total_hours < 12:
    if total_hours == 0:
      total_hours += 12
    return "{0:01d}".format(total_hours) + ":" + "{0:02d}".format(total_mins) + " AM"
  else:
    if total_hours == 12:
      total_hours += 12
    return "{0:01d}".format(total_hours - 12) + ":" + "{0:02d}".format(total_mins) + " PM"

def add_time(start, duration, day=""):
  day = day.lower()
  start_combined = start.split()
  pm = True
  if start_combined[1] == "AM":
    pm = False
  start_time = start_combined[0].split(":")
  start_hour = int(start_time[0])
  start_min = int(start_time[1])
  if pm:
    start_hour += 12  
  
  duration_info = duration.split(":")
  duration_hour = int(duration_info[0])
  duration_min = int(duration_info[1])

  total_hours = start_hour + duration_hour
  total_mins = start_min + duration_min
  if total_mins > 59:
    total_mins -= 60
    total_hours += 1

  return write_time(total_hours % 24, total_mins) + print_day(day, int(total_hours / 24))