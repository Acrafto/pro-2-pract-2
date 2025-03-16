class Patient:
    def __init__(self, IDPac, Consult_type, Urgency, Arrival_time,): #We may need another parameter for the time required to treat the patient
        self.idpac=IDPac
        self.consult_type=Consult_type
        self.urgency=Urgency
        self.arrival_time=Arrival_time

    @property
    def idpac(self):
        return self.__idpac
    @idpac.setter
    def idpac(self, value): #IDPac is a reads a value in format "userXXXX" where X is a digit, don't know how to treat it yet
        if value==None:
            raise ValueError("IDPac cannot be None")
        if not isinstance(value, str):
            raise ValueError("IDPac must be a integer")
        self.__idpac=value
    
    @property
    def consult_type(self):
        return self.__consult_type
    @consult_type.setter
    def consult_type(self, value):
        if value==None:
            raise ValueError("Consult_type cannot be None")
        if not isinstance(value, str):
            raise ValueError("Consult_type must be a string")
        if value not in ["general", "specialist"]:
            raise ValueError("Consult_type must be general or specialist")
        self.__consult_type=value
    
    @property
    def urgency(self):
        return self.__urgency
    @urgency.setter
    def urgency(self, value):
        if value==None:
            raise ValueError("Urgency cannot be None")
        if not isinstance(value, str):
            raise ValueError("Urgency must be a string")
        if value not in ["urgent", "non-urgent"]:
            raise ValueError("Urgency must be urgent or non-urgent")
        self.__urgency=value
    
    @property
    def arrival_time(self): #Don't know exactly what this is, so I'm assuming it's an integer
        return self.__arrival_time
    @arrival_time.setter 
    def arrival_time(self, value):
        if value==None:
            raise ValueError("Arrival_time cannot be None")
        if not isinstance(value, int):
            raise ValueError("Arrival_time must be an integer")
        if value<0:
            raise ValueError("Arrival_time must be positive")
        self.__arrival_time=value

    def __str__(self):
        return "Patient ID: "+str(self.idpac)+", Consult type: "+self.consult_type+", Urgency: "+str(self.urgency)+", Arrival time: "+str(self.arrival_time)

class PatientQueue: #Not implemented exactly as the material says, we'll figure out how to do it later
    def __init__(self,name):
        self.__patients=[]
        self.__name=name

    def add_patient(self, patient):
        if not isinstance(patient, Patient):
            raise ValueError("Patient must be a Patient object")
        self.__patients.append(patient)

    def size(self):
        return len(self.items)
    
    def remove_patient(self, idpac):
        for patient in self.__patients:
            if patient.idpac==idpac:
                self.__patients.remove(patient)
                return
        raise ValueError("Patient not found")
    
    def __str__(self):
        result=""
        for patient in self.__patients:
            result+=str(patient)+"\n"
        return result
    
class HospitalQueueSystem: #Awating time and sheit not implemented yet
    def __init__(self):
        self.admission_queue = PatientQueue(name="ADMISSION")
        self.queues = {
            ("GN", True): PatientQueue(name="GENERAL URGENT"),
            ("GN", False): PatientQueue(name="GENERAL NON-URGENT"),
            ("SP", True): PatientQueue(name="SPECIAL URGENT"),
            ("SP", False): PatientQueue(name="SPECIAL NON-URGENT")
        }

    def admit_patient(self, patient):
        self.admission_queue.enqueue(patient)

    def process_admission(self):
        while not self.admission_queue.is_empty():
            patient = self.admission_queue.dequeue()
            self.queues[(patient.consult_type, patient.urgency)].enqueue(patient)

    def get_next_patient(self, consult_type, urgency):
        queue = self.queues[(consult_type, urgency)]
        if queue.is_empty():
            return None
        return queue.dequeue()
    def __str__(self):
        result = "Admission Queue:\n" + str(self.admission_queue) + "\n"
        for key, queue in self.queues.items():
            result += f"Queue {key}:\n{queue}\n"
        return result
#I'm gonna kill myself after this, so I hope this works for now