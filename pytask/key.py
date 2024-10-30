
import time

import pytask.pop_up as pop_up
import pytask.task_list as task_list



def main () -> None :
    b = task_list.backlog()
    w = pop_up.window()

    t = 0

    while True :
        time.sleep(0.1) # Cooldown a litle
        if w.user_start :
            w.start()
        
        if w.user_end :
            ret = w.stop()
            print(f"Final Entry : {ret}")
            b.add_task(ret)
            b.save_backlog()


        w.update()

        if time.time() > t + 4 :
            print(f"Entry : {b.list_backlog()}")
            t = time.time()
