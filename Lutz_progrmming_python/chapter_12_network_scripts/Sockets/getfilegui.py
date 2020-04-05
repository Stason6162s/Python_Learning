import os
from tkinter import Tk, mainloop
from tkinter.messagebox import showinfo

import Lutz_progrmming_python.chapter_12_network_scripts.Sockets.getfile as getfile
from Lutz_progrmming_python.chapter_12_network_scripts.Sockets.form import Form


class GetFileForm(Form):
    def __init__(self, one_shot=False):
        root = Tk()
        root.title("GetFileForm")
        labels = ['Server name', 'Port number', 'File name', 'Local Dir?']
        Form.__init__(self, labels, root)
        self.one_shot = one_shot

    def on_Submit(self):
        Form.on_Submit(self)
        local_dir = self.content['Local Dir?'].get()
        port_number = self.content['Port number'].get()
        file_name = self.content['File name'].get()
        server_name = self.content['Server name'].get()
        if local_dir:
            os.chdir(local_dir)
        port_number = int(port_number)
        getfile.client(server_name, port_number, file_name)
        showinfo('get file gui', 'Download completed')
        if self.one_shot:
            Tk().quit()


if __name__ == '__main__':
    GetFileForm()
    mainloop()
