class Cifrador:
    def __init__(self, d) -> None:
        self.d = d
        self.cifrados_pendientes = 2
    
    def cesar(self, cadena: str) -> str:
        alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
        cifrado_realizado = ""
        long_alfabeto = len(alfabeto)

        for caracter in cadena.upper():
            if caracter in alfabeto:
                indice = alfabeto.index(caracter)
                indice_cifrado = (indice + self.d) % long_alfabeto # si es mayor de long alfabeto se hace modulo para saber el sobrante y empezar de nuevo 
                cifrado_realizado += alfabeto[indice_cifrado]
            else:
                cifrado_realizado += caracter
        return cifrado_realizado
    
    def cifrar(self, mensaje) -> str:

        if self.cifrados_pendientes == 0:
            return "Compre recambios en cifrados Pepe!"

        self.cifrados_pendientes -= 1

        return self.cesar(mensaje)
    
    
    def crea_cifrador(self) -> callable:
        def cifrador_interno(cadena):
            return self.cesar(cadena, self.d)
        return cifrador_interno


    def crea_par_cesar(self) -> tuple:
        def cifrador_interno(cadena):
            return self.cesar(cadena, self.d)
        def descifrador_interno(cadena):
            return self.cesar(cadena, -self.d)
        return cifrador_interno, descifrador_interno