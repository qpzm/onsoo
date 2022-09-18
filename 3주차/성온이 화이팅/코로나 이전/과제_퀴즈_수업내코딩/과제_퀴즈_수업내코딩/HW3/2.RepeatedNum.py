#Kimhaeun
#22100224
#가장 많이 반복된 수와 횟수, 가장 큰 수

num_list=[]
count=[0 for i in range(30)]
most=[]
most_count=0
most_count_list=[]

for i in range(30):
    n=int(input("정수를 입력하세요:"))
    num_list.append(n)

largest = n

for num in num_list:
    if num > largest:
        largest=num

for i in range(30):
    for j in range(30):
        if num_list[i]==num_list[j]:
            count[i]+=1

for i in range(29):
    if count[i]>count[i+1] and count[i]>most_count:
        most_count=count[i]
        if num_list[i] not in most:
            most.append(num_list[i])
            most_count_list.append(count[i])
           
for i in range(30):
    if count[i] == most_count and num_list[i] not in most:
        most.append(num_list[i])
        most_count_list.append(count[i])

print("가장 많이 반복된 수와 빈도수:", end=' ')
for i in range(len(most)):
    if i==len(most)-1:
        print(most[i],most_count_list[i],'회')
    else:
        print(most[i],most_count_list[i],'회,',end=' ')
                       
print("가장 큰 수:",largest)
