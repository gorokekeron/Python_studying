#범위
    ### 파이썬의 모든 기능들은 범위를 지정할 때 뒤에 입력한 숫자를 포함하지 않는다.
    ###range()의 매개변수는 반드시 정수로만 작성되어야 한다. (정수 나누기 연산자 자주 사용됨)
#0~n-1까지 정수
print(list(range(5))) #0~4
#a~n-1까지 정수
print(list(range(5,11)))
#a~n-1까지 x만큼 차이를 갖음
print(list(range(5,50,4)))

#역반복문 : reversed()
for i in reversed(range(5)):
    print("now:{}".format(i))

#while 
i=0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i+=1


## break: 반복문을 벗어남
## continue : 조건 판별라인으로 걍 바로 감 (다음 명령은 실행x)


#리스트에 적용할 수 있는 기본 함수
list_num=[103,52,273,32,77,1]
print(min(list_num))
print(max(list_num))
print(sum(list_num))


#리스트 뒤집기
#1. 확장 슬라이싱 (비파괴적)
list_a = [1,2,3,4,5]
print(list_a[::-1])
print(list_a)
#2. reversed() 사용 (이것도 비파괴적인듯?)
print("reversed() : ",list(reversed(list_a))) #enumerate() 발생하는 것을 list()함수로 강제 변환 출력
######## Generator(제너레이터)&Iterator(이터레이터)
##이터러블(iterable):반복할 수 있는 것. 내부에 있는 요소들을 차례차례 꺼낼 수 있는 객체.
##이터레이터(iterator):이터러블 중에서 next()함수를 적용해 하나하나 꺼낼 수 있는 요소.

#반복문 리스트
list_ex = ["el_A","el_B","el_C",]
print(list_ex)
print("enumerate(): ",list(enumerate(list_ex))) #enumerate() 발생하는 것을 list()함수로 강제 변환 출력
for i, value in enumerate(list_ex):
    print("{}번째 요소는 {}입니다.".format(i,value))

#반복문 딕셔너리
dic_ex={
    "key_A":"val_A",
    "key_B":"val_B",
    "key_C":"val_C"
}
print("item() : ", dic_ex.items())
for key, element in dic_ex.items():
    print("dic_ex[{}] = {}".format(key, element))


#리스트 내포 list comprehensions
array = [i*i for i in range(0,10,2)]
print(array)    #결과 : [0, 4, 16, 36, 64]   i*i(이게 표현식임)가 들어간다..
array2 = ["appel","banana","chocolate"]
array2_output = [fruit for fruit in array2 if fruit!="chocolate"]
print(array2_output)