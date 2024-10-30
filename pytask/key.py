
import time

import pytask.pop_up as pop_up
import pytask.task_list as task_list
import pytask.ihm as ihm



def main () -> None :
    b = task_list.backlog()
    w = pop_up.window()
    ihmm = ihm.ihm()
    ihmm.datas_update(b.list_backlog())

    while True :
        time.sleep(0.02) # Cooldown a litle
        if w.user_start :
            w.start()
        
        if w.user_end :
            ret = w.stop()
            b.add_task(ret)
            b.save_backlog()
            ihmm.datas_update(b.list_backlog())

        w.update()
        ihmm.manage()