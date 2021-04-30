import numpy as np
import math
import time
start_time = time.time()

# If ||v2|| < ||v1||, swap v1, v2
# Compute m = ⌊ v1∙v2 / v1∙v1 ⌋
# If m = 0, return v1, v2
# v2 = v2 - m*v1

v = []
v1 = np.array([846835985, 9834798552],dtype=np.int64)
v2 = np.array([87502093, 123094980],dtype=np.int64)
aux = 0
m = 1

while(1):
    if(np.linalg.norm(v2) < np.linalg.norm(v1)):
        v1,v2 = v2,v1

    m = np.math.floor(np.inner(v1,v2)/np.inner(v1,v1))
    if(m == 0):
        break
    v2 = v2 - m*v1

print("Optimal basis: ", np.inner(v1,v2))
print("--- %s seconds ---" % (time.time() - start_time))