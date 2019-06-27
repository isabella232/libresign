#!/usr/bin/python3
# fill the screen with a background + URL for playlist website +
# instructions on how to use this software
# this runs as a separate process

from multiprocessing import Process
import tkinter as tk

proc = None
bg_color = "#55A555"

class TKInfoScreen(tk.Frame):
    def __init__ (self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

    def setup (self, url):
        font        = ('Helvetica', 30)
        smallfont   = ('Helvetica', 20)
        # NOTE text height = 50 is somewhat arbitrary
        height      = '50'

        self.msg_txt = tk.Label(self.master)
        self.msg_txt['text'] = \
            'Visit the URL below to reach the control panel.'
        self.msg_txt.configure(foreground='white', 
                               font=font, background=bg_color)
        self.msg_txt.place(relx='0.5', rely='0.4', anchor='center', 
                           height=height)

        # show the URL to which the end-users should connect to reach
        # the control panel
        self.url_text = tk.Label(self.master)
        self.url_text["text"] = url
        self.url_text.configure(background=bg_color, foreground='white', 
                                font=font)
        self.url_text.place(relx='0.5', rely='0.5', anchor='center', 
                            height=height)

        # link to code repo
        code_site = tk.Label(self.master)
        code_site['text'] = 'Get the code at: https://github.com/rptr/libresign'
        code_site.configure(background=bg_color, foreground='white', 
                                font=smallfont)
        code_site.place(relx='0', rely='1.0', anchor='sw', 
                            height=height)

        copyright = tk.Label(self.master)
        copyright['text'] = 'The Document Foundation'
        copyright.configure(background=bg_color, foreground='white', 
                                font=smallfont)
        copyright.place(relx='1.0', rely='1.0', anchor='se', 
                            height=height)

def info (url):
    root = tk.Tk()
    root.configure(background=bg_color)
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    app = TKInfoScreen(master=root)
    app.setup(url)
    app.mainloop()

def start_info (url):
    proc = Process(target=info, args=(url,))
    proc.start()
    # proc.join()

def stop_info ():
    if proc:
        proc.terminate()

