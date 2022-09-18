'''
작성자 : 21900326 박현민
3번 문제 - 년도를 입력 받는다. 이 때 1보다 작은 값이 입력되면, "처리 할 수 없는
년도로, 에러입니다" 출력한다. 제대로 입력된 정수이면 윤년인지 평년인지를 확인한
후 Boolean data type, 변수 leap에 윤년이면 True, 윤년이 아니면 False를 저장한다.
변수 leap에 저장된 값이 True 이면 "????년은 윤년입니다." False 이면 "???년은
평년입니다" 출력 하시오. 입력된 년도가 4의 배수이면서, 100의 배수가 아닐 때
또는 400의 배수일 때 윤년이다.
'''
year=int(input('년도를 입력하시오 : '))

if year<1:
    print('처리 할 수 없는 년도로, 에러입니다')

else:
    if year%4==0 and not year%100==0 or year%400==0:
        leap=True
    else:
        leap=False

    if leap==True:
        print(year,'년은 윤년입니다')
    else:
        print(year,'년은 평년입니다')
            
