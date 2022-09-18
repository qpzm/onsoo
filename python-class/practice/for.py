test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

name = "박성온수매트"
# i=0 -> name[0:1] -> 박
# i=1 -> name[0:2] -> 박성
# i=2 -> name[0:3] -> 박성온
for i in range(0, len(name)):
    print(name[0 : i + 1])
    # print("박")
    # print(name[ : 2])
    # print(name[ : 3])

#i=1 -> name[1 : 4] 성온수
#i=2 -> name[2 : 4] 온수
#i=3 -> name[3 : 4] 수
#i

# i=1 -> name[1:3] 성온
# i=2 -> name[2:3] 온
# i=3 -> name[] 성온수
for i in range(1, len(name)):
    print(name[i : len(name)])

print(name[-1])