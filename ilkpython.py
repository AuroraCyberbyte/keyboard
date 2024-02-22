from pynput import keyboard

def tusaBasildiginda(tus):
    print("Basılan tuş {0}".format(tus))

def tusBirakildiginda(tus):
    print("Bırakılan tuş {0}".format(tus))

with keyboard.Listener(on_press=tusaBasildiginda, on_release=tusBirakildiginda) as dinleyici:
    dinleyici.join()



dinleyici = keyboard.Listener(on_press=tusaBasildiginda, on_release=tusBirakildiginda)
dinleyici.start()
        





    
