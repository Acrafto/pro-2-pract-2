#TO DO: -Acabar la simulación,
#Añadir recoleccion de datos para pandas(no se si hacerlo aqui o en lo de clases la vd)
from clases import *
import sys
import pandas as pd


def simulate_attend_patients(hospital:Turn_manager)-> None: #For the moment it returns None, but I will change it later to return data for pandas
    unfinished=True
    hospital.add_patient_to_respective_wait_queue()
    while unfinished:
        unfinished = hospital.run_time()
        if (hospital.tActual % 3 - 1) == 0:
            hospital.add_patient_to_respective_wait_queue()

    return None

if __name__ == "__main__":
    # Leer el nombre del archivo desde la línea de comandos o usar un nombre predeterminado
    config_file_name = sys.argv[1] if len(sys.argv) > 1 else "patients0.txt"
    #sys.argv devuelve una lista con cada uno de los argumentos usados en la terminal.
    #Si ejecutas este script desde el simbolo "Run Python File" equivale a escribir en la terminal:
    #python .\Simulation.py. por lo que si haces len(sys.argv) te devolvera 1 y con ello se ejecutara el bloque else.
    #si se quiere ejecutar desde la terminal: python .\Simulation.py "patients0.txt" por ejemplo.
    #len(sys.argv) sera 2 y eso ejecutara sys.argv[1] y eso se definira en config_fila_name.

    # Intentar abrir el archivo especificado
    try:
        with open(config_file_name, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: El archivo '{config_file_name}' no se ha encontrado o no existe.", file=sys.stderr)
        sys.exit(1)

    hospital=Turn_manager()
    for line in lines:
        try:
            idpac, consult_type, priority, t_estimated = line.split()
            #.split() method for string class, return a list splitting the elements by a certain criteria, then, when we have the returned list we assign every element from the list to the variables by doing multiple assignments in the same line
        except ValueError:
            print(f"Error: La línea '{line}' no tiene el formato esperado.", file=sys.stderr) #no se que error es ese.

       # print(f"Paciente: {idpac}, Tipo de consulta: {consult_type}, Prioridad: {priority}, Tiempo estimado: {t_estimated}")
        paciente = Patient(idpac, consult_type, priority, int(t_estimated))
        hospital.add_patient_to_admition_queue(paciente)
        #print(f"Paciente {paciente.idpac} admitido en la cola de admisión.")

    simulate_attend_patients(hospital)