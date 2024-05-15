class Tamagotchi:
    nivel_energia=100
    nivel_hambre=0
    nivel_felicidad=50
    humor="indiferente"
    esta_vivo=True
    def __init__(self,nombre):
        self.nombre=nombre
       
    def modificador(self,nombre,cantidad,hacer,humor):
        if hacer=="resta":
            for i in range(cantidad):
                if nombre==0:
                    break
                else:
                    nombre-=1
        if hacer=="suma":
            for i in range(cantidad):
                if nombre==100:
                    break
                else:
                    nombre+=1
        return nombre
    def modi_humor(self,felicidad):
        if felicidad<20:
            humor="enojado"
        elif felicidad>20 and felicidad<40:
            humor="triste"
        elif felicidad>40 and felicidad<60:
            humor="indiferente"
        elif felicidad>60 and felicidad<80:
            humor="feliz"
        elif felicidad>80 :
            humor="eudorico"
        return humor
    
    def mostrar_estado(self):
        print(f"El estado actual de {self.nombre} es:")
        print(f"Energía: {self.nivel_energia}")
        print(f"Hambre: {self.nivel_hambre}")
        print(f"Humor {self.humor}")

    def alimentar(self):
        self.nivel_hambre=self.modificador(self.nivel_hambre,10,"resta")
        self.nivel_energia=self.modificador(self.nivel_energia,15,"resta")

    def jugar(self):
        if self.nivel_hambre<=20:
            self.nivel_felicidad=self.modificador(self.nivel_felicidad,30,"resta")
            self.humor=self.modi_humor(self.nivel_felicidad,self.humor)
            self.nivel_energia=self.modificador(self.nivel_energia,20,"resta")
            self.nivel_hambre=self.modificador(self.nivel_hambre,10,"suma")
            pass
        else:
            self.nivel_felicidad=self.modificador(self.nivel_felicidad,20,"suma")
            self.humor=self.modi_humor(self.nivel_felicidad,self.humor)
            self.nivel_energia=self.modificador(self.nivel_energia,18,"resta")
            self.nivel_hambre=self.modificador(self.nivel_hambre,10,"suma")
        self.verificar_estado()
    def dormir(self):
        if self.nivel_hambre<=20:
            self.nivel_energia=self.modificador(self.nivel_energia,20,"resta")
            self.nivel_felicidad=self.modificador(self.nivel_felicidad,30,"resta")
            self.humor=self.modi_humor(self.nivel_felicidad,self.humor)
            self.nivel_hambre=self.modificador(self.nivel_hambre,5,"suma")
        else:
                
            self.nivel_energia=self.modificador(self.nivel_energia,40,"suma")
            self.nivel_hambre=self.modificador(self.nivel_hambre,5,"suma")
        self.verificar_estado()
    def verificar_estado(self):
        if self.esta_vivo:
            print("----------------------")
            print("El tamagochi esta vivo")
        else:
            print("----------------------")
            print("El tamagochi esta muerto")
            print("Fin del juego")
            










