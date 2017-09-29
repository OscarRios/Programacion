#Actividad 15

class Persona():
  
  def __init__(self):
    self.Registro=[]
    self.id=0
    self.Nombre=""
    self.Apellido=""
    self.Edad= 0
    
  def Registrar(self,identificador,Nombre,Apellido,Edad):
    
    self.id= identificador
    self.Nombre=Nombre
    self.Apellido=Apellido
    self.Edad=Edad  
    
  def GuardarRegistro(self) :
    self.Registro= [self.id,self.Nombre,self.Apellido,self.Edad]
    
    
P = Persona()
P.Registrar(1,"Oscar","Rios",22)
P.GuardarRegistro()