# Libreria de la Actividad 16

class Archivo():
  
  def __init(self):
    self.Lista=[]
   
    
  def GuardarArchivo(self, Club,Estadio,Titulos):
    self.Lista = [Club,Estadio,Titulos]
    registros = [self.Lista]
    Equipos = "Equipos"
    archivo = open(Equipos+".txt", 'w')
    Titulo = """ 
    ++++++++++++++++++++++++++++
            EQUIPOS
    ++++++++++++++++++++++++++++"""+"\n"
    archivo.write(Titulo)
     
      
    for i in range(len(registros)):  
      archivo.write("\n"+"Club: "+registros[i][0]+"\n"+"Estadio: "+registros[i][1]+"\n"+"Titulos: "+str(registros[i][2])+"\n" )

      archivo.write("""---------------------------------------------------------------------""")

      #archivo.close()
    
   
    