##임시
#__enumerate() 함수
#__딕셔너리의 items() 함수와 반복문 조합하기
#__리스트 내포


#def 함수명(매개변수):  //def는 함수를 만들 때 사용하는 예약어
#    <수행할 문장>

# 입력값이 몇 개가 될지 모를 때: 가변 매개변수 
#*가변 매개변수 뒤에는 일반 매개변수가 올 수 없고, 가변 매개변수는 하나만 사용할 수 있다.
#def 함수이름(*매개변수{,다른 매개변수....}):
#   <수행할 문장>
def add_many (*args):
    result = 0;
    for i in args:
        result +=i
    return result
print("first:  {}".format(add_many(10,20,30)))
print("second: {}".format(add_many(1000,500)))

def value_times(*values, times=2):
    for value in values:
        print(times*value)

#..이상 위치 매개변수 (positional argument) 전달방식이며 매개변수의 순서대로 인자를 입력받아 실횅한다.

##키워드 매개변수(kwargs) : ** 
# 키워드 매개변수로 전달하면 함수 내에서 딕셔너리로 인식한다.
def saveDic(category,**kargs):
    print("카테고리 : ",category)
    print(kargs)
saveDic("과일",a="사과",b="banana")
# +) 딕셔너리의 키가 숫자일 경우 update(dic)해서 값을 수정할 수 있다.  -> 찾아봐...

#기본매개변수 : 매개변수 초기값       *기본 매개변수 뒤에는 일반 매개변수가 올 수 없음.
value_times(1,2,3,4, times=5)

#함수 안에서 함수 밖의 변수 변경하는 법
# 1. return 사용하기
# 2. global 명령어 사용하기 (비추)
# 3. lambda :람다. def를 사용할 정도로 복잡하지 않거나 사용할 수 없는 곳에서 사용. lambda로 만든 함수는 return 명령어가 없어도 표현식의 결과값을 리턴한다.
## 사용법 : 함수명=lambda 매개변수1,... : 표현식
add = lambda a, b : a+b
result = add(3,4)
print("result =",result)


#재귀함수의 문제 : (피보나치 예를 들면) n번째 값을 구할 때 같은 값을 구하는 연산을 반복하는 문제가 있음 -> 메모화를 사용
#메모를 활용한 피보나치 

#메모 변수 생성
dictionary = {
    1:1,
    2:1
}

#함수 선언
def fibonacci(n):
    if n in dictionary : #메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else: #메모가 되어 있지 않으면 값을 구함.
        output = fibonacci(n-1)+ fibonacci(n-2)
        dictionary[n]=output
        return output

#함수 호출
print("fibonacci(50)",fibonacci(50))



#tuple튜플 : 리스트와 비슷한 자료형으로, 리스트와 달리 한번 결정된 요소는 바꿀 수 없다. 함수와 같이 자주쓰임/괄호 없이 여러 값을 할당하는 것이 큰 특징
tuple_test = (10,20,30)
#tuple_test[0]=100 #에러발생 does not support item assignment
#요소를 하나만 갖는 튜플은
tuple_test2=(10,) #쉼표가 들어가야 해!!!!!!! (안 그럼 그냥 숫자를 괄호로 감싼걸로 인식..)
#괄호 없이도 튜플을 활용할 수 있다.
tuple_test3=10,20,30,40
print('typle_test3',tuple_test3)
print('type(tuple_test3):',type(tuple_test3))
a,b,c=10,20,30 #괄호없는 튜플 활용
print("a:",a)
#변수의 값을 변경하는데 자주 활용된다.
d,e = 10, 20
print("교환 전")
print('d:{}, e:{}'.format(d,e))
d,e=e,d
print("교환 후")
print('d:{}, e:{}'.format(d,e))


#lambda람다 : 아주 간단하고 쉽게 함수를 선언하는 방법

