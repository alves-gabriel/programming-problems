"""

In this problem we use the library datetime

References: 
- https://www.programiz.com/python-programming/datetime/strptime
- https://www.kite.com/python/docs/datetime.timedelta.total_seconds

%a: Abbreviated name of day of the weak
%d: Day
%b: Abbeviated month
%Y: Year

%H,M,S: Zero-padded hours, minutes and seconds

%z: Time-zone
"""

from datetime import *

# Here we define the data format. Note the use of :'s in the middle; we have to precisely write how the data will be read
dt_format = "%a %d %b %Y %H:%M:%S %z"

for _ in range(int(input())):

    # Time difference between the two lines
    time_difference = datetime.strptime(input(), dt_format) \
                    - datetime.strptime(input(), dt_format)
    
    # Here we use the funciton total_seconds() to perform the conversion
    print(int(abs(time_difference.total_seconds())))
