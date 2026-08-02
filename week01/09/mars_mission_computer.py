import json
import multiprocessing
import platform
import psutil
import random
import threading
import time


class DummySensor:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None,
        }

    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = round(random.uniform(18, 30), 2)
        self.env_values["mars_base_external_temperature"] = round(random.uniform(0, 21), 2)
        self.env_values["mars_base_internal_humidity"] = round(random.uniform(50, 60), 2)
        self.env_values["mars_base_external_illuminance"] = round(random.uniform(500, 715), 2)
        self.env_values["mars_base_internal_co2"] = round(random.uniform(0.02, 0.1), 4)
        self.env_values["mars_base_internal_oxygen"] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values


class MissionComputer:
    def __init__(self, name):
        self.name = name
        self.sensor = DummySensor()
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None,
        }

    def get_sensor_data(self, interval=5, iterations=3):
        for _ in range(iterations):
            self.sensor.set_env()
            self.env_values = self.sensor.get_env()

            print(f"[{self.name}] 센서 데이터")
            print(json.dumps(self.env_values, indent=2, ensure_ascii=False))
            time.sleep(interval)

    def get_mission_computer_info(self, interval=20, iterations=3):
        for _ in range(iterations):
            system_info = {
                "os": platform.system(),
                "os_version": platform.version(),
                "cpu_type": platform.processor() or platform.machine(),
                "cpu_core_count": psutil.cpu_count(logical=False),
                "memory_bytes": psutil.virtual_memory().total,
            }

            print(f"[{self.name}] 컴퓨터 정보")
            print(json.dumps(system_info, indent=2, ensure_ascii=False))
            time.sleep(interval)

    def get_mission_computer_load(self, interval=20, iterations=3):
        for _ in range(iterations):
            cpu_info = {
                "cpu_usage_percent": psutil.cpu_percent(interval=0.1),
                "memory_usage_percent": psutil.virtual_memory().percent,
            }

            print(f"[{self.name}] 컴퓨터 부하")
            print(json.dumps(cpu_info, indent=2, ensure_ascii=False))
            time.sleep(interval)


def run_thread_demo():
    print("=== Threading demo ===")
    runComputer = MissionComputer("runComputer")

    threads = [
        threading.Thread(target=runComputer.get_mission_computer_info, args=(20, 3), daemon=True),
        threading.Thread(target=runComputer.get_mission_computer_load, args=(20, 3), daemon=True),
        threading.Thread(target=runComputer.get_sensor_data, args=(5, 3), daemon=True),
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


def run_process_demo():
    print("=== Multiprocessing demo ===")

    def worker_info():
        runComputer1 = MissionComputer("runComputer1")
        runComputer1.get_mission_computer_info(interval=20, iterations=3)

    def worker_load():
        runComputer2 = MissionComputer("runComputer2")
        runComputer2.get_mission_computer_load(interval=20, iterations=3)

    def worker_sensor():
        runComputer3 = MissionComputer("runComputer3")
        runComputer3.get_sensor_data(interval=5, iterations=3)

    processes = [
        multiprocessing.Process(target=worker_info),
        multiprocessing.Process(target=worker_load),
        multiprocessing.Process(target=worker_sensor),
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    run_thread_demo()
    run_process_demo()