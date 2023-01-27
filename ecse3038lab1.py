def parallel(arr):
    R=0
    for r in arr:
        R+= 1/r
    print("\"%.3f ohms\"" % (1/R))
    
    return 1/R

parallel([330, 1000, 2200])