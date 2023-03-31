from tkinter import *

root=Tk()
root.geometry("450x450")
root.title("Fabiel Tonala")
x= StringVar
c1=StringVar()
c2=StringVar()
c3=StringVar()
ventanaPrin=Frame(root,bg="#FFFFFF")
ventanaPrin.pack(fill="both", expand=1)

def cambiar():
    
   print("El cogigo hexadecimal que ingresaste")
   print("#"+c1.get()+c2.get()+c3.get())
   x=c1.get()+c2.get()+c3.get()
    
   if len(x)>6:
      B.config(text=f'Introdujiste mas de \n 6 digitos',bg="#FFFFFF")

   elif len(x)<6:
      B.config(text=f'Introdujiste menos de \n 6 digitos',bg="#FFFFFF")
    
   else: 
      ventanaPrin.config(bg=("#"+x))
      B.config(text="",bg=("#"+x))


titulo=Label(ventanaPrin,text="COLORES",bg="#FFFFFF",font=("Roboto",18))
titulo.grid(row=1,column=2,padx=5,pady=5)

red=Label(ventanaPrin,text="Red",bg="#FFFFFF",font=("Roboto",18))
red.grid(row=3,column=1,padx=5,pady=5)

color1=Entry(ventanaPrin,textvariable=c1,font=("Roboto",10))
color1.grid(row=3,column=2,padx=5,pady=5)

Green=Label(ventanaPrin,text="Green",bg="#FFFFFF",font=("Roboto",20))
Green.grid(row=6,column=1,padx=5,pady=5)

color2=Entry(ventanaPrin,textvariable=c2,bg="#FFFFFF",font=("Roboto",10))
color2.grid(row=6,column=2,padx=5,pady=5)

Blue=Label(ventanaPrin,text="Blue",bg="#FFFFFF",font=("Roboto",20))
Blue.grid(row=9,column=1,padx=5,pady=5)

color3=Entry(ventanaPrin,textvariable=c3,font=("Roboto",10))
color3.grid(row=9,column=2,padx=5,pady=5)

CambiarColor=Button(ventanaPrin,text="Cambiar color",bg="#FFFFFF",font=("Roboto",15),command=cambiar)
CambiarColor.grid(row=13,column=2,padx=5,pady=5)

B = Label(ventanaPrin, text="",bg="#FFFFFF",font=("Roboto",15))
B.grid(row=15,column=2,padx=10,pady=10)

root.mainloop()