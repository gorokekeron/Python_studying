#date
import datetime
now = datetime.datetime.now()
print(now.year,"년",now.month,"월",now.day,"일  ","{:02d}".format(now.hour),"시","{:02d}".format(now.minute),"분",now.second,"초")
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))

#if
#false 로 치환되는 것 : None, 0, 0.0, 빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등)
input_number = input("정수 입력:>")
if int(input_number) > 0:
    print("양수입니다.")
if input_number[-1] in "02468":
    print("짝수입니다.")
else:
    print("홀수입니다.")

if(3<=now.month<=5):
    print("봄입니다.")
elif(6<=now.month<=8):
    print("여름입니다.")
elif(9<=now.month<=11):
    print("가을입니다.")
else:
    print("겨울입니다.")

 #pass키워드. 조건 실행문 미구현일때 사용
if(5>0):
    pass #아직 미구현 상태입니다.
print("5>0 끝")