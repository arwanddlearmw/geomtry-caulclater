import turtle
import tkinter as tk
import customtkinter as ctk
import tkinter.ttk as ttk
import math

#the frames
class App:
    def __init__(self):
        self.root = ctk.CTk()

        self.menu = ctk.CTkFrame(self.root)
        self.menu.grid(row=0,column=0)

        self.canva_frame = tk.Frame(self.root,width=720,height=520)
        self.canva_frame.grid(row=1,column=0)

        self.canva = tk.Canvas(self.canva_frame)
        self.canva.grid(row=0,column=0)

        screen = turtle.TurtleScreen(self.canva)
        self.turtle = turtle.RawTurtle(screen)

        self.input = ctk.CTkFrame(self.root)
        self.input.grid(row=2,column=0)

        self.output = tk.Frame(self.root)
        self.output.grid(row=3,column=0)

        self.coondrite = []
#core
def circle_area(raduis):
    area = math.pi * ( (raduis / 2) ** 2)
    return area
def circle_permiter(raduis):
    perimiter = math.pi * raduis
    return perimiter
def square_rectangle (polygons_1 , polygons_2 = False):
    rectangle = polygons_1 * polygons_2
    return rectangle
def triangle_size(hight , base):
    size = hight * base * 1/2
    return(size)
def triangle_perimeter(polygon_1,polygon_2,polygon_3 = False):
    perimeter = polygon_1 + polygon_2 + polygon_3
    return perimeter
def pethagorths(hight , wietgh):
    entry_3 = int (math.sqrt((hight**2)+(wietgh**2)) )
    return entry_3

#drawing the geomtric looks
def event_triangle(self,event):
    if event.x == self.coondrite[0][0] and event.y == self.coondrite[0][1] :
        self.coondrite[0] = event.x ,event.y
        triangle_draw(self.coondrite,self)
    elif event.x == self.coondrite[1][0] and event.y == self.coondrite[1][1]:
        self.coondrite[1] = event.x ,event.y
        triangle_draw(self.coondrite,self)
    elif event.x == self.coondrite[2][0] and event.y == self.coondrite[2][1]:
        self.coondrite[2] = event.x , event.y
        triangle_draw(self.coondrite,self)
def polygons_draw(entry_1,entry_2,self):
    self.turtle.ht()
    entry_1 = int(entry_1 or 1)
    entry_2 = int(entry_2 or 1)
    self.turtle.screen.tracer(0)
    self.turtle.reset()
    for x in range(2):
        self.turtle.fd(entry_1)
        self.turtle.lt(90)
        self.turtle.fd(entry_2)
        self.turtle.lt(90)
    self.turtle.screen.update()

def circle_draw(entry,self):
    self.turtle.ht()
    self.turtle.screen.tracer(0)
    entry = int(entry)
    self.turtle.reset()
    self.turtle.circle (circle_permiter (entry))
    self.turtle.lt(90)
    self.turtle.fd(circle_permiter(entry))
    self.turtle.screen.update()

def coondrite_triangle(self,wieght,hight,entry_2):
    
    self.Coordinate = [
        [0,0],
        [int(wieght or 10),0],
        [int(entry_2 or 10),int(hight or 10)],
        [0,0]
        ]
    triangle_draw(self.Coordinate,self)
def triangle_draw (coorndition,  self):

    self.turtle.ht()
    self.turtle.screen.tracer(0)
    self.turtle.reset()
    self.turtle.goto (*coorndition[0])
    self.turtle.goto (*coorndition[1])
    self.turtle.goto (*coorndition[2])
    self.turtle.goto (*coorndition[0])
    self.turtle.screen.update()

#the ui
def clean_frame (frame):
    for widget in frame.winfo_children():
        widget.destroy()
def triangle_gui_core(self,hight,wietgh,entry_2):
    hight = int(hight)
    wietgh = int(wietgh)
    entry_2 = int(entry_2 or 0)
    clean_frame(self.output)
    ctk.CTkLabel(self.output,text=f"size : {triangle_size(hight,wietgh)}").grid(row=0,column=0)
    if entry_2 == 0 or entry_2 == wietgh:
        ctk.CTkLabel(self.output,text=f"permiters : {triangle_perimeter( abs(hight),abs(wietgh),pethagorths(abs( hight),abs(wietgh) ) )}").grid(row=1,column=0)
    else :
        left = math.sqrt(entry_2**2 + hight**2)
        right = math.sqrt((wietgh - entry_2)**2 + hight**2)
        ctk.CTkLabel(self.output , text=f"permiters : {triangle_perimeter(left,abs(wietgh),right)}").grid(row=1,column=0)
def triangle_gui(self):
    clean_frame(self.input)
    clean_frame(self.output)
    ctk.CTkLabel(self.input,text="hight :").grid(row="1",column="0")
    ctk.CTkLabel(self.input,text="wieght_half :").grid(row="2",column="0")
    ctk.CTkLabel(self.input,text="entry_2 :").grid(row="3",column="0")
    hight = ctk.CTkEntry(self.input)
    hight.grid(row="1",column="1",)
    wieght = ctk.CTkEntry(self.input)
    wieght.grid(row="2",column="1")
    entry_2 = ctk.CTkEntry(self.input)
    entry_2.grid(row="3",column="1")
    
    self.root.bind("<Return>", lambda event: coondrite_triangle(self ,hight.get() , wieght.get() , entry_2.get() ))
    self.root.bind("<Return>",lambda event: triangle_gui_core(self , hight.get() , wieght.get() , entry_2.get()),add="+")

def circle_gui_core(self,raduis):
    raduis = int(raduis)
    clean_frame(self.output)
    ctk.CTkLabel(self.output,text=f"the area : {circle_area(raduis)}").grid(row=0,column=0)
    ctk.CTkLabel(self.output, text=f"the permiter : {circle_permiter(raduis)}").grid(row=1,column=0)
def circle_gui(self):
    clean_frame(self.input)
    clean_frame(self.output)
    ctk.CTkLabel(self.input,text = "raduis input(not a half!):").grid(row=0,column=0)
    raduis = ctk.CTkEntry(self.input)
    raduis.grid(row=0,column=1)
    self.root.bind("<Return>",lambda event: circle_draw(raduis.get() , self))
    self.root.bind("<Return>",lambda event: circle_gui_core( self ,raduis.get() ),add="+")

def square_rectangle_gui_core(polygon_1,polygon_2,self):
    polygon_1 = int(polygon_1)
    polygon_2 = int(polygon_2)
    clean_frame(self.output)
    ctk.CTkLabel(self.output,text=f"the area : {square_rectangle(polygon_1 , polygon_2)}").grid(row=0,column=0)
def square_rectangle_gui(self):
    clean_frame(self.input)
    clean_frame(self.output)
    ctk.CTkLabel(self.input,text="polygon first :").grid(row=0,column=0)
    ctk.CTkLabel(self.input,text="polygon second :").grid(row=1,column=0)
    polygon_1 = tk.Entry(self.input)
    polygon_1.grid(row=0,column=1)
    polygon_2 = tk.Entry(self.input)
    polygon_2.grid(row=1,column=1)
    self.root.bind("<Return>",lambda event:square_rectangle_gui_core(polygon_1.get(),polygon_2.get(),self))
    self.root.bind("<Return>",lambda event:polygons_draw(polygon_1.get() , polygon_2.get() , self),add="+")

def statement_user(geomtric,self):
    match geomtric:
        case "Circle":
            circle_gui(self)
        case "Square/Rectangle":
            square_rectangle_gui(self)
        case "Triangle":
            triangle_gui(self)
def choose_geometric(self):
    combo_box = ctk.CTkComboBox(
    self.menu,
    values=["Circle", "Square/Rectangle", "Triangle"],
    state="readonly",
    command=lambda values: statement_user(values,self)
)
    combo_box.pack(pady=5)

#main
def main():


    self = App()
    ctk.set_appearance_mode("light")
    scroll_y = tk.Scrollbar(self.canva_frame, orient="vertical", command=self.canva.yview)
    scroll_x = tk.Scrollbar(self.canva_frame, orient="horizontal", command=self.canva.xview)
    self.canva.configure(
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )
    scroll_y.grid(row=0,column=1, sticky="ns")
    scroll_x.grid(row=1,column=0,sticky="ew")
    self.canva.configure(scrollregion=(-2000,-2000, 2000, 2000))
    choose_geometric(self)
    self.root.mainloop()

main()
