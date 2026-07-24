print("Hello Mars")

try:
    with open('mission_computer_main.log','r',encoding='utf-8') as f:
        logs = f.read()
        print(logs)
except FileNotFoundError:
    print("Error: The log file does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
except PermissionError:
    print("파일에 접근할 권한이 없습니다.")
except Exception as e:
    print(f"알 수 없는 에러가 발생했습니다: {e}")
