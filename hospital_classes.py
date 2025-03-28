#TO DO: -Aplicar bien lo del tiempo de consulta tal y como se indica en el material(creo que ya está), 
#-Añadir los prints que pone el material para todo ._.(Ya estaria esto hecho)

class Patient:
    def __init__(self, IDPac, Consult_type, Priority,Testimated, Arrival_time): #finally added the estimated time
        self.idpac=IDPac
        self.consult_type=Consult_type
        self.priority=Priority
        self.testimated=Testimated
        self.arrival_time=None #se define al entrar en la cola de espera

    @property
    def idpac(self):
        return self._idpac
    @idpac.setter
    def idpac(self, value): #IDPac is a reads a value in format "userXXXX" where X is a digit, don't know how to treat it yet
        if value==None:
            raise ValueError("IDPac cannot be None")
        if not isinstance(value, str):
            raise ValueError("IDPac must be a integer")
        self._idpac=value
    
    @property
    def consult_type(self):
        return self._consult_type
    @consult_type.setter
    def consult_type(self, value):
        if value==None:
            raise ValueError("Consult_type cannot be None")
        if not isinstance(value, str):
            raise ValueError("Consult_type must be a string")
        if value not in ["general", "specialist"]:
            raise ValueError("Consult_type must be general or specialist")
        self._consult_type=value
    
    @property
    def priority(self):
        return self._priority
    @priority.setter
    def priority(self, value):
        if value==None:
            raise ValueError("Priority cannot be None")
        if not isinstance(value, str):
            raise ValueError("Priority must be a string")
        if value not in ["priority", "no_priority"]:
            raise ValueError("Priority must be priority or no_priority")
        self._priority=value
        
    @property
    def testimated(self):
        return self._testimated
    @testimated.setter 
    def testimated(self, value):
        if value==None:
            raise ValueError("time estimated cannot be None")
        if not isinstance(value, int):
            raise ValueError("time estimated must be an integer")
        if value<0:
            raise ValueError("time estimated must be positive")
        self._testimated=value


    @property
    def arrival_time(self): 
        return self._arrival_time
    @arrival_time.setter 
    def arrival_time(self, value):
        if value==None:
            raise ValueError("Arrival_time cannot be None")
        if not isinstance(value, int):
            raise ValueError("Arrival_time must be an integer")
        if value<0:
            raise ValueError("Arrival_time must be positive")
        self._arrival_time=value

    def _str_(self):
        return "Patient ID: "+str(self.idpac)+", Consult type: "+self.consult_type+", Priority: "+str(self.priority)+", Arrival time: "+str(self.arrival_time)

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""

    DEFAULT_CAPACITY = 20  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned

    def __str__(self):
        s = "[\n"
        for i in range(self._front, self._size):
            s += "\t" + self._data[i].__str__() + "\n"
        s += "]\n"
        return s
    
class Turn_manager: 
    def __init__(self):
        self.admission_queue = ArrayQueue(name="ADMISSION")
        self.queues = {
            ("general", "priority"): ArrayQueue(name="GENERAL URGENT"),
            ("general", "no_priority"): ArrayQueue(name="GENERAL NON-URGENT"),
            ("specialist", "priority"): ArrayQueue(name="SPECIAL URGENT"),
            ("specialist", "no_priority"): ArrayQueue(name="SPECIAL NON-URGENT")       
        }
        self.Consulta_general=[None,0] #I do not think we need a queue for this two, so I will use a normal list
        self.Consulta_especialista=[None,0] #I use the second element to store the time left for the consultation
        self._tActual=0
    @property
    def tActual(self): 
        return self._tActual
    tActual.setter
    def tActual(self, value):
        if value==None:
            raise ValueError("tActual cannot be None")
        if not isinstance(value, int):
            raise ValueError("tActual must be an integer")
        if value<0:
            raise ValueError("tActual must be positive")
        self._tActual=value
    def run_time(self)-> None:
        self.check_and_prioritize()
        self.tActual+=1
        return None
    def admit_patient(self, patient):
        """Admit a patient to the admission queue."""
        self.admission_queue.enqueue(patient)
        print(f"{self.tActual}: {patient.idpac} en cola {patient.consult_type}/{patient.priority} EST:{patient.testimated}")

    def process_admission(self):
        """Process a patient from the admission queue to the appropriate consultation queue."""
        if not self.admission_queue.is_empty():
            patient = self.admission_queue.dequeue()
            patient.arrival_time = self.tActual
            self.queues[(patient.consult_type, patient.priority)].enqueue(patient)
            print(f"{self.tActual}: {patient.idpac} en cola {patient.consult_type}/{patient.priority} EST:{patient.testimated}")

    def check_and_prioritize(self):
        """Check and prioritize patients in non-priority queues."""
        for key in [("general", "no_priority"), ("specialist", "no_priority")]:
            queue = self.queues[key]
            for _ in range(len(queue)):
                patient = queue.dequeue()
                tiempo_espera = self.tActual - patient.arrival_time
                if tiempo_espera > 7:
                    # Move the patient to the priority queue
                    new_key = (patient.consult_type, "priority")
                    self.queues[new_key].enqueue(patient)
                    print(f"{self.tActual}: Priorización aplicada {patient.idpac}")
                else:
                    # Re-enqueue the patient if they don't meet the condition
                    queue.enqueue(patient)

    def Consulta_general(self):
        """Start a general consultation if no consultation is in progress."""
        if self.Consulta_general[1] == 0:
            try:
                if not self.queues[("general", "priority")].is_empty():
                    patient = self.queues[("general", "priority")].dequeue()
                else:
                    patient = self.queues[("general", "no_priority")].dequeue()

                self.Consulta_general[0] = patient
                self.Consulta_general[1] = patient.testimated
                print(f"{self.tActual}: {patient.idpac} entra {patient.consult_type}/{patient.priority} ADM:{patient.arrival_time}, INI:{self.tActual}, EST:{patient.testimated}")
            except Exception:
                print("No hay pacientes en las colas de consulta general.")

    def Process_Consulta_general(self):
        """Process the ongoing general consultation."""
        if self.Consulta_general[0] is not None:
            self.Consulta_general[1] -= 1
            if self.Consulta_general[1] == 0:
                patient = self.Consulta_general[0]
                self.Consulta_general[0] = None
                tTotal2 = self.tActual - patient.arrival_time
                print(f"{self.tActual}: {patient.idpac} sale {patient.consult_type}/{patient.priority} ADM:{patient.arrival_time}, INI:{self.tActual - tTotal2}, EST./TOTAL:{patient.testimated}/{tTotal2}")
                return patient

    def Consulta_especialista(self):
        """Start a specialist consultation if no consultation is in progress."""
        if self.Consulta_especialista[1] == 0:
            try:
                if not self.queues[("specialist", "priority")].is_empty():
                    patient = self.queues[("specialist", "priority")].dequeue()
                else:
                    patient = self.queues[("specialist", "no_priority")].dequeue()

                self.Consulta_especialista[0] = patient
                self.Consulta_especialista[1] = patient.testimated
                print(f"{self.tActual}: {patient.idpac} entra {patient.consult_type}/{patient.priority} ADM:{patient.arrival_time}, INI:{self.tActual}, EST:{patient.testimated}")
            except Exception:
                print("No hay pacientes en las colas de consulta especialista.")

    def Process_Consulta_especialista(self):
        """Process the ongoing specialist consultation."""
        if self.Consulta_especialista[0] is not None:
            self.Consulta_especialista[1] -= 1
            if self.Consulta_especialista[1] == 0:
                patient = self.Consulta_especialista[0]
                self.Consulta_especialista[0] = None
                tTotal2 = self.tActual - patient.arrival_time
                print(f"{self.tActual}: {patient.idpac} sale {patient.consult_type}/{patient.priority} ADM:{patient.arrival_time}, INI:{self.tActual - tTotal2}, EST./TOTAL:{patient.testimated}/{tTotal2}")
                return patient

    def _str__(self):
        result = "Admission Queue:\n" + str(self.admission_queue) + "\n"
        for key, queue in self.queues.items():
            result += f"Queue {key}:\n{queue}\n"
        return result
