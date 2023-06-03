class Task:
    def __init__(self, _pTask, _Delay, _Period):
        self.pTask = _pTask
        self.Delay = _Delay 
        self.Period = _Period
        
    pTask = None # con trỏ hàm của Task làm gì trong task thì trỏ tới cái hàm do người dùng lập trình 
    Delay = 0
    Period = 0
    RunMe = 0 # Báo cho chương trình biến khi nào thực hiện 
    TaskID = -1 # Delete task through ID

class Scheduler:
    TICK = 100 
    SCH_MAX_TASKS = 40 # mAX OF TASK IS 40
    SCH_tasks_G = [] # array
    current_index_task = 0 # blank position in array

    def __int__(self):
        return

    def SCH_Init(self):
        self.current_index_task = 0

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD): # tìm vị trí trống 
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            aTask.TaskID = self.current_index_task
            self.SCH_tasks_G.append(aTask)
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")

    def SCH_Update(self): # hàm quan trọng nhất sẽ trừ đi thời gian nếu thời gian bằng 0 thì tức là tới khi task đó làm thì runme +1
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].Delay > 0:
                self.SCH_tasks_G[i].Delay -= 1
            else:
                self.SCH_tasks_G[i].Delay = self.SCH_tasks_G[i].Period
                self.SCH_tasks_G[i].RunMe += 1
                
    def SCH_Dispatch_Tasks(self): 
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].RunMe > 0:
                self.SCH_tasks_G[i].RunMe -= 1
                self.SCH_tasks_G[i].pTask() 

    def SCH_Delete(self, aTask):
        return

    def SCH_GenerateID(self):
        return -1
