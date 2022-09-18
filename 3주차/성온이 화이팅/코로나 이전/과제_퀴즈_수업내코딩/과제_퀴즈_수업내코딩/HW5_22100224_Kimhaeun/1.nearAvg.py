#kimhaeun
#22100224
#nearAvg

import math

def nearAvg(numList):
    gapList=[]
    ave=0
    ave=sum(numList)/len(numList)
    for num in numList:
        gap=math.fabs(ave-num)
        gapList.append(gap)
    index=gapList.index(min(gapList))
    closest=numList[index]
    return index, closest, ave


print(nearAvg([10,9,8,7,-6,-5,-4,-3]))
print(nearAvg([1,2,3,4,5,6,7,8,9]))
print(nearAvg([0,1,3,5,-7,-9,0]))
