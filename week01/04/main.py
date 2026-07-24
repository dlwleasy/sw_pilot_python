# 1. 결정되는거 : 재질, 지름,두께,면적
# 반구체의 돔 면적 구하기
def sphere_area(diameter, material, thickness=1):
    radius = diameter / 2
    area = 2 * 3.14159 * (radius ** 2)  # 반구체 면적 공식: 2πr^2
    return area

# material,diameter = 사용자 입력
# 기본값 material=유리, thickness=1

input_materal = input("재질을 입력하세요(사용할 수 있는 재로 :유리, 탄소강, 알루미늄): ").strip()
input_diameter = input("지름을 입력하세요 : ").strip()

# material = input_materal if input_materal else "유리"

# 사용 할 수 있는 재료 : 유리, 알루미늄, 탄소강
if input_materal not in ["유리", "알루미늄", "탄소강"]:
    raise ValueError("사용할 수 있는 재료는 유리, 알루미늄, 탄소강입니다.")
else :
    material = input_materal


try:
    diameter = float(input_diameter)
except input_diameter == 0:
    print("지름은 0이 될 수 없습니다.")
except ValueError:
    print("지름은 숫자로 입력해야 합니다.")

# 구하기 - 면적
area=sphere_area(diameter=diameter, material=material)
print(f"반구체의 돔 면적은 {area:.3f}입니다.")

# 2. 무게 재계산

# 화성의 중력을 반영한 무게 재계산 
def calculate_weight_on_mars(weight_on_earth):
    gravity_earth = 9.81  # 지구 중력 가속도 (m/s^2)
    gravity_mars = 3.71   # 화성 중력 가속도 (m/s^2)
    
    weight_on_mars = {}
    for material, weight in weight_on_earth.items():
        #  소수점 이하 세 자리까지만 출력
        weight_on_mars[material] = weight * (gravity_mars / gravity_earth)

    
    return weight_on_mars
weight_on_earth = {"유리": 2.4, "알루미늄": 2.7, "탄소강": 7.85}  # 단위: g/cm^3
calculate_weight_on_mars(weight_on_earth)
  