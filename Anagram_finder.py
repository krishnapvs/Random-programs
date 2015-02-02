s1=raw_input("Enter string s1 to be checked: ")
s2=raw_input("Enter string to check in s2: ")
Dict={}

for i in s1:
    if ( i in Dict.keys()):
        Dict[i]+=1
    else:
        Dict[i]=1

Dict_help=dict(Dict)

L=[]
total=0

for i in range(len(s2)):
    Dict=dict(Dict_help)
    
    for j in range(len(s1)):
        if (i+j) < len(s2):
            if s2[i+j] in Dict.keys():
                if Dict[s2[i+j]]>0:
                    Dict[s2[i+j]]-=1
                else:
                    break
            else:
                break
        else:
            break
    for k in Dict.values():
        if k > 0:
            total=total+k
    
    if total==0:
        L.append(i+1)

    total = 0
    
print L
