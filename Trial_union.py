l=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]

'''global count'''
count=0
def counter(l,count):
    if l[0]==1:
        return count
    else:
        count=counter(l[1:],count)
        count=count+1
    return count

count=counter(l,0)
print count
'''
for i in l:
    if (i != 0):
        break
    else:
        count+=1
print count'''

