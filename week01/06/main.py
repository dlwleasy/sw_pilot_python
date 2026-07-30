import random

class DummySensor:

    def init(self):
        # 멤버(인스턴스 변수)로 env_values 사전 객체를 초기화
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }
    

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 4)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values

# ummySensor 클래스를 ds라는 이름으로 인스턴스(Instance)로 만든다.인스턴스화 한 DummySensor 클래스에서 set_env()와 get_env()를 차례로 호출해서값을 확인한다.

# 전체 코드를 mars_mission_computer.py 파일로 저장한다.

ds=DummySensor() #instance
ds.set_env()
get=ds.get_env()


code_to_save='''import random

class DummySensor:

    def init(self):
        # 멤버(인스턴스 변수)로 env_values 사전 객체를 초기화
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }
    

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 4)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values

# ummySensor 클래스를 ds라는 이름으로 인스턴스(Instance)로 만든다.인스턴스화 한 DummySensor 클래스에서 set_env()와 get_env()를 차례로 호출해서값을 확인한다.

# 전체 코드를 mars_mission_computer.py 파일로 저장한다.

ds=DummySensor() #instance
ds.set_env()
get=ds.get_env()
'''


try:
    with open("mars_mission_computer.py", "w", encoding='utf-8') as file:
        file.write(code_to_save)
    print("\n'mars_mission_computer.py' 파일이 성공적으로 저장되었습니다.")
except Exception as e:
    print(f"예상치 못한 오류가 발생했습니다.: {e}")
