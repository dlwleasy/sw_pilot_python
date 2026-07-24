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


# 배열 명 만들기 : Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability
for name in file_name.split(","):
   print(name)
   name=[]
   print(name)


# 전체 리스트로 만들기 [1,2,3,4,5,6,7,8,9,10]->[하나씩 가져와서 배열에 넣기]

list=[]
list=csv.split("\n") #1
pprint(list)


print("--------------------------------")
# 배열 결과
for i in range(len(file_name)):
    print(name[i])