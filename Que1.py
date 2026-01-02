#Problem 1:Given a list of laptimes, convert it into seconds and store the value in a new list
#Problem 2:Find the fastes lap,average laptime and consistency of the driver
#Problem 3:Finding the lap where degradation starts.(Lap after which the next 2 laps were slower)
#Problem 4:Find Out Avg Speed
#Problem 5:Checking consistency if the laptimes are within 0.5 seconds of the average
#Problem 6:Sector time analyser
#Problem 8:Delta time calculator between 2 laps
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
fastest=np.min(s_times)         #Problem 2 Solution
avg=np.mean(s_times).round(3)
cons=np.std(s_times).round(3)

print(s_times)
print(len(s_times))
print(f'Fastest lap: {fastest}')
print(f'Average lap times: {avg}')
print(f'Consistency: {cons}')
#3 Degradation problem
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
print(f'Deg lap: {deg_lap+1}')

#Creating an avg speed calculator given the distance is 5.807 km
race_dist=5.807
print(f'Race Distance:{race_dist} km\nAverage speed: {round((5.807*len(s_times)/sum(s_times))*3600,2)} kmph')

#Consistency check
dif=list(map(lambda x:round(x-avg,3),s_times))
def is_consis(n):
    if n>=-0.5 and n<=0.5:
        return True
    else:
        return False
diff=list(filter(is_consis,dif))
print(diff)

#Sector times analyser
laps = [
    [28.345, 30.112, 32.876],  # Lap 1
    [28.210, 30.054, 32.654],  # Lap 2
    [28.098, 29.998, 32.543],  # Lap 3
    [28.456, 30.220, 33.001],  # Lap 4
    [27.987, 29.876, 32.432],  # Lap 5
    [28.120, 30.010, 32.598],  # Lap 6
    [28.001, 29.945, 32.410],  # Lap 7
    [28.334, 30.180, 32.955]   # Lap 8
]
total_that_lap=list(map(lambda x:round(sum(x),3),laps))
print(total_that_lap)
print(f'Fastest Lap:{total_that_lap.index(np.min(total_that_lap))+1}')

#Calculatin delta time from 2 lap lists
lap1 = np.array([30.2, 30.5, 31.6])
lap2 = np.array([30.1, 30.4, 31.2])
delt=lap2-lap1
delt_full=round(np.sum(delt),3)
print(f'Delt full: {delt_full}')

