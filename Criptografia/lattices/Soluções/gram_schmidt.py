import numpy as np

v = []
v.append([])
aux = [4,1,3,-1]
v.append(aux)
aux = [2,1,-3,4]
v.append(aux)
aux  = [1,0,-2,7]
v.append(aux)
aux  = [6,2,9,-5]
v.append(aux)

u = []
u.append([])
u.append(v[1])
u.append([])
u.append([])
u.append([])


for i in range(2,5):
    u[i] = v[i]
    for j in range(1,i):
        aux = (np.inner(v[i],u[j]))/(np.inner(u[j],u[j]))
        u[i] -= np.multiply(aux,u[j])
        
    
print(u[1])
print(u[2])
print(u[3])
print(u[4])

#Still have problems with precision. So, approaching 0.91610738 to .5, you got 0.91611, the final asnwer.