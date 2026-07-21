

try:
    with open('mission_computer_main.log','r',encoding='utf-8') as f:
        logs = f.read()
        # print(logs)
except FileNotFoundError:
    print("Error: The log file does not exist.")

# change to list 
# 리스트 안에  timestamp,event,message 각각이 담기게 정리

log_list=logs.split("/n")
print(log_list)
sorted_list=log_list.sort()
reversed_list=sorted_list.reverse()
