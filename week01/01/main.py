print("Hello Mars")

try:
    with open('mission_computer_main.log','r',encoding='utf-8') as f:
        logs = f.read()
        print(logs)
except FileNotFoundError:
    print("해당 파일이 존재하지 않습니다.")
except PermissionError:
    print("파일에 접근할 권한이 없습니다.")
except Exception as e:
    print(f"예상치 못한 오류가 발생했습니다.: {e}")

