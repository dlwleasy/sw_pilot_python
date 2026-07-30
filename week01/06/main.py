import random

class DummySensor:

    env_values={

        'mars_base_internal_temperature':random_data[0],
        'mars_base_external_temperature':,
        'mars_base_internal_humidity':,
        'mars_base_external_illuminance':,
        'mars_base_internal_co2':,
        'mars_base_internal_oxygen':,
    }
    

    def set_env():
        random_data = [
        random.uniform(18, 30),
        random.uniform(0, 21),
        random.uniform(50, 60),
        random.uniform(500, 715),
        random.uniform(0.02, 0.1),
        random.uniform(4, 7),
        ]
        return random_data

    def get_env():
        return env_values


# ummySensor 클래스를 ds라는 이름으로 인스턴스(Instance)로 만든다.인스턴스화 한 DummySensor 클래스에서 set_env()와 get_env()를 차례로 호출해서값을 확인한다.

# 전체 코드를 mars_mission_computer.py 파일로 저장한다.

ds=DummySensor() #instance
set=ds.set_env()
get=ds.get_env()

try:
    with open("mars_mission_computer.py","w",encoding='utf-8') as file:
        file.writer()
except Exception as e:
    print(f"예상치 못한 오류가 발생했습니다.: {e}")

