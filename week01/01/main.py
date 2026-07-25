#1
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



# 1. 항목별로 입력 받기
title = input("보고서 제목을 입력하세요: ")
author = input("작성자 이름을 입력하세요: ")
content = input("분석 내용을 입력하세요: ")

# 2. 입력받은 데이터를 Markdown 형식으로 조립하기
markdown_content = f"""# {title}

**작성자:** {author}

## 분석 내용
{content}
"""

# 3. 파일에 저장하기
with open('log_analysis.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)

print("'log_analysis.md' 파일이 생성되었습니다.")



