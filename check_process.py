import psutil

"""
프로세스 실행 상태 감시
"""
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

"""
프로세스 이름으로  PID 찾기
"""
def findProcessIdByName(processName):
    listOfProcessObjects = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            if processName.lower() in pinfo['name'].lower():
                listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listOfProcessObjects;

"""
감시 대상 프로세스 이름
"""
process = "java"

"""
프로세스 상태 확인
"""
if checkIfProcessRunning(process):
    print(f"{process} is running.")
else:
    print(f"{process} was down.")

"""
프로세스 PID, 프로세스 이름, 사용자
"""
listOfprocessIds = findProcessIdByName(process)

if len(listOfprocessIds) > 0:
    print('Process Exists | PID and other detail are')
    for elem in listOfprocessIds:
        processID = elem['pid']
        processName = elem['name']
        processUsername = elem['username']
        print(processID, processName, processUsername)
else:
    print('No Running Process found with given text')
