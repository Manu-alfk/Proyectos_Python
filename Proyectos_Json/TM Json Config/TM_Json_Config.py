"""
1-tengo que leer un archivo json creado                   -h
2-tengo que modificar un archivo json creado              -h
3-tengo que añadir elementos a un archivo json creado     -h
4-tengo que borrar elementos de un archivo json creado    -h

5-tengo que crear un archivo json con python                      -h
    *crear una rchivo en una ruta especifica                      -h
    *copiar un archivo plantilla en otra ruta y cambiar nombre    -h
6-tengo que añadir contenido a ese nuevo archivo al momento de crearlo     -h
7-tengo que crear una libreria que tenga la plantilla de los datos que se escriviran el el archivo json -h                           
    *-crear una libreria que me reciva todos los datos de ese nuevo archivo json y los escriva -h
    *crear una libreria que reciva todos los archivos y carpetas de una carpeta  

8-abrir el explorador de archivos  -h
9-abrir un archivo json desde el explorador de archivos -h
    *obtener la direccion del path  -h
    *guardar esa path para futuros usos  
10-guardar archivo json usando el path -h
11-guardar archivo json usando explorado de archivos -h

12-crar carpetas usando python  -h
    *seleccionar carpetas y obtener la path -h
13-crear carpetas dentro de carpetas usando python  -h
    *seleccionar carpetas y obtener las diferentes path -h

14-crear interfaz en tkinter para resolver los primeros 4 temas -h
15-crear interfaz en tkinter para resoler los primeros 7 temas  -h
16-crear interfaz en tkinter para resoler los primeros 11 temas -h
17-crear interfaz en tkinter para resoler los primeros 13 temas -h

18-crear interfaz en tkinter para mostrar los datos del archivo json  -h
    *sin importar que este dentro del archivo, que la interfaz se adapte  -h

19-crear interfaz en tkinter para mostrar las carpetas que estan dentro de las carpetas
18-crear interfaz en tkinter para mostrar todo los datos dentro de un carpeta seleccionada
    *LAS CARPETAS, LOS ARCHIVOS de estas carpetas, etc
    
"""

import json, os, shutil
from os import path
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb

def mostrar_butons():
    b_crear_crapeta_escena.place(x=150,y=100,anchor="center") 
    b_crear_sub_carpeta.place(x=150,y=150,anchor="center")
    b_archivo_json.place(x=150,y=200,anchor="center")

def crear_carpeta_escena():
    #print("crear carpeta")
    ruta_dir = dame_ruta_dir()
    if os.path.isdir(os.path.join(ruta_dir)):
        #print("--  ",ruta_dir)
        en_carpeta.delete(0,100)
        en_carpeta.insert(0,ruta_dir)
        mostrar_carpet()
    #dame_num_sub_carpet()
    #pass

def dame_ruta_archivo():
    archivo = filedialog.askopenfilename(filetypes = (( "json_files .json" , "* .json " )))  
    return archivo

def dame_ruta_dir():
    ruta = filedialog.askdirectory()  
    return ruta

def mostrar_carpet():    
    ocultar_sub_carpet()
    en_carpeta.place(x=10,y=10)

    l_nom_carpet.place(x=10, y=50)
    en_nom_carpet.place(x=10, y=80)

    l_num.place(x=10,y=120)    
    en_num_sub.place(x=10, y=150)

    bu_num_sub.place(x=40, y=200)
    bu_carpet_cancel.place(x=120,y=200)
    
def ocultar_carpet():
    en_carpeta.place_forget()

    l_nom_carpet.place_forget()
    en_nom_carpet.place_forget()

    l_num.place_forget()
    en_num_sub.place_forget()

    bu_num_sub.place_forget()
    bu_carpet_cancel.place_forget()

    try:
        borrar_tabla()
    except:
        pass

def dame_num_sub_carpet():
    snum = en_num_sub.get()
    car_name = en_nom_carpet.get()
    if car_name !="":
        if snum!= "":
            try:
                inum = int(snum)
                if inum <10:                
                    crear_tabla(inum)
                else:
                    r = mb.showwarning("Error!!", "Has indicado un numero de sub carpetas demasiado grande")
            except:
                r = mb.showwarning("Error!!", "Debes escribir un numero de sub_carpetas")
        else:
            #poner una ventana de aviso
            r = mb.showwarning("Error!!","No has indicado el numero de las sub-carpetas") 
    else:
        #poner una ventana de aviso
        r = mb.showwarning("Error!!","No has indicado el nombre de la carpeta")
        #Label(root,text=r).pack()
        #pass

def crear_tabla(n_i=5):
    global tabla_sub_carpet
    rows =[] 
    for i in range(n_i):
        cols = []
        for j in range(1):                
            l=Label(fr_mu_datos,text="carpeta "+str(i))
            #l.grid(row=i, column=0)
            l.place(x=100,y=100+(i*30))
            cols.append(l)
            e = Entry(fr_mu_datos)
            e.place(x=180,y=100+(i*30))
            #e.grid(row=i,column=2)
            cols.append(e)       
        rows.append(cols)
    b = Button(fr_mu_datos, text="aceptar",command=aceptar_tabla)
    b.place(x=160,y=50)
    rows.append(b)
    b1 = Button(fr_mu_datos, text="Cancelar",command=borrar_tabla)
    b1.place(x=250,y=50)
    #b.grid(row=n_i,column=1)
    rows.append(b1)
    tabla_sub_carpet = rows

def aceptar_tabla():
    #tengo que imprimir todo y despues borrar
    global tabla_sub_carpet
    #print(len(tabla_sub_carpet))
    borrar=False
    for a in range(len(tabla_sub_carpet )):
        b = tabla_sub_carpet[a]
        if type(b) == list:#es el label y el entri           
            print(b[1])
            d=b[1].get()
            #print("**", d)
            if d != "":
                borrar =True
            else:
                borrar = False
                msg=""
                r = mb.showwarning("Carpeta"+str(a)+"!!", "Nombre de carpeta esta vacio")
                break
    if borrar:
        ruta=en_carpeta.get()
        name=en_nom_carpet.get()        
        crear_sub_carpet(ruta,name) 
        #r = mb.showwarning("Error!!", "Debes escribir un numero de sub_carpetas")
        
        n_ruta = ruta+"/"+name
        for a in range(len(tabla_sub_carpet)):
            b = tabla_sub_carpet[a]
            if type(b) == list:#es el label y el entri           
                #print(b[1])
                name = b[1].get()#esto es el nombre de la carpeta
                crear_sub_carpet(n_ruta, name)
                crear_archivos(n_ruta+"/"+name)
        #tengo que crear carpeta y subs carpeta 
        borrar_tabla(True)
        ocultar_carpet()

def borrar_tabla(mode):
    global tabla_sub_carpet
    global tabla_t_ext
    if mode:
        tabla=tabla_sub_carpet
    else:
        tabla= tabla_t_ext
    #print(len(tabla))   
    for a in tabla:
        if type(a) ==list:
            for b in a:
                #print(b)
                b.destroy()            
        else:
            #print(a)           
            a.destroy()

def sub_carpeta():
    #print("crear sub carpeta")
    #tengo que abrir el explorador
    ruta_dir = dame_ruta_dir()
    if os.path.isdir(os.path.join(ruta_dir)):
        #print("--  ",ruta_dir)
        en_ruta_carpet.delete(0,100)
        en_ruta_carpet.insert(0,ruta_dir)
        mostrar_sub_carpet()    

def mostrar_sub_carpet():
    ocultar_carpet()
    en_ruta_carpet.place(x=10,y=10)
    l_sub_carpet.place(x=10, y=40)
    en_sub_carpet.place(x=10, y=70)
    bu_sub_carpet_acept.place(x= 10, y = 100)
    bu_sub_carpet_cancel.place(x=70,y=100)

def aceptar_sub_carpet():
    name = en_sub_carpet.get()
    if name != "":
        ruta=en_ruta_carpet.get()
        #print("creando carpeta")
        crear_sub_carpet(ruta, name)
        crear_archivos(ruta + "/" + name)
        ocultar_sub_carpet()
        #creamos la carpeta

def crear_sub_carpet(ruta, name):
    try:
        os.makedirs(ruta+"/"+name)
    except:
        r = mb.showwarning("Error!!", "Carpeta existente en el directorio indicado")

def ocultar_sub_carpet():
    en_ruta_carpet.place_forget()
    l_sub_carpet.place_forget()
    en_sub_carpet.place_forget()
    bu_sub_carpet_acept.place_forget()
    bu_sub_carpet_cancel.place_forget()

def crear_archivos(ruta):
    #tengo que crear los archivos de
    archivos_idioma= [
        "Español.json",
        "English.json",
        "Aleman.json",
        "Italiano.json",
        "Portuges.json",
        "Ruso.json",
        "Chino.json",
        "Japones.json"
    ]

    for a in archivos_idioma:
        shutil.copy("prueba.json",ruta+"\\"+a)

def mostrar_archivos1():
    b_json_aceptar.place(x=50, y=10)
    b_json_cancelar.place(x=150,y=10)

    t_archivo_original.place(x=10,y=40)
    en_json.place(x=10,y=10)
    #t_archivo1.place(x=400,y=40)

def ocultar_archivos1():
    b_json_aceptar.place_forget()
    b_json_cancelar.place_forget()

    t_archivo_original.place_forget()
    t_archivo_malo.place_forget()
    en_json.place_forget()

def editar_archivo_json():
    #print("archivo")
    archivo = dame_ruta_archivo()
    if os.path.isfile(os.path.join(archivo)):
        mostrar_archivos1()
        print(archivo)
        en_json.delete(0,100)
        en_json.insert(0,archivo)
        dame_datos(archivo,True)
    #pass

def dame_datos(ruta,mode):
    global archivo_json
    with open(ruta) as contenido:
        datos = json.load(contenido)
        archivo_json=datos
        if mode:
            archivo=t_archivo_original
        else:
            archivo=t_archivo_malo
        #print(datos.get("num_idioma",""))
        archivo.delete("1.0", END)
        #print(type(datos))
        if type(datos) ==dict:
            archivo.insert("insert", "{" + "\n")
            cierro="}"
        elif type(datos) == list:
            archivo.insert("insert", "[" + "\n")
            cierro="]"
        for n_datos in datos:
            #print(type(n_datos))
            data = datos.get(n_datos)
            #print(type(data))            
            if type(data) == list:
                #print(n_datos, "*")
                archivo.insert("insert", "  " + str(n_datos) + ":[ " + "\n")                
                #tengo que crear un boton y un Text
                crear_t_ext(str(n_datos))
                for n_data in data:
                    #print("  --   ",n_data)
                    archivo.insert("insert", "    " + str(n_data) + ",\n")
                    añadir_t_ext(n_data)
                archivo.delete("end-3c",END)
                archivo.insert("insert","\n"+"  "+"]" +",\n")                           
                #tengo que crear un boton y un Text
                #crear_t_ext(str(n_data))
            else:
                #print(n_datos, "- * -", str(datos.get(n_datos)))                
                archivo.insert("insert", "  " + n_datos + ": " + str(datos.get(n_datos)) + ",\n")                           
        archivo.delete("end-3c", END)
        archivo.insert("insert","\n"+ cierro + "\n")
        mostrar_butons_t_editar()
        #datos.close()
        #t_archivo1.delete("1.0", END)
        #t_archivo1.insert("insert",datos)
    #print("")

def añadir_t_ext(msg):
    global tabla_t_ext
    #tengo que saber cual text modificar    
    ids=len(tabla_t_ext)-1
    #print("+-- ",ids) 
    tabla = tabla_t_ext[ids]   
    tabla[1].insert("insert",msg+"\n")

def crear_t_ext(texto):  #esto agrega un boton a la lista de botones
    global tabla_t_ext
    tabla = []
    ids=len(tabla_t_ext)
    #print(ids)
    b = Button(fr_mu_datos, text="Editar:\n "+texto, command=lambda:mostrar_t_editar(ids)) 
    t = Text(fr_mu_datos, padx=1, pady=1, height=28, width=30)
    tabla.append(b)
    tabla.append(t)
    tabla_t_ext.append(tabla)

def mostrar_butons_t_editar():
    global tabla_t_ext
    #for a in tabla_t_ext:
    for a in range(len(tabla_t_ext)):
        tabla=tabla_t_ext[a]
        tabla[0].place(x=270,y=100+(a*50))
        #tabla[1].place(x=400,y=100+(a*100))
    pass

def mostrar_t_editar(ids):
    global tabla_t_ext
    #for a in tabla_t_ext:
    ocultar_t_editar()
    #mostrar_butons_t_editar()
    tabla=tabla_t_ext[ids]
    tabla[1].place(x=400,y=10+(ids*1))
    #print(ids)
    pass

def ocultar_t_editar():
    global tabla_t_ext
    #for a in tabla_t_ext:
    for a in range(len(tabla_t_ext)):
        tabla=tabla_t_ext[a]
        tabla[1].place_forget()           

def json_aceptar():
    global tabla_t_ext
    global archivo_json
    global datos_t_ext

    datos=[]    
    for a in range(len(tabla_t_ext)):
        tabla=tabla_t_ext[a]
        #tabla[0].place(x=270,y=100+(a*50))
        datos.append(dame_t_sin_(tabla[1]))

    nun=0
    for a in archivo_json:
        data = archivo_json.get(a)
        if type(data)==list:
            archivo_json[a] = datos[nun]
            nun+=1
    
    #debo de guardar el archivo
    ruta=en_json.get()
    escribe_json(archivo_json,ruta)

    t_archivo_original.delete("1.0", END)
    t_archivo_malo.delete("1.0", END)
    ocultar_archivos1()

    ocultar_t_editar()
    borrar_tabla(False)

    tabla_t_ext.clear()   
    datos_t_ext.clear()
    archivo_json.clear()
    #pass

def escribe_json(datos,ruta):
    n_datos = json.dumps(datos)
    #print(n_datos)

    with open(ruta, "w") as f:
        json.dump(datos,f)

def dame_t_sin_(textos):
    #datos = textos.get("1.0",END)
    lineas=[]
    for linea in textos.get('1.0', 'end-1c').splitlines():
        # Iterate lines
        if linea:
            #print('path: {}'.format(linea))
            lineas.append(linea)
    return lineas

def json_cancelar(): 
    global tabla_t_ext  
    global datos_t_ext
    global archivo_json   
    t_archivo_original.delete("1.0", END)
    t_archivo_malo.delete("1.0", END)
    ocultar_archivos1()
    borrar_tabla(False)

    tabla_t_ext.clear()   
    datos_t_ext.clear()
    archivo_json.clear()

r=Tk()
#r.attributes('-topmost', True)
r.title("TM Json Config")
fr_opc=Frame(r)
fr_opc.config(width=300,height=300,bg="black")
fr_opc.grid(row=0,column=0,rowspan=4,columnspan=4)
fr_opc.propagate = "false"
fr_maopc=Frame(r)
fr_maopc.config(width=300,height=300,bg="gray")
fr_maopc.grid(row=4,column=0,rowspan=4,columnspan=4)
fr_maopc.propagate = "false"
fr_aun_mopc=Frame(r)
fr_aun_mopc.config(width=300,height=168,bg="green")
fr_aun_mopc.grid(row=8,column=0,rowspan=4,columnspan=4)
fr_aun_mopc.propagate="false"

fr_datos=Frame(r)
fr_datos.config(width=800,height=100,bg="gray")
fr_datos.grid(row=0,column=4,rowspan=1,columnspan=1)
fr_datos.propagate="false"
fr_mu_datos=Frame(r)
fr_mu_datos.config(width=800,height=500,bg="purple")
fr_mu_datos.grid(row=1,column=4,rowspan=4,columnspan=4)
fr_mu_datos.propagate="false"
fr_mas_datos=Frame(r)
fr_mas_datos.config(width=800,height=168,bg="green")
fr_mas_datos.grid(row=8,column=4,rowspan=4,columnspan=4)
fr_mas_datos.propagate="false"

b_crear_crapeta_escena=Button(fr_opc,text="Crear Carpeta de Escena",font=20,command=crear_carpeta_escena)
b_crear_sub_carpeta=Button(fr_opc,text="Crear Sub Carpeta",font=20,command=sub_carpeta)
b_archivo_json = Button(fr_opc, text="Editar Archivo Json",font=20, command=editar_archivo_json)

mostrar_butons()
 
fr_carpet = Frame(fr_mas_datos)
fr_carpet.config(width=200, height=300, bg="black")

#mostrare la ruta de la carpeta
ruta_carpeta=StringVar()
en_carpeta=Entry(fr_maopc,textvariable=ruta_carpeta,width=40)

#tengo que pedir un nombre
l_nom_carpet = Label(fr_maopc, text="Nombre de la carpeta")
nom_carpet=StringVar()
en_nom_carpet = Entry(fr_maopc, textvariable=nom_carpet)

#tengo que pedir un numero
l_num=Label(fr_maopc,text="Numero de sub crapetas")
num_sub_carpet=StringVar()
en_num_sub = Entry(fr_maopc, textvariable=num_sub_carpet)
#boton de aceptar
bu_num_sub=Button(fr_maopc,text="Aceptar",command=dame_num_sub_carpet,font=20)
#boton de cancel
bu_carpet_cancel =Button(fr_maopc,text="Cancelar",command=ocultar_carpet,font=20)

ruta_carpet=StringVar()
en_ruta_carpet=Entry (fr_maopc,textvariable=ruta_carpet,width=40)
l_sub_carpet=Label(fr_maopc,text="Nombre de sub carpeta")
name_sub_carpet = StringVar()
en_sub_carpet = Entry(fr_maopc, textvariable=name_sub_carpet)
bu_sub_carpet_acept=Button(fr_maopc,text="Aceptar",command=aceptar_sub_carpet)
bu_sub_carpet_cancel=Button(fr_maopc,text="Cancelar",command=ocultar_sub_carpet)
#la tabla donde se motraran las opciones de sub carpet
tabla_sub_carpet = []

#tengo escribir el archivo
b_json_aceptar=Button(fr_mu_datos,text="Aceptar",command=json_aceptar)
b_json_cancelar = Button(fr_mu_datos, text="Cancelar", command=json_cancelar)
#donde se guardara la ruta del archivo 
ruta_json=StringVar()
en_json= Entry(fr_maopc,textvariable=ruta_json,width=40)
t_archivo_original=Text(fr_mu_datos, padx=1, pady=1, height=28,  width=30 )
t_archivo_malo=Text(fr_mu_datos, padx=1, pady=1, height=28,  width=30 )

#las tabla donde se mostraran las opciones de archivo
tabla_t_ext = []
datos_t_ext=[]
archivo_json = []

r=mainloop()



















