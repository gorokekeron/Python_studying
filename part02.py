#p54 줄바꿈
print("""
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세""")
# 환경에 따라 위아래로 줄이 추가될 수 있어 아래와 같이 이스케이프를 추가해줄 수 있다.
print("""\
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세""")

#p56 문자 연산자
print("안녕하세요"+"!")
#print("HI"+1)    은 오류발생 (타입이 다름)
print("Hi~"*4)
print("안녕하세요"[0])  #결과 : 안
print("안녕하세요"[1:4]) #결과 : 녕하세   #파이썬은 >>마지막 숫자를 포함하지 않는다<< 그래서 1번째,2번째,3번째 글자만 출력됨
print("안녕하세요"[:3]) #결과 : 안녕하
print("안녕하세요"[-1]) #결과: 요
#글자수
print(len("안녕하세요")) #결과 : 5


#연산자
#정수 나누기 연산자 : //
print(7/5) # 결과 : 1.4
print(7//5) #결과 :1
#나머지 연산자 : %
print(7%5) # 결과 : 2
#제곱연산자 : **
print(2**10) #결과 : 1024


#p086 숫자를 문자열로 변경하기 : str()
print(type(str(6737)));  #결과 : <class 'str'>

#p093 문자열의 format()함수  //format() : 문자열이 갖은 함수. 중괄호의 개수와 format의 매개변수의 개수는 동일해야함.
string_a = "{} {} {}".format(101, 102, 103)
print(string_a) 
print(type(string_a)) #결과 : <class 'str'>
string_b="매개변수로는 : {} {} {}가 있습니다.".format(1985, "탄생", True)
print(string_b)
print(type(string_b)) #결과 : <class 'str'>
 #p097 특정 칸에 글 쓰기
print("{:10d}".format(10233))     #타입은 str
print("{:+015f}".format(52.273))  #결과 : +0000052.273000
print("{:15.1f}".format(52.273))  #결과 :            52.3
print("{:g}".format(52.0000000))  #결과 : 52

#문자의 양옆의 공백 제거: strip() //lstrip(), rstrip()도 존재
print("""                                                 안녕                  
               안녕하세요                                   """.strip())
#문자열 자르기 : split()
print("10 20 30 40 50 60".split(" "))  #결과 : ['10', '20', '30', '40', '50', '60']

#문자열 찾기 : find() //rfind()도 존재
print("안녕하세요. 안녕!".find("안녕"))  #결과 : 0
#문자열이 있는지 확인 : in 연산자
print("안녕" in "안녕하세요")           #결과 : True