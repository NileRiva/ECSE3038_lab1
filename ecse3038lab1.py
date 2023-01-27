import numpy as np

def parallel(arr):
    R=0
    for r in arr:
        R+= 1/r
    print("\"%.3f ohms\"" % (1/R))
    
    return 1/R

parallel([330, 1000, 2200])

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

potential_divider(9, [3000, 1000])
