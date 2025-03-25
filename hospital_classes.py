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
    def testimated(self): #Don't know exactly what this is, so I'm assuming it's an integer
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
    def arrival_time(self): #Don't know exactly what this is, so I'm assuming it's an integer
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

class PatientQueue: #Not implemented exactly as the material says, we'll figure out how to do it later
    def __init__(self,name):
        self._patients=[]
        self._name=name

    def add_patient(self, patient):
        if not isinstance(patient, Patient):
            raise ValueError("Patient must be a Patient object")
        self._patients.append(patient)

    def size(self):
        return len(self.items)
    
    def remove_patient(self, idpac):
        for patient in self._patients:
            if patient.idpac==idpac:
                self._patients.remove(patient)
                return
        raise ValueError("Patient not found")
    
    def __str__(self):
        result=""
        for patient in self._patients:
            result+=str(patient)+"\n"
        return result
    
class HospitalQueueSystem: #Awating time and sheit not implemented yet
    def __init__(self):
        self.admission_queue = PatientQueue(name="ADMISSION")
        self.queues = {
            ("general", "priority"): PatientQueue(name="GENERAL URGENT"),
            ("general", "no_priority"): PatientQueue(name="GENERAL NON-URGENT"),
            ("specialist", "priority"): PatientQueue(name="SPECIAL URGENT"),
            ("specialist", "no_priority"): PatientQueue(name="SPECIAL NON-URGENT")
        }

    def admit_patient(self, patient):
        self.admission_queue.enqueue(patient)

    def process_admission(self):
        while not self.admission_queue.is_empty():
            patient = self.admission_queue.dequeue()
            self.queues[(patient.consult_type, patient.priority)].enqueue(patient)

    def get_next_patient(self, consult_type, priority):
        queue = self.queues[(consult_type, priority)]
        if queue.is_empty():
            return None
        return queue.dequeue()
    def _str__(self):
        result = "Admission Queue:\n" + str(self.admission_queue) + "\n"
        for key, queue in self.queues.items():
            result += f"Queue {key}:\n{queue}\n"
        return result
