import random
import json
import time
# mission computer
class MissionComputer:
    def __init__(self):
            # 멤버(인스턴스 변수)로 env_values 사전 객체를 초기화
            self.env_values = {
                'mars_base_internal_temperature': None,
                'mars_base_external_temperature': None,
                'mars_base_internal_humidity': None,
                'mars_base_external_illuminance': None,
                'mars_base_internal_co2': None,
                'mars_base_internal_oxygen': None
            }
    def get_sensor_data(self):
        while(True):
            # 동작 1 : 값 불러오기
            ds.set_env()
            self.env_values=ds.get_env()
            print(self.env_values)
            # 동작 2 : 값 저장하기
            #info_json=json.dumps(self.env_values,indent=4,ensure_ascii=False)
            #print(info_json)
            print(json.dump(self.env_values,indent=4,ensure_ascii=False))

            time.sleep(5)
            ans=input("계속 하시겠습니까? (y/n) : ").lower()
            if ans =="y":
                continue
            elif ans =="n":
                break
            else:
                print("y또는 n만 입력해주세요.") 


# dummy sensor
class DummySensor:

    def __init__(self):
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

ds=DummySensor()
RunComputer=MissionComputer() # 인스턴스화
MissionComputer.get_sensor_data() 

# 현재코드 파일 저장
with open(__file__, 'r', encoding='utf-8') as current_file:
    code_content = current_file.read()
with open('mars_mission_computer.py', 'w', encoding='utf-8') as target_file:
    target_file.write(code_content)

