# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:45:20 2020

@author: John
"""
import random
# Python3 program for implementation  
# of FCFS scheduling 
  
# Function to find the waiting  
# time for all processes 
def Waiting_Time(p, burst_time, waiting_time): 
  
    # waiting time for  
    # first process is 0 
    waiting_time[0] = 0
  
    # calculating waiting time 
    for i in range(1, p ): 
        waiting_time[i] = burst_time[i-1] + waiting_time[i-1]  
  
# Function to calculate turn 
# around time 
def Turnaround_Time(p, burst_time, waiting_time, turnaround_time): 

    # calculating turnaround  
    # time by adding burst_time + wait_time 
    for i in range(p): 
        turnaround_time[i] = burst_time[i] + waiting_time[i]
  
# Function to calculate 
# average time 
def average_time(p, burst_time): 
  
    waiting_time = [0] * p 
    turnaround_time = [0] * p  
    total_waiting_time = 0
    total_turnaround_time = 0
  
    # Function to find waiting  
    # time of all processes 
    Waiting_Time(p, burst_time, waiting_time) 
  
    # Function to find turn around  
    # time for all processes 
    Turnaround_Time(p, burst_time, waiting_time, turnaround_time) 
  
    # Display processes along 
    # with all details 
    print("\nProcesses" + " Burst time " + " Waiting time " + " Turnaround time") 
  
    # Calculate total waiting time  
    # and total turn around time 
    for i in range(p): 
        total_waiting_time = total_waiting_time + waiting_time[i] 
        total_turnaround_time = total_turnaround_time + turnaround_time[i] 
        print(str(i + 1) + "\t\t\t" + 
              str(burst_time[i]) + "\t\t\t" + 
              str(waiting_time[i]) + "\t\t\t\t" + 
              str(turnaround_time[i]))  
  
    print( "\nAverage waiting time = "+
                   str(total_waiting_time / p)) 
    print("Average turn around time = "+
                     str(total_turnaround_time / p)) 
  
# Driver code 
if __name__ =="__main__": 
      
    # process id's 
    p = int(input("How many processes? "))
  
    # Burst time of all processes
    c = input("Would you like to choose burst times? (enter 'y' for 'yes' or 'n' for 'no'")
    burst_time = []
    if c == 'y':
        for i in range(p):
            i = int(input("Enter Burst Time for Process {}: ".format(len(burst_time)+1)))
            burst_time.append(i)
    elif c == 'n':
        for i in range(p):
            i = random.randint(1,20)
            burst_time.append(i)
        
    average_time(p, burst_time) 