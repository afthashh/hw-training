# import datetime

# current= datetime.datetime.now()
# print(current)

# current_date = datetime.date.today()
# print(current_date)

# date = datetime.date(2023, 8, 14)
# print(date)

# datetime = current.strftime('%Y-%m-%d %H:%M:%S')
# print(datetime)

import time

current_time = time.time()
print(current_time)

time.sleep(10)
print("Done waiting.")

end_time = time.time()
struct_time = time.localtime(end_time)
print(struct_time)

