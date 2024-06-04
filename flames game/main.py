x=input('enter first person name  :  ')
y=input('enter second person name  :   ')
l1=[i for i in x]
l2=[i for i in y]
i=0
while i<len(l1):
    c=0
    for j in range(0,len(l2)):
        if l1[i]==l2[j]:
            c=c+1
            l1.remove(l1[i])
            l2.remove(l2[j])
            break
    if c!=1:
        i=i+1
c=len(l1)+len(l2)
result=['F','L','A','M','E']
i=0
while len(result)!=1:
    if len(result)>= i+c:
        i = i + c - 1
        result.pop(i)
    else:
        i=i+c-len(result)-1
        if i>len(result)-1:
            i=i%len(result)
        result.pop(i)
final_result=result[0]
if final_result=='F':
    print('FRIENDS')
elif final_result=='L':
    print('LOVE')
elif final_result=='A':
    print('ATTRACTION')
elif final_result=='M':
    print('MARRIAGE')
else:
    print('ENEMY')




