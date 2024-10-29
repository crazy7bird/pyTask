from pathlib import Path

class backlog() :
    def __init__(self, filePath : Path = ".note"):
        self.filePath = filePath
        self.taskList= []
        self.fileLoad()
        pass

    def fileLoad(self, filePath : Path = None) :
        if filePath is None :
            filePath = self.filePath
        with open(filePath, "rt") as file:
            for line in file.readlines() :
                task = line.rstrip('\n')
                if task :
                    self.taskList.append(task)

    def list_backlog(self) :
        return self.taskList

    def add_task(self, task:str) :
        self.taskList.append(task)
    
    def save_backlog(self) :
        with open(self.filePath, "wt") as f:
            for line in self.taskList:
                f.write(f"{line}\n")