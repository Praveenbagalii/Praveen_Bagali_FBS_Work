### Convert the time entered in hh,min and sec into seconds
seconds = int(input("Enter time in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f'Time in HH:MM:SS format is {hours}:{minutes}:{remaining_seconds}')