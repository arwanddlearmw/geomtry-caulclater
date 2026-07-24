import turtle
import tkinter as tk
import tkinter.ttk as ttk
import math
#the frames
class App:
    def __init__(self,root):
        self.menu = tk.Frame(root)
        self.menu.grid(row=0,column=0)

        self.canva_frame = tk.Frame(root)
        self.canva_frame.grid(row=1,column=0)

        self.canva = tk.Canvas(self.canva_frame)
        self.canva.pack()
  
        screen = turtle.TurtleScreen(self.canva)
        self.turtle = turtle.RawTurtle(screen)

        self.input = tk.Frame(root)
        self.input.grid(row=2,column=0)

        self.output = tk.Frame(root)
        self.output.grid(row=3,column=0)
#the core
def circle_area(raduis):
    area = math.pi * ( (raduis / 2) ** 2)
    return area
def circle_permiter(raduis):
    perimiter = math.pi * raduis
    return perimiter

def regular_polygon (polygons_1 , polygons_2 = False):
    rectangle = polygons_1 * polygons_2
    return rectangle

def triangle_size(hight , base):
    size = hight * base * 1/2
    return(size)

def triangle_perimeter(polygon_1,polygon_2,polygon_3 = False):

    perimeter = polygon_1 + polygon_2 + polygon_3
    return perimeter

def pethagorths(hight , wietgh_half):
    entry_3 = int (math.sqrt((hight**2)+(wietgh_half**2)) )
    return entry_3
#drawing the geomtric looks
def polygons_draw(entry_1,entry_2,self,polygons):
    entry_1 = int(entry_1 or 1)
    entry_2 = int(entry_2 or 1)
    polygons = int(polygons or 4)
    self.turtle.reset()
    for x in range(polygons):
        self.turtle.fd(entry_1)
        self.turtle.lt(360 / polygons)
        self.turtle.fd(entry_2)
        self.turtle.lt(360 / polygons)

def circle_draw(entry,self):
    entry = int(entry)
    self.turtle.reset()
    self.turtle.circle (circle_permiter(entry))
    self.turtle.lt(90)
    self.turtle.fd(circle_permiter(entry))
def triangle_draw (hight , wietgh ,  self , entry_2):
    hight = int(hight)
    wietgh = int(wietgh)
    entry_2 = int(entry_2 or 0 )

    self.turtle.reset()
    self.turtle.goto (0,0)
    self.turtle.goto (wietgh , 0)

    self.turtle.goto (entry_2,hight)
    self.turtle.goto (0,0)
#the ui
def clean_frame (frame):
    for widget in frame.winfo_children():
        widget.destroy()

def triangle_gui_core(self,hight,wietgh,entry_2):
    hight = int(hight)
    wietgh = int(wietgh)
    entry_2 = int(entry_2 or 0)

    clean_frame(self.output)
    tk.Label(self.output,text=f"size : {triangle_size(hight,wietgh)}").grid(row=0,column=0)
    if entry_2 == 0 or entry_2 == wietgh:
        tk.Label(self.output,text=f"permiters : {triangle_perimeter( abs(hight),abs(wietgh),pethagorths(abs( hight),abs(wietgh) ) )}").grid(row=1,column=0)
    else :
        entry_3 = wietgh - (entry_2 - hight)
        tk.Label(self.output , text=f"permiters : {triangle_perimeter(abs(entry_2),abs(wietgh),abs(entry_3))}").grid(row=1,column=0)
def triangle_gui(self,root):
    clean_frame(self.input)

    tk.Label(self.input,text="hight :").grid(row="1",column="0")
    tk.Label(self.input,text="wieght_half :").grid(row="2",column="0")
    tk.Label(self.input,text="entry_2 :").grid(row="3",column="0")
    hight = tk.Entry(self.input)
    hight.grid(row="1",column="1",)
    wieght = tk.Entry(self.input)
    wieght.grid(row="2",column="1")
    entry_2 = tk.Entry(self.input)
    entry_2.grid(row="3",column="1")
    root.bind("<Return>", lambda event: triangle_draw(hight.get(),wieght.get(), self , entry_2.get()) )
    root.bind("<Return>",lambda event: triangle_gui_core(self , hight.get() , wieght.get() , entry_2.get()),add="+")

def circle_gui_core(self,raduis):
    raduis = int(raduis)
    clean_frame(self.output)
    tk.Label(self.output,text=f"the area : {circle_area(raduis)}").grid(row=0,column=0)
    tk.Label(self.output, text=f"the permiter : {circle_permiter(raduis)}").grid(row=1,column=0)

def circle_gui(self,root):
    clean_frame(self.input)


    tk.Label(self.input,text = "raduis input(not a half!):").grid(row=0,column=0)
    raduis = tk.Entry(self.input)
    raduis.grid(row=0,column=1)

    root.bind("<Return>",lambda event: circle_draw(raduis.get() , self))

    root.bind("<Return>",lambda event: circle_gui_core( self ,raduis.get() ),add="+")
def square_rectangle_gui_core(polygon_1,polygon_2,self):
    polygon_1 = int(polygon_1)
    polygon_2 = int(polygon_2)
    clean_frame(self.output)

    tk.Label(self.output,text=f"the area : {regular_polygon(polygon_1 , polygon_2)}").grid(row=0,column=0)


def square_rectangle_gui(self,root):

    clean_frame(self.input)

    tk.Label(self.input,text="polygon first :").grid(row=0,column=0)
    tk.Label(self.input,text="polygon second :").grid(row=1,column=0)
    polygon_1 = tk.Entry(self.input)
    polygon_1.grid(row=0,column=1)
    polygon_2 = tk.Entry(self.input)
    polygon_2.grid(row=1,column=1)

    root.bind("<Return>",lambda event:square_rectangle_gui_core(polygon_1.get(),polygon_2.get(),self))
    root.bind("<Return>",lambda event:polygons_draw(polygon_1.get() , polygon_2.get() , self,4),add="+")
def statement_user(geomtric,self,root):
    match geomtric:
        case "Circle":
            circle_gui(self,root)
        case "Square/Rectangle":
            square_rectangle_gui(self,root)
        case "Triangle":
            triangle_gui(self,root)
def choose_geometric(self,root):
    combo_box = ttk.Combobox(
    self.menu,
    values=["Circle", "Square/Rectangle", "Triangle"],
    state="readonly"
)
    combo_box.pack(pady=5)

    combo_box.bind("<<ComboboxSelected>>", lambda event:statement_user(combo_box.get(),self,root))

#main
def main():
    root = tk.Tk()
    root.title("drawing :3")
    self = App(root)

    choose_geometric(self,root)

    root.mainloop()
main()