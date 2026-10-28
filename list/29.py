#29.Store the temperature of 30 days and determine:
#a.Hottest day b.Coldest day c.Average temperature
#d.Days above average temperature e.Days below average temperature
temps = [30, 32, 31, 29, 28, 35, 36, 33, 31, 30, 27, 26, 34, 38, 37, 32, 30, 29, 31, 33, 35, 34, 28, 27, 29, 32, 31, 30, 36, 33]
print("temps =",temps)

hottest = max(temps)
coldest = min(temps)
avg_temp = sum(temps) / len(temps)

days_above_avg = sum(1 for t in temps if t > avg_temp)
days_below_avg = sum(1 for t in temps if t < avg_temp)

print("Hottest day temp:", hottest)
print("Coldest day temp:", coldest)
print("Average temperature:", avg_temp)
print("Days above average:", days_above_avg)
print("Days below average:", days_below_avg)