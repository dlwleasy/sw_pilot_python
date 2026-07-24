import numpy as np
# print(np.__version__)


# 모두 numpy를 사용해서 읽어들여서 각각 
# arr1, arr2, arr3 과 같이 ndarray 타입으로
# 가져온다.

def ndarray(filename):
 try:
    with open(filename,'r',encoding='utf-8') as file:
        lines=file.readlines()

    data=[]
    for line in lines[1:]:
            row=[val for val in line.strip().split(',')]
            data.append(row)
    print(data[:5])
    
        # 2차원 리스트를 numpy ndarray로 변환하여 반환
    return np.array(data) # [[Steel,18],[Brick,92],[Wood,63]] 이 식으로

 except FileNotFoundError:
    print("Error: The log file does not exist.")
 except Exception as e:
    print(f"An unexpected error occurred: {e}")
 except PermissionError:
    print("파일에 접근할 권한이 없습니다.")
 except Exception as e:
    print(f"알 수 없는 에러가 발생했습니다: {e}")

    


# 지정된 파일명들을 각각 arr1, arr2, arr3에 할당
arr1 = ndarray('mars_base_main_parts-001.csv')
arr2 = ndarray('mars_base_main_parts-002.csv')
arr3 = ndarray('mars_base_main_parts-003.csv')

# 결과 확인
# print(type(arr1))
# print(arr1.shape)
# print(arr1)

# 이름을 parts 라는 ndarray :세로로 합치기
parts = np.hstack((arr1, arr2, arr3))
print(parts[:5])

# 평균 값 구하기

# 1. 부품 '이름'만 뽑아내기 (모든 행의 첫 번째 열(인덱스 0) 가져오기)
part_names = parts[:, 0]

# 2. '숫자'만 뽑아내서 실수(float)로 변환하기 (인덱스 1부터 2칸씩 건너뜀)
numbers_only = parts[:, 1::2]
numbers_num = numbers_only.astype(float)

# 3. 각 부품별(가로줄 방향) 평균 계산하기 
# 핵심: axis=1 은 '가로줄(행)끼리 계산해라'라는 뜻
part_averages = numbers_num.mean(axis=1)

# 4. 결과 출력 (zip을 사용해 이름과 평균값을 하나씩 짝지어서 출력)
print("=== 각 부품별 평균 강도 ===")
for name, avg in zip(part_names, part_averages):
    print(f"{name:<10} : {avg:.2f}")


    # 1. 평균값이 50보다 작은지 검사하는 '조건 마스크' 만들기
# 결과: [True, True, False, ...] 형태의 배열이 만들어집니다.
mask = part_averages < 50

# 2. 마스크(True인 항목)를 이용해 50 미만인 이름과 평균값만 쏙 뽑아내기
target_names = part_names[mask]
target_averages = part_averages[mask]

# 3. 저장하기 위해 이름과 평균값을 하나의 2차원 표(열 단위)로 묶어주기
# 결과 형태: [['Steel' '41.33'], ['Wood' '30.50'], ...]
# np.round(..., 2)를 써서 소수점 둘째 자리까지만 깔끔하게 저장합니다.
save_data = np.column_stack((target_names, np.round(target_averages, 2)))

# 4. 파일로 저장하기 (np.savetxt 사용)
# fmt='%s'는 문자열로 저장하라는 뜻이며, 구분자는 쉼표(,)를 사용합니다.
np.savetxt(
    'parts_to_work_on.csv', 
    save_data, 
    delimiter=',', 
    fmt='%s', 
    header='Part_Name,Average_Strength', 
    comments=''  # 헤더 앞에 # 기호가 붙는 것을 방지
)

print("=== 필터링된 부품 목록 ===")
print(save_data)
print("\n'parts_to_work_on.csv' 파일 저장이 완료되었습니다!")