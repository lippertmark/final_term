import time
import threading
import random

CNT_GET_DATA = 0
CNT_WRITE_TO_FILE = 0
CNT_WRITE_TO_CONSOLE = 0
list_get_data = {}
list_write_to_console = {}
list_write_to_file = {}


def get_data(task_id):
    print(f"processing get_data({task_id})")
    time.sleep(random.randint(1, 3))
    print(f"completed get_data({task_id})")


def obr_get_data(task_id):
    global CNT_GET_DATA
    CNT_GET_DATA += 1
    get_data(task_id)
    CNT_GET_DATA -= 1


def obr_write_to_console(task_id):
    global CNT_WRITE_TO_CONSOLE
    CNT_WRITE_TO_CONSOLE += 1
    write_to_console(task_id)
    CNT_WRITE_TO_CONSOLE -= 1


def obr_write_to_file(task_id):
    global CNT_WRITE_TO_FILE
    CNT_WRITE_TO_FILE += 1
    write_to_file(task_id)
    CNT_WRITE_TO_FILE -= 1


def write_to_file(task_id):
    print(f"processing write_to_file({task_id})")
    time.sleep(random.randint(1, 5))
    print(f"completed write_to_file({task_id})")


def write_to_console(task_id):
    print(f"processing write_to_console({task_id})")
    time.sleep(random.randint(1, 5))
    print(f"completed write_to_console({task_id})")


def doing_smth(task_id):
    list_get_data[task_id] = threading.Thread(target=obr_get_data, args=(task_id,))
    while CNT_GET_DATA > 10:
        time.sleep(1)
    list_get_data[task_id].start()
    list_get_data[task_id].join()
    list_write_to_file[task_id] = threading.Thread(target=obr_write_to_file, args=(task_id,))
    list_write_to_console[task_id] = threading.Thread(target=obr_write_to_console, args=(task_id,))

    while CNT_WRITE_TO_FILE > 5:
        time.sleep(1)
    list_write_to_file[task_id].start()
    while CNT_WRITE_TO_CONSOLE > 1:
        time.sleep(1)
    list_write_to_console[task_id].start()


list_doing_smth = []
for task_id in range(1, 21):
    list_doing_smth[task_id] = threading.Thread(target=doing_smth, args=(task_id,))
    list_doing_smth[task_id].start()
