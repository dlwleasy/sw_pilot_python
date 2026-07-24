# 03
from pprint import pprint

with open("Mars_Base_Inventory_List.csv","r",encoding="utf-8") as file:

    file_name=file.readline() #2
    print(file_name) #2
    csv=file.read()
    # print(csv) #1
    


# Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability
# Alcohol,0.789,0.79,Very weak,0.85
# Petroleum Products,Various,Various,Various,0.92
# Gasoline,Various,Various,Various,0.91


# # 배열 명 만들기 : Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability
# for name in file_name.split(","):
#    print(name)
#    name=[]
#    print(name)


# # 전체 리스트로 만들기 [1,2,3,4,5,6,7,8,9,10]->[하나씩 가져와서 배열에 넣기]

# list=[]
# list=csv.split("\n") #1
# pprint(list)


# print("--------------------------------")
# # 배열 결과
# for i in range(len(file_name)):
#     print(name[i])

# 배열 명 만들기 : Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability
headers = file_name.split(",")

# 헤더 개수만큼 빈 리스트 생성
columns = []
for h in headers:
    columns.append([])


Substance = columns[0]
Weight = columns[1]
Specific_Gravity = columns[2]
Strength = columns[3]
Flammability = columns[4]

# 전체 리스트로 만들기 [1,2,3,4,5,6,7,8,9,10]->[하나씩 가져와서 배열에 넣기]

rows_list=csv.split("\n") #1
# 배열에 넣기
# 3. 배열(컬럼)에 데이터 넣기
for line in rows_list:
    if not line.strip(): # 빈 줄은 건너뛰기
        continue
    
    items = line.split(",") # 쉼표 기준으로 컬럼 분리 (예: ['Alcohol', '0.789', ...])
    
    # 한 줄 안에서 0번부터 4번 컬럼까지 순서대로 각 columns 리스트에 append
    for i in range(len(headers)):
        columns[i].append(items[i])

# 배열 결과
# print("=== Substance (물질명 목록) ===")
# print(Substance)

print("\n=== Flammability (인화성 목록) ===")
print(Flammability[:5])

print("=== Flammability (인화성 목록) 정렬 ===")
# print(Flammability.sort())# 1. 실수(float)로 변환된 숫자를 담을 빈 리스트를 미리 만듭니다.
Flammability_float = []

# 2. 기존 문자열 리스트(Flammability)에서 항목을 하나씩 꺼냅니다.
for x in Flammability:
    # 3. 문자열(예: '0.85')을 실수(0.85)로 변환합니다.
    num = float(x)
    
    # 4. 변환된 숫자를 새 리스트에 하나씩 집어넣습니다.
    Flammability_float.append(num)

# # 정렬 
Flammability_float = [float(x) for x in Flammability]
Flammability_float.sort(reverse=True)
print("=== Flammability (인화성 목록) 정렬 ===")
print(Flammability_float[:3])  # 정렬된 원본 리스트 출력

# 0.7 이상
danger_list=[]
for i in range(len(Flammability_float)):
 if Flammability_float[i]>=0.7:
    danger_list.append(Flammability_float)
print("=== Flammability (인화성 목록) 0.7 이상 ===")
print(Flammability_float[:3])