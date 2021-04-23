import tkinter as tk
from PIL import Image, ImageTk

class Application():

    def __init__(self):
        self.root = tk.Tk()
        self.week=0
        #self.root.geometry('1800x1500')
        self.init_images()
        self.init_widgets()
        #self.add_event()
    
    def init_images(self):
        self.img_rep = "C:\\Users\\ponch\\python\\Montpellier_Biking\\montpellier_biking\\data\\images\\"
        self.img = ImageTk.PhotoImage(Image.open(self.img_rep+"0.png"))
    
    def init_widgets(self):
        self.label = tk.Label(self.root, text="J'adore Python !")
        self.listbox = tk.Listbox(activestyle='dotbox')
        self.listbox.insert(1, "01/04-04/28")
        for i in range(1, 13):
            self.listbox.insert(i, "week "+str(i))
        self.bouton = tk.Button(self.root, text="Quitter", command=self.root.quit)
        self.bouton_vid = tk.Button(self.root, text="Make Video!",
                                    command=callbakc_vid)
        self.my_label = tk.Label(self.root, image=self.img)
        self.my_label.pack(side=tk.TOP)
        self.listbox.bind("<<ListboxSelect>>", self.callback_list)
        self.listbox.pack()
        self.label.pack()
        self.bouton.pack()
    
    def callbakc_vid(event):
        if self.week != 0:
            


    def callback_list(self, event):
        selection = self.listbox.curselection()
        self.img = ImageTk.PhotoImage(Image.open(
                                      self.img_rep+str(selection[0])+".png"))
        self.my_label.configure(image=self.img)
        self.week = selection[0]
        #self.label.image = self.img
        print(selection[0])

if __name__ == "__main__":
    app = Application()
    app.root.title("Ma Première App :-)")
    app.root.mainloop()

