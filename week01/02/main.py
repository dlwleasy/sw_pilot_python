
from pprint import pprint
import json  # 1. 파이썬 기본 json 모듈 불러오기

try:
    with open('mission_computer_main.log','r',encoding='utf-8') as file:
        keys = file.readline().strip().split(",") #첫째줄 제외
        logs =file.read()
       # print(keys)
       # print(logs)


except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
except PermissionError:
    print("파일에 접근할 권한이 없습니다.")
except Exception as e:
    print(f"알 수 없는 에러가 발생했습니다: {e}")


log_list = logs.splitlines() # 문자열 logs -> list에 날짜별로 저장 :  print(log_list) //['2023-08-27 10:00:00,INFO,Rocket initialization process started.',]
list=[]
for line in log_list: # 현재 날짜별로 하나씩 가져와서
 list.append(line.split(",")) # 각 항목별 구분하여 리스트에 저장
pprint(list[:2],width=200)  # [['2023-08-27 10:00:00', 'INFO', 'Rocket initialization process started.'], ['2023-08-27 10:02:00', 'INFO', 'Power systems online. Batteries at optimal charge.']]

# 시간 역순으로 정렬 list.reverse()
list.reverse()
print("=========시간 역순 정렬=========")
pprint(list[:3],width=100)


# 사전 객체 전환 : 리스트의 값에 무엇을 의미하는지 키(이름) 지정
dict_list=[]
list.reverse()

for line in list:
    log_dict = {
 keys[0]: line[0],
 keys[1]: line[1],
 keys[2]: line[2],
       
    }
    dict_list.append(log_dict)
print(dict_list[:3])


# mission_computer_main.json 파일로 저장하는데
# 파일 포멧은 JSON(JavaScript Ontation)으로 저장

with open('mission_computer_main.json','w',encoding='utf-8') as file:
   # json.dump(저장할데이터, 파일객체, 들여쓰기설정, 한글깨짐방지)
    json.dump(dict_list, file, indent=4, ensure_ascii=False)
