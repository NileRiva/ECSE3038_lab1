import numpy as np

def parallel(arr):
    R=0
    for r in arr:
        R+= 1/r
    print("\"%.3f ohms\"" % (1/R))
    
    return 1/R

parallel([1000,1000])

def potential_divider(v,arr):
    Rtotal=0
    voltarr=[]
    for R in arr:
        Rtotal+=R
    for R in arr:
        voltarr.append((R/Rtotal)*v)
    for V in voltarr:
        print("\"%.2fv\"" % (V))
    return voltarr

potential_divider(10, [1000, 2000])

def temperature_check(temp,unit):
    if unit== "F":
        temp=(temp-32)*5/9
    if temp>=36.1 and temp<=37.2:##using normal temperature range according to mayo clinic
        print("\"the patient's temperature is normal\"")
    if temp>37.2:
        print("\"the patient is hyperthermic\"")
    if temp<36.1:
        print("\"the patient is hypothermic\"")


temperature_check(14, "C")
temperature_check(37, "C")
temperature_check(37, "F")
temperature_check(98.6, "F")
temperature_check(37.4, "C")