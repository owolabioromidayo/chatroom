import threading
import time


def singlethread(process):
    threading.Thread(target=process).start()


def multithread(processes, time_interval=0.00):
    threads = [threading.Thread(target=process) for process in processes]
    for thread in threads:
        thread.start()
        time.sleep(time_interval)
    for thread in threads:
        thread.join()
