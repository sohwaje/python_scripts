import psutil
"""
psutil.process_iter() 함수를 호출하여 프로세스 이름으로 pid를 찾는다.
"""
def findProcessIdByName(processName):
    listOfProcessObjects = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            if processName in pinfo['name']:
                listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listOfProcessObjects;

process = "pppd"  #pid를 찾을 프로세스 이름

"""
프로세스 상태 체크
"""
if findProcessIdByName(process):
    print(f"{process} is running.")
else:
    print(f"{process} was down.")

"""
findProcessIdByName 함수를 호출하여 받아온 값을 listOfprocessIds에 담는다.
"""
listOfprocessIds = findProcessIdByName(process)

"""
listOfprocessIds의 값이 0보다 크면 for문을 진행하고, pid, name, username을 각각 변수에 담는다.
"""
if len(listOfprocessIds) > 0:
    for element in listOfprocessIds:
        processID = element['pid']
        processName = element['name']
        processUsername = element['username']
        print(processID, processName, processUsername)
else:
    print('No Running Process found with given text')
