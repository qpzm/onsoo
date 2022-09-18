#Kimhaeun
#22100224
#varFTs

#a

def sorted(a,b,c,d):
    input_nums=[a,b,c,d]
    nums=[a,b,c,d]
    nums.sort()
    reversed_nums=[]
    
    for i in range(3,-1,-1):
        reversed_nums.append(nums[i])
        
    if input_nums==nums or input_nums==reversed_nums:
        return True
    else:
        return False

for i in range(2):
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))
    d=int(input("d:"))
    print(sorted(a,b,c,d))
    
        
#예시
#print(sorted(3,0,-2,-5))
#print(sorted(3,0,3,0))
#print(sorted(2,8,12,16))
#print(sorted(0,0,0,0))


#b

def numDigit(n):
    s=n.split('.')
    int_pt=len(s[0])
    decimal_places=len(s[1])
    print("정수 자리 수",int_pt,", 소수 자리 수", decimal_places)

for i in range(2):
    n=str(input("n:"))
    numDigit(n)

#예시    
#numDigit(3.12)
#numDigit(119.0)
#numDigit(10.08217)



