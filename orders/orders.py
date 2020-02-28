from datetime import datetime


def escape_order():
    now = datetime.now()
    today = date.today()
    #     &&&&&&&&&&&&&6 Guardando en Archivo
    print(today)
    print(now)
    f = open('GENERADOS_inside_orders.txt', 'w')
    f.write(str(now) +" --- BD Vehiculos Auto Conduccion --- " )
    f.write("\n" + " Adelante " + str(i_ad))
    f.write("\n" + " SemIzq " + str(i_si))
    f.write("\n" + " Izq " + str(i_iz))
    f.write("\n" + " SemDer " + str(i_sd))
    f.write("\n" + " Der " + str(i_de))

    f.close()
    #       &&&& fin de guardado &&&&