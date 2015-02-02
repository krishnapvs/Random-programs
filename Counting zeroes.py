l=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]

'''global count'''
count=0
def counter(l,count):
    if l[0]==1:
        return 0
    else:
        count= count+counter(l[1:],count)
        
    return 1

count+=counter(l,0)
print count
'''
for i in l:
    if (i != 0):
        break
    else:
        count+=1
print count'''

