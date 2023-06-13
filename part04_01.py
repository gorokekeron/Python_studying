#리스트와 접근
list_a = [273,32,103,"문자열",True,False]
print(list_a[0])    #273
print(list_a[1:6])  #[32, 103, '문자열', True, False]
print(list_a[-1])   #False
print(list_a[3][0]) #문

#리스트 연산자 : + 연결 / * 반복 / len()
list_b=[4,5,6]
print(list_a+list_b)    #[273, 32, 103, '문자열', True, False, 4, 5, 6]
print(list_b*2)         #[4, 5, 6, 4, 5, 6]
print(len(list_b))      #3

#리스트에 요소 추가하기
list_b.append("append")
list_b.insert(1,"insert")
list_b.extend([10,11,12])
print(list_b)           #[4, 'insert', 5, 6, 'append', 10, 11, 12]

#### 연산자로 연결 : 비파괴적(리스트가 변경되지 않음)
#### 함수로 연결 : 파괴적(리스트가 변경됨)

#리스트에 요소 제거하기
list_c = [1,2,3,4,5,6,7,8,9,10,9,10,9,10]
del list_c[1]   #특정인덱스 제거
del list_c[5:7] #범위지정 제거
list_c.pop()    #마지막 인덱스 제거
list_c.pop(0)   #특정인덱스 제거
print(list_c)   #[3, 4, 5, 6, 9, 10, 9, 10, 9]
list_c.remove(9)#값으로 제거. 단, 가장 먼저 발견되는 하나만 제거된다.
print(list_c)   #[3, 4, 5, 6, 10, 9, 10, 9]
list_c.clear()  #모두 제거
print(list_c)   #[]

#리스트 내부에 있는지 확인하기 연산자 : in 과 not in
list_d=[10,11,12]       
print(10 in list_d)     #True
print(99 in list_d)     #False
print(10 not in list_d) #False
print(99 not in list_d) #True


#반복문
for i in range(10):
    print("출력")
list_f=[374,12,"문자열임",True]
for i in list_f:
    print(i)
for i in "안녕하세요":
    print("-",i,"-")
