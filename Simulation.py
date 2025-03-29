#TO DO: -Acabar la simulación,
#Añadir recoleccion de datos para pandas(no se si hacerlo aqui o en lo de clases la vd)
from hospital_classes import *
import sys
import pandas as pd

def sim(Hospital:Turn_manager)-> None: #For the moment it returns None, but I will change it later to return data for pandas
    unfinished=True
    while unfinished:
        Hospital.run_time()
        if Hospital.tActual%3==0:
            Hospital.process_admission()
    return None


if __name__ == "__main__":
    # Leer el archivo de configuración desde la línea de comandos o usar el predeterminado
    config_file = sys.argv[1]

    # Intentar abrir el archivo especificado
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: El archivo '{config_file}' no se ha encontrado o no existe.", file=sys.stderr)
        sys.exit(1)
    
    Hospital=Turn_manager()
    for line in lines:
        try:
            idpac, consult_type, priority, testimated = line.split()
        except ValueError:
            print(f"Error: La línea '{line}' no tiene el formato esperado.", file=sys.stderr)
        
        print(f"Paciente: {idpac}, Tipo de consulta: {consult_type}, Prioridad: {priority}, Tiempo estimado: {testimated}")
        paciente = Patient(idpac, consult_type, priority, int(testimated))
        Hospital.admit_patient(paciente)
        print(f"Paciente {paciente.idpac} admitido en la cola de admisión.")