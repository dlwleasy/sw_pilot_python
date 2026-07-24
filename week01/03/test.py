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

list=[]
list=csv.split("\n") #1

# 배열에 넣기
i=0

for line in list:
  line=line.split(",")
  for k in range(len(list)):
    columns[i]=columns[i].extend(line[i])
    print(columns[i])
  i+=1

# 배열 결과
