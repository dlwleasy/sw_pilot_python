import random
import json
import time

import platform
import psutil


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
            print(json.dumps(self.env_values,indent=4,ensure_ascii=False))

            time.sleep(5)
            
            ans=input("계속 하시겠습니까? (y/n) : ").lower()
            if ans =="y":
                continue
            elif ans =="n":
                print("System stopped")
                break
            else:
                print("y또는 n만 입력해주세요.") 

    def get_mission_computer_info(self):
        system_info = {
        "os": platform.system(),              # 예: Windows, Linux
        "os_version": platform.version(),     # OS 빌드/커널 정보
        "cpu_type": platform.processor() or platform.machine(),
        "cpu_core_count": psutil.cpu_count(logical=False),  # 물리 코어 수
        "memory_bytes": psutil.virtual_memory().total,      # 전체 RAM (byte)
        }

        system_info_json=json.dumps(system_info, indent=4, ensure_ascii=False)
        print(f"시스템 정보 : {system_info_json}")
    
    def get_mission_computer_load():
        cpu_info={
            "cpu_usage_percent": psutil.cpu_percent(interval=0.1),
            "memory_usage_percent": psutil.virtual_memory().percent
        }
        cpu_info_json=json.dumps(cpu_info, indent=4, ensure_ascii=False
    )
        print(f"시스템 부하 : {cpu_info_json}")
        
    
        

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
RunComputer.get_sensor_data() 

runComputer=MissionComputer()
info=runComputer.get_mission_computer_info()
print(f"시스템 정보 : {info}")



