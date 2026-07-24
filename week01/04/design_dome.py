
# 1. 결정되는거 : 재질, 지름,두께,면적
# 반구체의 돔 면적 구하기
def sphere_area(diameter, material, thickness=1):
    radius = diameter / 2
    area = 2 * 3.14159 * (radius ** 2)  # 반구체 면적 공식: 2πr^2
    return {"재질": material,"지름":diameter, "면적": round(area, 3), "두께": thickness}

# material,diameter = 사용자 입력 (기본값 material=유리, thickness=1)
input_materal = input("재질을 입력하세요(사용할 수 있는 재로 :유리, 탄소강, 알루미늄): ").strip()
input_diameter = input("지름을 입력하세요 : ").strip()

# 사용 할 수 있는 재료 : 유리, 알루미늄, 탄소강
if input_materal not in ["유리", "알루미늄", "탄소강"]:
    raise ValueError("사용할 수 있는 재료는 유리, 알루미늄, 탄소강입니다.")
else :
    material = input_materal

# 지름 조건
try:
    diameter = float(input_diameter)
except input_diameter == 0:
    print("지름은 0이 될 수 없습니다.")
except ValueError:
    print("지름은 숫자로 입력해야 합니다.")

# 구하기 - 면적
info = sphere_area(diameter=diameter, material=material)
# print(f"반구체의 돔 면적은 {area:.3f}입니다.")

# 2. 무게 재계산

# 기존 무게
weight_on_earth = {"유리": 2.4, "알루미늄": 2.7, "탄소강": 7.85}  # 단위: g/cm^3
weight_on_mars = {}
# 화성의 중력을 반영한 무게 재계산 
def calculate_weight_on_mars(weight_on_earth):
    print("화성에서의 무게")
    for name,weight in weight_on_earth.items():
        #(3.71 / 9.81)  # 화성 중력 가속도 / 지구 중력 가속도
        weight_on_mars[name] =round(weight * 0.378, 3) 
        print(f" {name} : {weight_on_mars[name]:.3f}입니다.")
    
    return weight_on_mars

weight=calculate_weight_on_mars(weight_on_earth) # print(weight)


# 전역변수에 지정
materal=info["재질"]
diameter=info["지름"]
thickness=info["두께"]
area=info["면적"]
weight=weight[materal]
print(f"재질 : {materal}, 지름 : {diameter}, 두께 : {thickness}, 면적 : {area}, 무게 : {weight}")



