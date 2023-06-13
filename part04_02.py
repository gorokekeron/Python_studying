#딕셔너리 접근
age = "나이"
dict_a={
    'name': "Jade",
    'info':[22,"백수",True],
    age : 222
}
print(dict_a)
print(dict_a['info'])

#딕셔너리 값 추가
dict_a["class"]="3-Z"
print(dict_a)
#딕셔너리 값 제거
del dict_a["class"]
print(dict_a)

#딕셔너리 내부에 키가 있는지 확인하기
print("name" in dict_a)
print(dict_a.get("존재하지 않는 키")) #존재하지 않는 키에 접근할 경우 KeyError를 발생시키지 않고 None 출력

#딕셔너리 for문
for key in dict_a:
    print(key, ":", dict_a[key])
    #  name : Jade
    #  info : [22, '백수', True]
    #  나이 : 222
