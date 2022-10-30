# importamos la bibliteca NumPy
import numpy as np
 
# función principal del programa
def main():
  # vamos a crear una matriz de 3x3
  m = np.array([(1, 2, 3), (2, 5, 2), (1, 3, 1)])
   
  # calcula el determinante usando solo NumPy
  det = np.linalg.det(m)
     
  # mostramos el resultado
  print("El determinante de la matriz es: %f" % det)
   
if __name__== "__main__":
  main()
