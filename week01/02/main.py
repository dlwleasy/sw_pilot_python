
from pprint import pprint
import json  # 1. 파이썬 기본 json 모듈 불러오기

try:
    with open('mission_computer_main.log','r',encoding='utf-8') as file:
        keys = file.readline().strip().split(",") # 첫째줄 제외
        logs = file.read()
       # print(keys)
       # print(logs)


except FileNotFoundError:
    print("Error: The log file does not exist.")


# 첫째줄 제외 이중 리스트로 날짜 구분 및 (,) 기준 정보 구분하여 리스트 생성

log_list = logs.splitlines() 
# print(log_list)
list=[]
for line in log_list:
 list.append(line.split(","))
print(list)

# 시간 역순으로 정렬 list.reverse()
list.reverse()
# pprint(list,width=100)

# 사전 객체 전환 : 리스트의 값에 무엇을 의미하는지 키(이름) 지정
dict_list=[]

for line in list:
    log_dict = {
 keys[0]: line[0],
 keys[1]: line[1],
 keys[2]: line[2],
       
    }
    dict_list.append(log_dict)
pprint(dict_list)


# mission_computer_main.json 파일로 저장하는데
# 파일 포멧은 JSON(JavaScript Ontation)으로 저장

with open('mission_computer_main.json','w',encoding='utf-8') as file:
   # json.dump(저장할데이터, 파일객체, 들여쓰기설정, 한글깨짐방지)
    json.dump(dict_list, file, indent=4, ensure_ascii=False)