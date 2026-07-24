# 2. 무게 재계산

# 기존 무게
weight_on_earth = {"유리": 2.4, "알루미늄": 2.7, "탄소강": 7.85}  # 단위: g/cm^3
weight_on_mars = {}
# 화성의 중력을 반영한 무게 재계산 
def calculate_weight_on_mars(weight_on_earth):
    print("화성에서의 무게")
    for name,weight in weight_on_earth.items():
        # weight_on_earth[weight] = weight_on_earth[weight] * (3.71 / 9.81)  # 화성 중력 가속도 / 지구 중력 가속도
        weight_on_mars[name] =round(weight * 0.378, 3) # 화성 중력 가속도 / 지구 중력 가속도
        print(f" {name} : {weight_on_mars[name]:.3f}입니다.")
    
    return weight_on_mars

weight=calculate_weight_on_mars(weight_on_earth)
print(weight)