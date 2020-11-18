#!/usr/bin/env python3

import sys
import numpy as np
from matplotlib import pyplot

#######This section is for to reading the given chromatogram file (superose6_50.asc)#######
Absfilename="superose6_50.asc"
Absfile=open(Absfilename,'r')
lines=Absfile.readlines()
Absfile.close()


#######This section of program makes one list for the absorption values of the points and one list for the time values of the points########

time=[]
absorption=[]
i=1
for line in lines[3:]:
  words=line.split("\t")
  try:
    time.append(float(words[0]))
    absorption.append(float(words[1]))
  
  except:
    print("could not parse line:", i)
    continue
  i+=1


#####With this section of the program it can differentiate between true peaks and false peaks (such as noises).####
####The measure is the BaseLine of the data#######

sum=0
for y in absorption:
  sum+=y
BaseLine=sum/len(absorption)
#print (BaseLine)

###This section loops over all data points to find the peaks.##### 
####The criteria is that neighboring points must have smaller values than the peak point#######

from scipy.signal import find_peaks

peaks, _ = find_peaks(absorption, height= BaseLine)

pk_value = []
time_value=[]
for i in peaks:
  pk_value.append(absorption[i])
  time_value.append(time[i])
  
  
print('peak values:',pk_value)
print('time values: ',time_value)


#####This section try to find the boundaries by slipping off of each peak and reaching the boundaries through considering two conditions:##### 
####the point after(or before) the current point has either a greater value or an equal value####

rightboundary=[];
leftboundary=[];
rp=[.0,.0]
lp=[.0,.0]
for p in pk_value:
  p_index=pk_value.index(p)
  p_time=time_value[p_index];
  p_time_index=time.index(p_time);
  leftboundary_index=p_time_index;
  rightboundary_index=p_time_index;
  while True:
    leftboundary_index=leftboundary_index-1;
    if absorption[leftboundary_index-1] >= absorption[leftboundary_index] or absorption[leftboundary_index-1] < BaseLine:
      leftboundary.append([time[leftboundary_index], absorption[leftboundary_index]]);
      break;
  while True:
    rightboundary_index+=1;
    if absorption[rightboundary_index+1] >= absorption[rightboundary_index] or absorption[rightboundary_index+1] < BaseLine:
      rightboundary.append([time[rightboundary_index], absorption[rightboundary_index]]);
      break;
  print("\nBoundaries of peak %s, %s"%(p_time,p));
  print("       Time       Abs")
  print("Left:  %s     %s"%(time[leftboundary_index], absorption[leftboundary_index]));
  print("Right: %s     %s"%(time[rightboundary_index], absorption[rightboundary_index]));

rp = np.array(rightboundary)
lp = np.array(leftboundary)

#print(rp);
#print(lp);

#######The output of this section is the results on a graph, showing the peaks and the boundaries marked with various colored indicators#### 


pyplot.plot(time,absorption,rp[:,0],rp[:,1],'bs',lp[:,0],lp[:,1],'ro',time_value, pk_value,'g^')

for a,b in zip(time_value, pk_value): 
    pyplot.text(a, b, str(b))
pyplot.show()
