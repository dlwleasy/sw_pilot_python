import numpy as np
import csv
# 1
file_list = ['mars_base_main_parts-001.csv','mars_base_main_parts-002.csv','mars_base_main_parts-003.csv']

arr1 = np.loadtxt(file_list[0],dtype='str', delimiter=',', encoding='utf-8', skiprows=1)
arr2 = np.loadtxt(file_list[1],dtype='str', delimiter=',', encoding='utf-8', skiprows=1)
arr3 = np.loadtxt(file_list[2],dtype='str', delimiter=',', encoding='utf-8', skiprows=1)

# 2
parts = np.vstack((arr1,arr2,arr3))

# 3 
# -> 공통요소 = 위치, 이름 -> 위치 : 값[i :: 100] / 이름 & 값의 위치 동일 

keys = parts[:,0]
values = parts[:,1].astype(int)
# 3-1 parts_to_work_on.csv
try:
 with open("parts_to_work_on.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
 
    for i in range(100):
     mean = np.mean(values[i::100])  
     if 50.0 > (mean):
      writer.writerow([keys[i],round(mean,3)])
    print("저장 완료")

except OSError as e:
    print(f"파일 저장 중 오류가 발생했습니다: {e}")
