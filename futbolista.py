from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(nombre, edad, altura, sexo)
        Deportista.__init__(self, añosPracticando)
        self._golesMarcado = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcado
        
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcado = golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas
        
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil
        
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    @classmethod
    def getListaFutbolistas(clc):
        return clc.listaFutbolistas

    @classmethod 
    def setListaFutbolistas(clc, listaFutbolistas):
        clc.listaFutbolistas = listaFutbolistas

    def __str__(self):
        return f"Mi nombre es {Persona.getNombre()} soy profesional en el deporte {Deportista.getDeporte()} Tengo {Persona.getEdad()} años de edad y llevo {Deportista.getAñosPracticando()} años en el deporte"