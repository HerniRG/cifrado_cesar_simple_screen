from simple_screen import Screen_manager, locate, Print, Input, cls 
from funcs import cesar, print_cabecera

with Screen_manager as sc:
        
    def main():
        

        while True:
            cls()
            print_cabecera()
            locate(4, 7)
            cifrado = int(Input("Distancia de cifrado: "))
            locate(4, 8)
            mensaje = Input("Mensaje a cifrar: ")
            mensaje_cifrado = cesar(mensaje, cifrado)
            locate(4, 10)
            Print(f"Mensaje cifrado: {mensaje_cifrado}")
            locate(4, 14)
            salida = Input("¿Otro mensaje (S/N)?: ")
            if salida.lower() != 's':
                break
            

    # Por si se importa para no ejecutarlo
    if __name__ == "__main__":
        main()
