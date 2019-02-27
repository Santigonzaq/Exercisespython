from datetime import datetime as dt
from datetime import timedelta as td
from dateutil.relativedelta import relativedelta as rd
import locale
locale.setlocale(locale.LC_ALL,"Spanish_Spain.1252")
formato="%d/%m/%y  - %I:%m:%p"
alterno = "%Y-%m-%d"
print("----------------CLINICA LA ESPERANZA------------------")
print("Hoy es: "+str(dt.today().strftime(formato)))
print("----------------------------------------------------------------------")
nombre=str(input("Ingrese el nombre de la mascota: \n"))
tipo=""
while(True):
        seleccion=str(input("Ingrese el tipo de mascota (p/g): \n"))
        seleccion=seleccion.lower()
        if seleccion!="p" and seleccion !="g":
            print("Entrada no valida, por favor ingrese p ó g")
        else:
            if seleccion=="p":
                tipo="Perro"
            else:
                tipo="Gato"
            break
print("Bienvenido/a "+nombre+", "+tipo)
print("----------------------------------------------------------------------")

def volverFecha(aux=1):

    #strp es para volver una entrada por teclado, una fecha

    #si aux=1, requiero fecha de nacimiento
    #Sino, estoy hablando de última desparacitación
    if aux==1:
        nacimiento=input("Ingrese fecha de nacimiento de la mascota (yyyy-mm-dd): \n")
        nacimiento=dt.strptime(nacimiento,alterno)
        return nacimiento
    else:

        ultima = input("Ingrese fecha especifica de última desparasitación de la mascota (yyyy-mm-dd): \n")
        ultima = dt.strptime(ultima, alterno)
        return ultima



ultima=volverFecha(0)
print("La ultima fecha de desparasitación de "+nombre+" es: "+str(dt.strftime(ultima,alterno)))
print("----------------------------------------------------------------------")
fechatope=ultima+td(days=1461)
print("La programación de desparacitación de "+nombre+" durante los proximos cuatro años es: ")

def queDiaEs(fecha):
    formatoaux="%A"
    dia=dt.strftime(fecha,formatoaux)
    if str(dia)=="viernes" or str(dia)=="sábado" or str(dia)=="domingo":
        if str(dia)=="viernes":

            fecha+=td(days=3)
        elif str(dia)=="sábado":

            fecha+=td(days=2)
        else:

            fecha += td(days=1)
    return fecha



while ultima<=fechatope:
    formatomostrar="%A, %B %d de %Y"
    ultima+=td(days=90)
    ultima=queDiaEs(ultima)
    print("Desparasitación el dia: "+str(dt.strftime(ultima,formatomostrar)))
print("----------------------------------------------------------------------")


nacimiento=volverFecha()
print("La fecha de nacimiento de "+nombre+" es: "+str(dt.strftime(nacimiento,alterno)))
print("----------------------------------------------------------------------")

fechahoy=dt.today()
 #Para hacer los calculos de días meses y años vividos, voy a hacer uso del formato de la fecha, extrayendo a su vez los datos requeridos

añosvividos=rd(fechahoy,nacimiento).years
diasvividos=rd(fechahoy,nacimiento).days
mesesvividos=rd(fechahoy,nacimiento).months

print(nombre+" ha vivido por "+str(añosvividos)+" años, "+str(mesesvividos)+" meses y "+str(diasvividos)+" dias.")

esperanzaperro=14*365
esperanzagato=6*365
diasvividospormascota=fechahoy-nacimiento

if tipo=="Perro":
    print("El potencial de vida para "+nombre+" es de: "+str(esperanzaperro)+", días es decir, 14 años aproximadamente")
    if int(diasvividospormascota.days)>esperanzaperro:
        print("Ha superado la expectativa de vida")

else:
    print("El potencial de vida para " + nombre + " es de: " + str(esperanzagato) + " días, es decir, 6 años aproximadamente")
    if int(diasvividospormascota.days)>esperanzagato:
        print("Ha superado la expectativa de vida")





















