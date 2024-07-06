#Version realizada despues de la fecha limite de entrega de la prueba, con mas tiempo y menos presion

#===================Librerias========================
import os
import time
from datetime import datetime
#====================================================
#===================Funciones========================

#función_menu_1
def reservar_habitacion(piso,room,nombre,apellido,rut,fecha_entrada,fecha_salida):
    global id
    global ventas_diarias
    valor_diario = 0
    number_room=str(piso)+str(room)
    room_id = int(number_room)
    if habitaciones_reservadas[piso-1][room-1]=="Reservado":
        print("Lo sentimos, la habitación ya se encuentra reservada ")
        time.sleep(5) # informacion se muestra en pantalla por 5 segundos y vuelve al menu
    else:    
        if piso == 5:
            ventas_diarias+= 100000
            valor_diario = 100000
        elif piso == 4:
            ventas_diarias+= 60000
            valor_diario = 60000
        else:
            ventas_diarias+=30000
            valor_diario = 30000
        hotel[id] = {"room":room_id, "estado": "Reservado", "valor_diario": valor_diario, "nombre": nombre, "apellido": apellido, "rut": rut, "fecha_entrada": fecha_entrada,"fecha_salida": fecha_salida }
        habitaciones_reservadas[piso-1][room-1]="Reservado"
        print(f"La Habitación ha sido reservado correctamente, su codigo de reserva es {room_id}")
        id +=1
        time.sleep(5) # informacion se muestra en pantalla por 5 segundos y vuelve al menu

#Número de habitación, estado de reserva, valor diario de la 
#reserva, nombre, apellido, rut, fecha:hora de entrada y fecha:hora de salida.


#función_menu_2
def buscar_reserva(codigo):
    num_piso = int(codigo[0])
    num_habitacion = int(codigo[1])
    indice=int(codigo)
    if habitaciones_reservadas[num_piso-1][num_habitacion-1]=="Reservado":
        print(f"La reserva:{codigo}, pertenecece a la habitación {num_habitacion} ubicada en piso {num_piso}.")
        time.sleep(5) # informacion se muestra en pantalla por 5 segundos y vuelve al menu
    else:
        print(f"No hemos encontrado datos validos para la reserva indicada, favor intente nuevamente ")
        time.sleep(5) # informacion se muestra en pantalla por 5 segundos y vuelve al menu  

#función_menu_3
def estado_actual():
    for estado_actual in habitaciones_reservadas:
        print(estado_actual)
    time.sleep(10) # informacion se muestra en pantalla por 10 segundos y vuelve al menu

#función_menu_4
def total_ingresos():
    print(f"El total de ingresos del dia {fecha}, es ${ventas_diarias}")
    time.sleep(5) # informacion se muestra en pantalla por 5 segundos y vuelve al menu
#función_menu_5
def exportar_registros():
    with open(f"Reserva_Habitaciones_{fecha}.csv", "w", newline='') as file:
        file.write("numero_habitacion,estado,valor_diario,nombre,apellido,rut,fecha_entrada,fecha_salida\n")
        for x in hotel:
            file.write(f"{hotel[x]["room"]},{hotel[x]["estado"]},{hotel[x]["valor_diario"]},{hotel[x]["nombre"]},{hotel[x]["apellido"]},{hotel[x]["rut"]},{hotel[x]["fecha_entrada"]},{hotel[x]["fecha_salida"]}\n")
    
#====================================================
#===================Variables========================
validador=True
ventas_diarias = 0
id = 0
fecha=datetime.now().strftime('%d-%m-%Y')
hotel={}
habitaciones_reservadas=[
    ["Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible"],
    ["Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible"],
    ["Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible"],
    ["Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible"],
    ["Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible"],
]

#====================================================
#===================Menu=============================
while validador:
    try:
        print("\n")
        print("Ingrese la opcion deseada ")
        print("\n")
        print("1. Reservar Habitación ")
        print("2. Buscar Habitación ")
        print("3. Ver estado de habitaciones ")
        print("4. Calcular el total de ventas del día ")
        print("5. Guardar archivo CSV ")
        print("6. Salir ")
        print("\n")
        opcion=(int(input()))
        match opcion:
            case 1:
                os.system("cls")
                print("Reserva de Habitación ")
                print("\n")
                piso=(int(input("Ingrese el piso en donde se hospedara el huesped (entre 1 y 5):  ")))
                room=(int(input(f"Ingrese la habitacion asignada en el piso {piso} (entre 1 y 8):  ")))
                nombre=input("Ingrese el nombre del huesped: ").title()
                apellido=input("Ingrese el apellido del huesped: ").title()
                rut=input("Ingrese el rut del huesped: ")
                fecha_entrada=fecha
                fecha_salida=input("Ingrese la fecha de salida de su habitacion (formato dd-mm-aaaa): ")
                reservar_habitacion(piso,room,nombre,apellido,rut,fecha_entrada,fecha_salida)
            case 2:
                os.system("cls")
                print("Información de Habitación por código ")
                print("\n")
                codigo=(input("Ingrese el codigo de reserva:  "))
                buscar_reserva(codigo) 
            case 3:
                os.system("cls")
                print("A continuación te mostramos el estado actual de ocupación del Hotel ")
                print("\n")
                print("Habitaciones")
                estado_actual()
            case 4:
                os.system("cls")
                total_ingresos()
            case 5:
                os.system("cls")
                exportar_registros()
                print("Exportando Registros ")
                time.sleep(3) # informacion se muestra en pantalla por 3 segundos y vuelve al menu
            case 6:
                os.system("cls")
                print("Gracias por preferir Hotel DuocUC, Adios. ")
                validador = False
                time.sleep(3)  # informacion se muestra en pantalla por 3 segundos y vuelve al menu
            case _:
                os.system("cls")
                print("Opcion del menú invalido, Intente Nuevamente")   
            
    except ValueError:
        os.system("cls")
        print("Ha ingresado un dato no valido, favor reintente")
        time.sleep(3) # informacion se muestra en pantalla por 3 segundos y vuelve al menu
    except IndexError:
        os.system("cls")
        print("Ha ingresado un número de habitación no valida, favor reintente")
        time.sleep(5) # informacion se muestra en pantalla por 5 segundos y vuelve al menu  
#====================================================