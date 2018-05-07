try:
    import numpy as np
    import random
    
    myList = []
    for item in range(5):
        x = myList.append(np.array(input("")))
        print x[item]

except Exception, e:
    str(e)