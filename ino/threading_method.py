import threading

class ths (threading.Thread) :
    def __init__(self, threadID, name, task, args):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name     = name
        self.task     = task
        self.args     = args
    def run(self) -> None:
        print("start " + self.name)
        self.task(self.args)
        print("exit " + self.name)
        return 

# def cal(info):
#     a = info[0]
#     b = info[1]
#     for _ in range(a):    
#         b += 1
#         print(f"cal: {b}")
#     return print(b)

# def dem(info):
#     a = info[0]
#     b = info[1]
#     for _ in range(a):
#         b -= 1
#         print(f"dem: {b}")
#     return print(b)

# def nothing(v):
#     print("Hi")

# th1 = ths(1, "th-1", cal, (100,0))
# th2 = ths(2, "th-2", nothing, (0))

# th1.start()
# th2.start()

# print("Main Threading")
