import psutil
import time

process = "java"
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
 
def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
 
    listOfProcessObjects = []
 
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
 
    return listOfProcessObjects;
 
def main():
 
    print("*** Check if a process is running or not ***")
 
    # Check if any process process was running or not.
    if checkIfProcessRunning(process):
        print(f"Yes a {process} process was running")
    else:
        print('No process process was running')
 
 
 
    print("*** Find PIDs of a running process by Name ***")
 
    # Find PIDs od all the running instances of process that contains 'process' in it's name
    listOfProcessIds = findProcessIdByName(process)
 
    if len(listOfProcessIds) > 0:
       print('Process Exists | PID and other details are')
       for elem in listOfProcessIds:
           processID = elem['pid']
           processName = elem['name']
           processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
           print((processID ,processName,processCreationTime ))
    else :
       print('No Running Process found with given text')
 
 
    print('** Find running process by name using List comprehension **')
 
    # Find PIDs od all the running instances of process that contains 'process' in it's name
    procObjList = [procObj for procObj in psutil.process_iter() if 'process' in procObj.name().lower() ]
 
    for elem in procObjList:
       print (elem)
 
 
if __name__ == '__main__':
   main()
