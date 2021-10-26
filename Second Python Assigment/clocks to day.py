def convert_to_days():
    hours = eval(input("Enter numbers of hours"))
    minutes = eval(input("Enter minuntes"))
    seconds = eval(input("Enter seconds"))
    
    result= get_days(hours, minutes, seconds)
    print(f"The number of days is: {result}")
    
    
def get_days(hours: int, minutes: int, seconds: int):
    nDays = ((seconds / 3600) + (minutes / 60) + hours) / 24
    
    return round(nDays, 4)

convert_to_days()