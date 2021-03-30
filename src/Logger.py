
import time


def info(message):
    print_message('I', message)



def error(message):
    print_message('E', message)



def debug(message):
    print_message('E', message)



def print_message(message_type, message):
    t = time.localtime()
    current_time = time.strftime("%Y%m%d_%H%M%S", t)
    print(f" {current_time}  |  {message_type}  |  {message}")
