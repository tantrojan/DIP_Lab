import numpy as np

def N4(arr, i, j, V):
    m, n = arr.shape
    s = set()
    
    if arr[i][j] in V:
        if i-1 >= 0 and arr[i-1][j] in V:
            s.add((i-1, j))
        if i+1 < m and arr[i+1][j] in V:
            s.add((i+1, j))
        if j-1 >= 0 and arr[i][j-1] in V:
            s.add((i, j-1))
        if j+1 < n and arr[i][j+1] in V:
            s.add((i, j+1))
            
    if len(s) > 0:
        return s
    
def ND(arr, i, j, V):
    m, n = arr.shape
    s = set()
    
    if i-1 >= 0 and j-1 >= 0 and arr[i-1][j-1] in V:
        s.add((i-1, j-1))
    if i+1 < m and j+1 < n and arr[i+1][j+1] in V:
        s.add((i+1, j+1))
    if i-1 >= 0 and j+1 < n and arr[i-1][j+1] in V:
        s.add((i-1, j+1))
    if i+1 < m and j-1 >= 0 and arr[i+1][j-1] in V:
        s.add((i+1, j-1))
    
    if len(s) > 0:
        return s

def N8(arr, i, j, V):
    m, n = arr.shape
    s = set()
    
    if arr[i][j] in V:
        n4 = N4(arr, i, j, V) or []
        nd = ND(arr, i, j, V) or []
        for ng in n4:
            s.add(ng)
        for ng in nd:
            s.add(ng)
            
    if len(s) > 0:
        return s

def Nm(a, i, j, v):
    m, n = arr.shape
    s = set()
    
    if arr[i][j] in V:
        n4 = N4(arr, i, j, V) or []
        for ng in n4:
            s.add(ng)
        nd = ND(arr, i, j, V) or []        
        for ng in nd:
            nd_q = ND(arr, ng[0], ng[1], V)
            if len(nd.intersection(nd_q)) == 0:
                s.add(ng)
                
    if len(s) > 0:
        return s


# In[4]:


arr = np.array([[0, 1, 1 , 0, 1],
       [1, 1, 0 , 1, 1],
       [1, 0, 1 , 1, 1],
       [0, 1, 0 , 1, 1],
       [0, 1, 1 , 1, 0]])

m, n = arr.shape

V = [1]

print("4 Neighbours:")
for i in range(m):
    for j in range(n):
        print(N4(arr, i, j, V), end=", ")
    print()

print("\n8 Neighbours:")
for i in range(m):
    for j in range(n):
        print(N8(arr, i, j, V), end=", ")
    print()

print("\nM-adjacent Neighbours:")
for i in range(m):
    for j in range(n):
        print(Nm(arr, i, j, V), end=", ")
    print()

