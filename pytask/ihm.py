from os import system, name #know wich os is used.

# this module provide terminal interface.

#-------- Terminal --------
# 1 . Task One
# > 2 . Task Two
# 3 . Task Three
# 
# ########################
#  u : update, d : mark as done, r : remove
# win+alt+n : adding another task

class ihm():
    """_summary_ Print list of task, add a cursor to select one task and scroll between them
    """
    def __init__(self):
        self.list = None
        self.list_size = 0
        self.cursor = 0 # Position of the >
        self.clear_screen()
        pass

    def datas_update(self, datas : list[str]) -> None :
        self.list = datas
        self.list_size = len(datas)
    
    def clear_screen(self) -> None :
        # Clear_screen depend on the used OS
        if name == 'nt' :
            system('cls')
        else :
            system('clear')

    def head(self):
        print("########## /!\\PyTask/!\\ ##########")
    
    def tail(self) :
        print("####################################")
        print("# u : update, d : done, r : remove #")
        print("# WIN+ALT+N : new task             #")
        print("####################################")



def main() :
    IHM = ihm()
    
    IHM.head()
    print(">")
    IHM.tail()
    return

if __name__ == "__main__" :
    main()