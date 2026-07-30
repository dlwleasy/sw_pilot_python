import random

class DummySensor:
    env_values={
        'mars_base_internal_temperature':null,
        'mars_base_external_temperature':,
        'mars_base_internal_humidity':,
        'mars_base_external_illuminance':,
        'mars_base_internal_co2':,
        'mars_base_internal_oxygen':,
    }

    def set_env():
        random_data=[]
        random_data=random_data.append(random.uniform(18,30))
        random_data=random_data.append(random.uniform(0,21))
        random_data=random_data.append(random.uniform(50,60))
        random_data=random_data.append(random.uniform(500,715))
        random_data=random_data.append(random.uniform(0.02,0.1))
        random_data=random_data.append(random.uniform(4,7))

    def get_env():
        return env_values


ds=DummySensor() #instance
set=ds.set_env()
get=ds.get_env()

try:
    with open("mars_mission_computer.py","w",encoding='utf-8') as file:
        file
except Exception as e:
    print(f"예상치 못한 오류가 발생했습니다.: {e}")

