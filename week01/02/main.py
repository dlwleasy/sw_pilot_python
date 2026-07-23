
from pprint import pprint

try:
    with open('mission_computer_main.log','r',encoding='utf-8') as file:
        logs = file.read()
        print(logs)


except FileNotFoundError:
    print("Error: The log file does not exist.")


# 첫째줄 제외 이중 리스트로 날짜 구분 및 (,) 기준 정보 구분하여 리스트 생성

log_list = logs.splitlines()[1:] # print(log_list)
list=[]
for line in log_list:
 list.append(line.split(","))
# print(list)

# 시간 역순으로 정렬 list.reverse()
list.reverse()
pprint(list,width=100)

# 사전 객체 전환 : 리스트의 값에 무엇을 의미하는지 키(이름) 지정



# mission_computer_main.json 파일로 저장하는데 파일 포멧은 JSON(JavaScript Ontation)으로 저장