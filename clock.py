from datetime import datetime, date, time
import time
# start_time = datetime.now()
# # do your work here
# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))
print(datetime.now())

now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

t_string = now.strftime("%H:%M:%S")
t_check = now.strftime("%H")

print(t_check)

print("time =", t_string)
