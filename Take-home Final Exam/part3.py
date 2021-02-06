def billboardMaximize(billboard, revenue, n, limit):
    table=[]
    
    #base value
    for i in range(0, n):
        table.append(revenue[i])


    for i in range(1, n):
        #first two recursion case
        value = max(table[i - 1], table[i])
        #picking ith billboard, third recursion case
        for j in range(0,i):
            if (billboard[j] < billboard[i] - limit):
                value = max(value, table[j] + revenue[i])
        table[i] = value
    return table[n - 1]

billboard = [6, 7, 12, 13, 14] 
revenue = [5, 6, 5, 3, 1] 
n = len(billboard)
limit = 4
print(billboardMaximize(billboard, revenue, n, limit))