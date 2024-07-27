import time


current_time_struct = time.localtime()

# Extract hours, minutes, and seconds from the structured time object
hours = current_time_struct.tm_hour
minutes = current_time_struct.tm_min
seconds = current_time_struct.tm_sec

# Print hours, minutes, and seconds
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")

# Optionally, print the full current time
current_time = time.ctime()
print(f"The time right now is {current_time}")



