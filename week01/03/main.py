# 03

with open("Mars_Base_Inventory_List.csv","r",encoding="utf-8") as file:

    file_name=file.readline() #2
    print(file_name) #2
    csv=file.read()
    print(csv) #1
    


# Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability
# Alcohol,0.789,0.79,Very weak,0.85
# Petroleum Products,Various,Various,Various,0.92
# Gasoline,Various,Various,Various,0.91


# 배열 명 만들기 : Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability
for name in file_name.split(","):
   name=[]

# 전체 리스트로 만들기 [1,2,3,4,5,6,7,8,9,10]->[하나씩 가져와서 배열에 넣기]

list=[]
list=csv.split("\n") #1

# 배열에 넣기
i=0
k=0

for line in list:
  line=line.split(",")
  for k in range(len(list)):
    name[i]=name[i].extend(line[i])
  i+=1

# 배열 결과
for i in range(len(name)):
    print(name[i])


# 정렬 
Flammability_sorted=Flammability.sort()

# 0.7 이상
danger_list=[]
for i in range(len(Flammability_sorted)):
 if Flammability_sorted[i]>=0.7:
    danger_list.append(Flammability_sorted)
    print(Flammability_sorted)

# csv 파일에 저장
with open('Mars_Base_Inventory_danger.csv','w',encoding='utf-8') as file:
   # (저장할데이터, 파일객체, 들여쓰기설정, 한글깨짐방지)
    csv.dump(danger_list, file, indent=4, ensure_ascii=False)


