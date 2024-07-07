from simple_screen import Screen_manager, locate, cls, init, finish, Print, Input
from cesar_class import Cifrador
from funcs import calculo_width, mostrar_error, mostrar_mensaje_cifrado, obtener_cifrado_y_mensaje, salir_programa, print_cabecera

with Screen_manager as sc:
        
    def main():
        init()
        ancho_pantalla = calculo_width()      
        cifrador = Cifrador(0)
        while True:
            locate(ancho_pantalla, 1)
            print_cabecera(ancho_pantalla)
            try:
                cifrado, mensaje = obtener_cifrado_y_mensaje(ancho_pantalla)
            except ValueError as e:
                mostrar_error(ancho_pantalla, e) #lo he hecho así porque sino vuelve al bucle y me borra el print del error
                continue
                
            cifrador.d = cifrado
            mensaje_cifrado = cifrador.cifrar(mensaje)
            mostrar_mensaje_cifrado(ancho_pantalla, mensaje_cifrado)
            
            if salir_programa(ancho_pantalla):
                break
        
        finish()

# Por si se importa para no ejecutarlo
if __name__ == "__main__":
    main()

   