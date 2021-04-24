"""This program is a graphic interface to modelise bike traffic in Montpellier
    : First step select the week you want to modelise
    : Second step select days you want to modelise
    : Then press make video ! It will create you a video by day. 
"""
import os
import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
import montpellier_biking as mb


class Application():
    selected_days = [0]*7
    week = 1

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1230x700')
        self.week = Application.week
        # self.root.geometry('1800x1500')
        self.init_image()
        self.init_widgets()
        self.selected_days = Application.selected_days
        # self.add_event()

    def init_image(self):
        """
        Set the first graphic
        """
        self.img_rep = os.path.dirname(__file__)+"/data/images/"
        self.img = ImageTk.PhotoImage(Image.open(self.img_rep+"0.png"))

    def init_widgets(self):
        """
        Init widgets
        """
        # init listbox
        self.listbox = tk.Listbox(activestyle='dotbox', height=13)
        self.listbox.insert(1, "01/04-04/28")
        for i in range(1, 13): 
            self.listbox.insert(i, "week "+str(i))
        self.listbox.bind("<<ListboxSelect>>", self.callback_list)
        self.lng = Checkbar(self.root, ['0: Monday', '1: Tuesday',
                                        '2: Wednesday', '3: Thursday',
                                        '4: Friday', '5: Saturday',
                                        '6: Sunday'])
        self.label_text1 = tk.Label(text="Select day: ")
        self.bouton = tk.Button(self.root, text="Quit",
                                command=self.root.destroy)
        self.bouton_vid = tk.Button(self.root, text="Make Video!",
                                    command=self.callbakc_vid)
        self.my_label = tk.Label(self.root, image=self.img)
        # Set widget position
        self.my_label.place(x=0, y=0)
        self.listbox.place(x=1105, y=0)
        self.bouton.place(x=1190, y=639)
        self.bouton_vid.place(x=1103, y=639)

    def callbakc_vid(self):
        pass
    #     if self.week != 0 and self.selected_days != [0]*7:
    #         load = mb.Load_db.Load_db()
    #         data = load.set_df()
    #         for i in range(len(self.selected_days)):
    #             if self.selected_days[i] == 1:
    #                 mb.vis.animation.Animation(load.bikes_list(data, self.week, i))
    #     else:
    #         tkinter.messagebox.showinfo(title="Attention", message="You didn't select a week and days")

    def callback_list(self, event):
        selection = self.listbox.curselection()
        if selection[0] != 0:
            self.lng.place(x=270, y=670)
            self.label_text1.place(x=200, y=670)
        else:
            self.lng.place_forget()
            self.label_text1.place_forget()
        self.img = ImageTk.PhotoImage(Image.open(
                                      self.img_rep+str(selection[0])+".png"))
        self.my_label.configure(image=self.img)
        self.week = selection[0]


class Checkbar(tk.Frame):
    def __init__(self, parent=None, picks=[], side=tk.LEFT, anchor=tk.W):
        tk.Frame.__init__(self, parent)
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.var5 = tk.IntVar()
        self.var6 = tk.IntVar()
        self.var7 = tk.IntVar()
        self.chk1 = tk.Checkbutton(self, text='0: Monday', variable=self.var1,
                                   command=self.check_day_list1)
        self.chk1.pack(side=side, anchor=anchor, expand=tk.YES)
        self.chk2 = tk.Checkbutton(self, text='1: Tuesday', variable=self.var2,
                                   command=self.check_day_list2)
        self.chk2.pack(side=side, anchor=anchor, expand=tk.YES)
        self.chk3 = tk.Checkbutton(self, text='2: Wednesday', variable=self.var3,
                                   command=self.check_day_list3)
        self.chk3.pack(side=side, anchor=anchor, expand=tk.YES)
        self.chk4 = tk.Checkbutton(self, text='3: Thursday', variable=self.var4,
                                   command=self.check_day_list4)
        self.chk4.pack(side=side, anchor=anchor, expand=tk.YES)
        self.chk5 = tk.Checkbutton(self, text='4: Friday', variable=self.var5,
                                   command=self.check_day_list5)
        self.chk5.pack(side=side, anchor=anchor, expand=tk.YES)
        self.chk6 = tk.Checkbutton(self, text='5: Saturday', variable=self.var6, command=self.check_day_list6)
        self.chk6.pack(side=side, anchor=anchor, expand=tk.YES)
        self.chk7 = tk.Checkbutton(self, text='6: Sunday', variable=self.var7, command=self.check_day_list7)
        self.chk7.pack(side=side, anchor=anchor, expand=tk.YES)

    def check_day_list1(self):
        Application.selected_days[0] = self.var1.get()

    def check_day_list2(self):
        Application.selected_days[1] = self.var2.get()

    def check_day_list3(self):
        Application.selected_days[2] = self.var3.get()

    def check_day_list4(self):
        Application.selected_days[3] = self.var4.get()

    def check_day_list5(self):
        Application.selected_days[4] = self.var5.get()

    def check_day_list6(self):
        Application.selected_days[5] = self.var6.get()

    def check_day_list7(self):
        Application.selected_days[6] = self.var7.get()



if __name__ == "__main__":
    app = Application()
    app.root.title("MONTPELLIER_BIKING")
    app.root.mainloop()



