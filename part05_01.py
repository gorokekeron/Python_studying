##임시
__enumerate() 함수
__딕셔너리의 items() 함수와 반복문 조합하기
__리스트 내포

55인치 티비가 좋을듯.



05-2 함수의 활용
__재귀 함수
__재귀 함수의 문제
__조기 리턴
__[누적예제] 리스트 평탄화하는 재귀 함수 만들기
[좀 더 알아보기] 코드에 이름 붙이기
[좀 더 알아보기] 코드 유지보수
[3가지 키워드로 정리하는 핵심 포인트]
[확인문제]

05-3 함수 고급
__튜플
__람다
__파일 처리
[좀 더 알아보기] 혼자 공부하는 파이썬 프로그래밍
[좀 더 알아보기] 제너레이터
[좀 더 알아보기] 리스트 함수의 key 키워드 매개변수
[좀 더 알아보기] 스택, 힙
[좀 더 알아보기] 함수의 값 복사와 레퍼런스 복사
[3가지 키워드로 정리하는 핵심 포인트]
[확인문제]















#def 함수명(매개변수):  //def는 함수를 만들 때 사용하는 예약어
#    <수행할 문장>

# 입력값이 몇 개가 될지 모를 때: 가변 매개변수
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

#매개변수 초기값      
value_times(1,2,3,4, times=5)

#함수 안에서 함수 밖의 변수 변경하는 법
# 1. return 사용하기
# 2. global 명령어 사용하기 (비추)
# 3. lambda :람다. def를 사용할 정도로 복잡하지 않거나 사용할 수 없는 곳에서 사용. lambda로 만든 함수는 return 명령어가 없어도 표현식의 결과값을 리턴한다.
## 사용법 : 함수명=lambda 매개변수1,... : 표현식
add = lambda a, b : a+b
result = add(3,4)
print("result =",result)
