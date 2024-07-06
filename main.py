from simple_screen import Screen_manager, locate, cls, Print
from funcs import cesar, print_cabecera

with Screen_manager as sc:
        
    def main():
        print_cabecera()

        while True:
            cifrado = input("Distancia de cifrado: ")
            mensaje = input("Mensaje a cifrar: ")
            mensaje_cifrado = cesar(mensaje, cifrado)
            Print(f"Mensaje cifrado: {mensaje_cifrado}")
            salida = input("¿Otro mensaje (S/N)?: ")
            if salida == "S" or salida == "s":
                break
           







# Por si se importa para no ejecutarlo
if __name__ == "__main__":
    main()





