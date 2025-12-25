#Problem 1:Given a list of laptimes, convert it into seconds and store the value in a new list
#Problem 2:Find the fastes lap,average laptime and consistency of the driver
#Problem 3:Finding the lap where degradation starts.(Lap after which the next 2 laps were slower)
#Problem 4:Find Out Avg Speed
import numpy as np
lap_times = np.array([
    "1:32.345",
    "1:31.876",
    "1:32.102",
    "1:31.654",
    "1:31.998",
    "1:32.210",
    "1:31.543",
    "1:31.889",
    "1:32.034",
    "1:31.612",
    "1:31.734",
    "1:32.156",
    "1:31.598",
    "1:31.921",
    "1:32.045"
])
s_times=list(map(lambda x:round(int(x[0])*60+float(x[2:]),3),lap_times))  #Problem 1 Solution
fastest=np.min(s_times)
avg=np.mean(s_times).round(3)
cons=np.std(s_times).round(3)
s_times1=np.diff(s_times)

print(s_times)
print(len(s_times))
print(f'Fastest lap: {fastest}')
print(f'Average lap times: {avg}')
print(f'Consistency: {cons}')
p=0
deg_lap=-1
while p!=len(s_times):
    if s_times[p]<s_times[p+1]:
        if s_times[p+1]<s_times[p+2]:
            deg_lap=p
            break
        else:
            p+=1
    else:
        p+=1
print(f'Deg lap: {deg_lap}')

#Creating an avg speed calculator given the distance is 5.807 km
race_dist=5.807
avg_speed=(5.807*len(s_times)/sum(s_times))*3600
print(f'Average speed: {avg_speed}')


