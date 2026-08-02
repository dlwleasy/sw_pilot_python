import numpy as np
import csv
# 1
file_list = ['mars_base_main_parts-001.csv','mars_base_main_parts-002.csv','mars_base_main_parts-003.csv']

arrays = []
for file in file_list:
  arr=np.loadtxt(file,dtype='str', delimiter=',', encoding='utf-8', skiprows=1)
  arrays.append(arr)

parts = arrays[0][:,0] 
strength1=arrays[0][:,1].astype(int)
strength2=arrays[1][:,1].astype(int)
strength3=arrays[2][:,1].astype(int)

# 열별 모아서 배열 안에 저장해줌
strengths = np.column_stack([
    strength1,
    strength2,
    strength3
])

strengths_mean =np.round(np.mean(strengths, axis=1),3) #각 행별 평균

# 3-1 parts_to_work_on.csv
try:
 with open("parts_to_work_on.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for i in range(100):
     mean=strengths_mean[i] 
     if 50.0 > (mean):
      writer.writerow([parts[i],mean])
    print("저장 완료")

except OSError as e:
    print(f"파일 저장 중 오류가 발생했습니다: {e}")
