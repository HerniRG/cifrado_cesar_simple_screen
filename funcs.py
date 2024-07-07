from simple_screen import cls, Print, pen, locate, Input, DIMENSIONS
from simple_screen.entities import Color


def calculo_width():
    width = DIMENSIONS.w
    column_center = (width - len("*          CIFRADO CESAR          *")) // 2 
    return column_center

def obtener_cifrado_y_mensaje(ancho_pantalla):
    try:
        locate(ancho_pantalla, 7)
        cifrado = int(Input("Distancia de cifrado: "))   
        locate(ancho_pantalla, 8)
        mensaje = Input("Mensaje a cifrar: ")
    except ValueError:
        raise ValueError("Error: El dato introducido no es válido.")
        
    return cifrado, mensaje

def mostrar_mensaje_cifrado(ancho_pantalla, mensaje_cifrado):
    locate(ancho_pantalla, 10)
    Print(f"Mensaje cifrado: {mensaje_cifrado}")

def mostrar_error(ancho_pantalla, error):
    pen(Color(255, 0, 0))
    locate(ancho_pantalla, 16)
    Print(error)
    locate(ancho_pantalla, 17)
    Input("Pulsa cualquier tecla para continuar...") #lo he hecho así porque sino vuelve al bucle y me borra el print del error

def salir_programa(ancho_pantalla):
    locate(ancho_pantalla, 14)
    salida = Input("¿Otro mensaje (S/N)?: ")
    return salida.lower() != 's'

def print_cabecera(espacio_centrado):
    cls()
    pen(Color(0, 255, 0))  # Establece el color verde lima para la cabecera
    Print(f"{' ' * espacio_centrado}***********************************")
    Print(f"{' ' * espacio_centrado}*                                 *")
    Print(f"{' ' * espacio_centrado}*          CIFRADO CESAR          *")
    Print(f"{' ' * espacio_centrado}*                                 *")
    Print(f"{' ' * espacio_centrado}***********************************") 






   
# ana = Cifrador(4)
# Print(ana.cifrados_pendientes)
# Print(ana.cifrar("Hola"))
