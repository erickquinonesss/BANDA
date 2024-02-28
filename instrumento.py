

class Instrumento:

    def afinar(self):
        pass

    def tocar(self):
        pass
    
    def mostrar(self):
        return "Instrumento: " + (str(type(self)).split(".")[-1][:-2])

class Guitarra(Instrumento):
    def afinar(self):
        print("Afinando guitarra")
    
    def tocar(self):
        print("Tocando guitarra")

        
class Saxo(Instrumento):
    def afinar(self):
        return("Afinando Saxo")
    
    def tocar(self):
        return("Tocando Saxo")
        
class Tiple(Instrumento):
    def afinar(self):
        return("Afinando Tiple")
    
    def tocar(self):
        return("Tocando Tiple")
        
class Bateria(Instrumento):
    def afinar(self):
        return("Afinando Bateria")
    
    def tocar(self):
        return("Tocando Bateria")
        
class Bajo(Instrumento):
    def afinar(self):
        return("Afinando Bajo")
    
    def tocar(self):
        return("Tocando Bajo")
        
class Piano(Instrumento):
    def afinar(self):
        return("Afinando Piano")
    
    def tocar(self):
        return("Tocando Piano")
    
class Trompeta(Instrumento):
    def afinar(self):
        return("Afinando Trompeta")
    
    def tocar(self):
        return("Tocando Trompeta")

class Flauta(Instrumento):
    def afinar(self):
        return("Afinando Flauta")
    
    def tocar(self):
        return("Tocando Flauta")
    
class Ukelele(Instrumento):
    def afinar(self):
        return("Afinando Ukelele")
    
    def tocar(self):
        return("Tocando Ukelele")
    
class Violin(Instrumento):
    def afinar(self):
        return("Afinando Violin")
    
    def tocar(self):
        return("Tocando Violin")