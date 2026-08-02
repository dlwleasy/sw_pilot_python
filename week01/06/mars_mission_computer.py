import random

class DummySensor:

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
    

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 4)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values


ds=DummySensor() #instance
ds.set_env()
get=ds.get_env()



