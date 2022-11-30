from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import tkinter as tk

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        # setting attribute
        self.title("Hydroponics")
        self.configure(bg='#FFFFFF')
        # self.configure(bg='black')
        # self.attributes('-fullscreen', True)
    
        
         # =================== Center Form =================== #
        window_height = 800
        window_width = 1030

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # kapag sa screen ko
        # x_cordinate = int((screen_width/2) - (window_width/2))
        # y_cordinate = int((screen_height/3) - (window_height/3))

        # kapag sa screen ni rey
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/4) - (window_height/4))
        
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        
        self.resizable(0,0)
        
        #==================================2 main frames top and bottom====================================
        
        self.top_frame = tk.Frame(master = self, width=1200, height=300, background="#F5F5F5")
        self.top_frame.pack(pady=30, padx=30, fill="both", expand=True)
        
        # self.top_frame.grid_rowconfigure(1, weight=1)
        self.top_frame.grid_columnconfigure(1, weight=1)
        
        self.top_frame.pack_propagate("false")

        self.bot_frame = tk.Frame(master = self, width=1200, height=200, background="#F5F5F5")
        self.bot_frame.pack(padx=30)

        self.bot_frame.grid_columnconfigure(1, weight=1)
        # self.bot_frame.grid_rowconfigure(1, weight=1)
        self.bot_frame.pack_propagate("false")

        #==================================3 top frames====================================

        self.myLabel = Label(self.top_frame, text="Parameters", bg="#F5F5F5", fg='#3B3D40', font=("Open Sans Semibold", 12))
        self.myLabel.grid(pady=5, padx=10, sticky='w')  
        
        # self.myLabel = customtkinter.CTkLabel(self.top_frame, 
        #                                       text="Hydroponics",
        #                                       bg_color="#F5F5F5",
        #                                       text_font=("Open Sans Semibold", 12),
        #                                       anchor="center",
        #                                       text_color="#3B3D40"
        #                                       )
        # self.myLabel.grid(pady=5, padx=10, sticky='w')  
        
        
        self.top_frame1 = tk.Frame(self.top_frame, width=300, height=300, bg="#FFFFFF")
        self.top_frame1.grid(row=3, column=0, padx=2, pady=4)
        self.top_frame1.pack_propagate("false")

        self.top_frame2 = tk.Frame(self.top_frame, width=300, height=300, bg="#FFFFFF")
        self.top_frame2.grid(row=3, column=1, padx=2, pady=4)
        self.top_frame2.pack_propagate("false")

        self.top_frame3 = tk.Frame(self.top_frame, width=300, height=300, bg="#FFFFFF")
        self.top_frame3.grid(row=3, column=2, padx=2, pady=4)
        self.top_frame3.pack_propagate("false")
        
        #================================== Temperature Sensor ====================================
        self.my_img = (Image.open("Images/celsius.png"))

        resized_image= self.my_img.resize((110,110))
        self.new_image= ImageTk.PhotoImage(resized_image)

        myLabel1 = Label(self.top_frame1, text=" \n" + " ", bg='#FFFFFF')
        myLabel1.pack()

        myLabel2= Label(self.top_frame1, image=self.new_image, height=170, width=170, bg='#FFFFFF')
        myLabel2.pack()

        #dito yung value na manggagaling sa sensor
        self.myLabel3 = Label(self.top_frame1, 
                              text="00.0 °C", 
                              font=("Open Sans Bold", 30), 
                              bg='#FFFFFF', 
                              fg='#3B3D40'
                              )
        self.myLabel3.pack()
        

        

        myLabel4 = Label(self.top_frame1, text="Temperature", font=("Open Sans Semibold", 10), bg='#FFFFFF', fg='#3B3D40')
        myLabel4.pack() 
        
        #================================== Water Level Sensor ====================================

        self.my_img_1 = (Image.open("Images/water-level.png"))

        resized_image_1= self.my_img_1.resize((110,110))
        self.new_image_1= ImageTk.PhotoImage(resized_image_1)

        myLabel1_2 = Label(self.top_frame2, text=" \n" + " ", bg='#FFFFFF')
        myLabel1_2.pack()

        myLabel2_2= Label(self.top_frame2, image=self.new_image_1, height=170, width=170, bg='#FFFFFF')
        myLabel2_2.pack()

        #dito yung value na manggagaling sa sensor
        self.myLabel3_2 = Label(self.top_frame2, text="100 %", font=("Open Sans Bold", 30), bg='#FFFFFF', fg='#3B3D40')
        self.myLabel3_2.pack()
        


        myLabel4_2 = Label(self.top_frame2, text="Water Level", font=("Open Sans Semibold", 10), bg='#FFFFFF', fg='#3B3D40')
        myLabel4_2.pack()

        #================================== TDS level sensor====================================

        my_img_2 = (Image.open("Images/meter.png"))

        resized_image_2= my_img_2.resize((110,110))
        self.new_image_2= ImageTk.PhotoImage(resized_image_2)

        myLabel1_3 = Label(self.top_frame3, text=" \n" + " ", bg='#FFFFFF')
        myLabel1_3.pack()

        myLabel2_3= Label(self.top_frame3, image=self.new_image_2, height=170, width=170, bg='#FFFFFF')
        myLabel2_3.pack()

        #dito yung value na manggagaling sa sensor
        self.myLabel3_3 = Label(self.top_frame3, text="0 PPM", font=("Open Sans Bold", 30), bg='#FFFFFF', fg='#3B3D40')
        self.myLabel3_3.pack()
        

        myLabel4_3 = Label(self.top_frame3, text="TDS Level", font=("Open Sans Semibold", 10), bg='#FFFFFF', fg='#3B3D40')
        myLabel4_3.pack()
        
        #==================================3 bottom frames====================================
        myLabel = Label(self.bot_frame, text="Switches", bg="#F5F5F5", fg='#3B3D40', font=("Open Sans Semibold", 12))
        myLabel.grid(pady=5, padx=10, sticky='w')

        self.bot_frame1 = tk.Frame(self.bot_frame, width=300, height=190, bg="#FFFFFF")
        self.bot_frame1.grid(row=3, column=0, padx=2, pady=4)
        self.bot_frame1.pack_propagate("false")

        self.bot_frame2 = tk.Frame(self.bot_frame, width=300, height=190, bg="#FFFFFF")
        self.bot_frame2.grid(row=3, column=1, padx=2, pady=4)
        self.bot_frame2.pack_propagate("false")

        self.bot_frame3 = tk.Frame(self.bot_frame, width=300, height=190, bg="#FFFFFF")
        self.bot_frame3.grid(row=3, column=2, padx=2, pady=4)
        self.bot_frame3.pack_propagate("false")
        
        #================================== Water Pump ====================================

        my_img_3 = (Image.open("Images/water-pump.png"))

        resized_image_3= my_img_3.resize((70,70))
        self.new_image_3= ImageTk.PhotoImage(resized_image_3)

        myLabel1 = Label(self.bot_frame1, text=" \n" + " \n", bg='#FFFFFF')
        myLabel1.pack(padx=25, pady=15, side=tk.LEFT)

        myLabel2= Label(self.bot_frame1, image=self.new_image_3, height=80, width=60, bg='#FFFFFF')
        myLabel2.pack(side=tk.LEFT)

        myLabel3 = Label(self.bot_frame1, text=" \n" + " \n", bg='#FFFFFF')
        myLabel3.pack()

        myLabel4 = Label(self.bot_frame1, text="Water Pump", font=("Open Sans Semibold", 10), bg='#FFFFFF', fg='#3B3D40')
        myLabel4.pack(pady=15)

        switch_1 = customtkinter.CTkSwitch(self.bot_frame1, text="")#eto yung switch pre
        switch_1.pack()

        #================================== Oxygen Pump ====================================

        my_img_4 = (Image.open("Images/oxygen.png"))

        resized_image_4= my_img_4.resize((70,70))
        self.new_image_4= ImageTk.PhotoImage(resized_image_4)

        myLabel1_2 = Label(self.bot_frame2, text=" \n" + " \n", bg='#FFFFFF')
        myLabel1_2.pack(padx=25, pady=15, side=tk.LEFT)

        myLabel2_2= Label(self.bot_frame2, image=self.new_image_4, height=80, width=60, bg='#FFFFFF')
        myLabel2_2.pack(side=tk.LEFT)

        myLabel3_2 = Label(self.bot_frame2, text=" \n" + " \n", bg='#FFFFFF')
        myLabel3_2.pack()

        myLabel4_2 = Label(self.bot_frame2, text="Oxygen Pump", font=("Open Sans Semibold", 10), bg='#FFFFFF', fg='#3B3D40')
        myLabel4_2.pack(pady=15)

        switch_2 = customtkinter.CTkSwitch(self.bot_frame2, text="")     #eto yung switch pre
        switch_2.pack()
        
        #================================== bottom frame 3 info====================================

        my_img_5 = (Image.open("Images/pump.png"))

        resized_image_5= my_img_5.resize((70,70))
        self.new_image_5= ImageTk.PhotoImage(resized_image_5)

        myLabel1_3 = Label(self.bot_frame3, text=" \n" + " \n", bg='#FFFFFF')
        myLabel1_3.pack(padx=25, pady=15, side=tk.LEFT)

        myLabel2_3= Label(self.bot_frame3, image=self.new_image_5, height=80, width=60, bg='#FFFFFF')
        myLabel2_3.pack(side=tk.LEFT)

        self.myLabel3_3 = Label(self.bot_frame3, text=" \n" + " \n", bg='#FFFFFF')
        self.myLabel3_3.pack()

        myLabel4_3 = Label(self.bot_frame3, text="Peristaltic Pump", font=("Open Sans Semibold", 10), bg='#FFFFFF', fg='#3B3D40')
        myLabel4_3.pack(pady=15)

        switch_3 = customtkinter.CTkSwitch(self.bot_frame3, text="")     #eto yung switch pre
        switch_3.pack()
        
if __name__ == "__main__":
    
    app = App()
    app.mainloop()
