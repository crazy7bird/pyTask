from os import system, name #know wich os is used.
import keyboard
import pytask.KBhit as KBhit

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
        self.kbhit = KBhit.KBHit()
        #keyboard.on_press_key("up arrow", lambda _: print('mkay'))
        #keyboard.on_press_key("down arrow", lambda _: print('mkayMouse'))

        pass

    def datas_update(self, datas : list[str]) -> None :
        self.list = datas
        self.list_size = len(datas)
        self.update()
    
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

    def screen_list(self) :
        for i,el in enumerate(self.list) :
            if self.cursor == i :
                print("> ",end="")
            elif "[V]" in el :     
                print('\u0336'.join(el) + '\u0336')
            else :
                print(el)

    def up(self):
        if self.cursor > 0 :
            self.cursor -= 1
    def down(self) :
        if self.cursor < (self.list_size -1) :
            self.cursor += 1

    def update(self) :
        self.clear_screen()
        self.head()
        self.screen_list()
        self.tail()

    def manage(self) :
        update = False
        if self.kbhit.kbhit():
            c = self.kbhit.getch()
            if ord(c) == 72: # UPARROW
                self.up()
                update = True
            elif ord(c) == 80: # DOWNARROW
                self.down()
                update = True

            if update :
                self.update()

    def __del__(self) :
        self.kbhit.set_normal_term()


def main() :
    data = ["One", "Deux", "Tress"]
    IHM = ihm()
    IHM.datas_update(data)
    IHM.manage()
    while True :
        IHM.manage()
        continue
    return

if __name__ == "__main__" :
    main()