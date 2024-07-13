
import time
import math

def time_it(fn, *args, repetitions= 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    # Repetition should be positive number
    if repetitions <= 0:
        raise ValueError("Repetitions should be positive number")
    
    total_time = 0
    for i in range(repetitions):
          start = time.time()
          fn(*args, **kwargs)
          end = time.time()
          total_time += end - start

    return total_time / repetitions


def squared_power_list(number,*args, start=0, end=5,**kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validation checks
    if number < 0:
        raise ValueError("Number should be positive")
    if start < 0 or end < 0 or end < start:
        raise ValueError("Invalid values for start, end, or both")

    # Calculation and list creation
    result = [number ** i for i in range(start, end + 1)]

    return result


def polygon_area(length, *args, sides = 3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    # Validations
    if not isinstance(length, (int, float)):
        raise TypeError("Length should be an integer or float")

    if sides < 3 or sides > 6:
        raise ValueError("Number of sides should be between 3 and 6")

    return sides*(length**2)/(4*math.tan(math.pi/sides))

def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    if temp_given_in not in ['f', 'c',"F","C"]:
            raise ValueError("Invalid temperature scale specified")

    if not isinstance(temp, (int, float)):
            raise TypeError("Temperature should be an integer or float")

        # Temperature conversion
    if temp_given_in in ('f','F'):
          if temp < -459.67:
                raise ValueError("Temperature is below absolute zero")
          else:
                return (temp - 32) * 5 / 9
    elif temp_given_in in ('c','C'):
          if temp < -273.15:
                raise ValueError("Temperature is below absolute zero")
          else:
                return (temp * 9 / 5) + 32

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph to different units.
    dist can be km/m/ft/yrd and time can be ms/s/min/hr/day."""

    # Validations
    distance_units = ['KM', 'M', 'FT', 'YRD']
    time_units = ['MS', 'S', 'MIN', 'HR', 'DAY']


    if dist not in distance_units or time not in time_units:
        raise ValueError("Incorrect unit of distance or time")

    if not isinstance(speed, (int, float)):
        raise TypeError("Speed can be int or float type only")

    if speed < 0:
        raise ValueError("Speed can't be negative")

    # Conversion factors (kmph to specified unit)
    conversion_factors = {
    ('KM', 'MS'): 5 / 18,
    ('KM', 'S'): 5 / 18 * 1000,
    ('KM', 'MIN'): 1 / 60,
    ('KM', 'HR'): 1,
    ('KM', 'DAY'): 24,
    ('M', 'MS'): 1 / 360,
    ('M', 'S'): 1 / 360 * 1000,
    ('M', 'MIN'): 1 / 60000,
    ('M', 'HR'): 1 / 3600000,
    ('M', 'DAY'): 24 / 1000,
    ('FT', 'MS'): 82021 / 90000000,
    ('FT', 'S'): 82021 / 90000000000,
    ('FT', 'MIN'): 82021 / 2160000000,
    ('FT', 'HR'): 82021 / 129600000000,
    ('FT', 'DAY'): 102551 / 1314000000,
    ('YRD', 'MS'): 27391 / 25000000,
    ('YRD', 'S'): 27391 / 25000000000,
    ('YRD', 'MIN'): 27391 / 2160000000,
    ('YRD', 'HR'): 27391 / 129600000000,
    ('YRD', 'DAY'): 102551 / 9375000
    }


    # Calculate converted speed
    if (dist, time) in conversion_factors:
        return speed * conversion_factors[(dist, time)]
    else:
        raise ValueError("Conversion factor not found")
