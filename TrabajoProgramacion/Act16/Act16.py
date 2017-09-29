# Actividad 16

from LibreriaAct16 import *

class Equipos():
  def __init__(self):
    self.Club= ""
    self.Estadio= ""
    self.Titulos= 0
    
    
  def RegistrarClub(self,Club,Estadio,Titulos):
    self.Club= Club
    self.Estadio= Estadio
    self.Titulos= Titulos
    A = Archivo()
    A.GuardarArchivo(self.Club,self.Estadio,self.Titulos)
    
    
C = Equipos()
C.RegistrarClub("River","El Monumental",58)

    
    
      