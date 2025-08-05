"""Mini Project: Hospital Management System
Design a system with the following 3 tightly connected classes:
Must use at least 2 Doctors and 3 Patients
All data properly private and accessed via methods only
"""
class Doctor:
    """
    Class: Doctor
    Attributes: __name, __specialization, __experience (in years)
    Methods: show_profile() → Print all details, is_senior() → Returns True if experience ≥ 10 years
    """
    def __init__(self, name, specialization, experience):
        self.__dname = name
        self.__specialization = specialization
        self.__experience = experience

    def get_dname(self):
        return self.__dname

    def get_specialization(self):
        return self.__specialization

    def get_experience(self):
        return self.__experience

    def show_profile(self):
        print("Doctor's profile:")
        print(f"Doctor Name: {self.get_dname()}")
        print(f"Specialization Area: {self.get_specialization()}")
        print(f"Years of Experience: {self.get_experience()}")

    def is_senior(self):
        return self.get_experience() >= 10

    def set_dname(self, newdname):
        if isinstance(newdname, str):
            self.__dname = newdname
        else:
            print("Invalid name. Must be a string.")

    def set_experience(self, exp):
        if exp > 0:
            self.__experience = exp
        else:
            print("Experience must be positive.")

    def set_specialization(self, spec):
        if isinstance(spec, str):
            self.__specialization = spec
        else:
            print("Invalid specialization. Must be a string.")
class Patient:
    """
    Class: Patient
    Attributes: __name, __age, __disease
    Methods: show_profile(), is_senior() (age ≥ 60), set_disease(), etc.
    """
    def __init__(self, name, age, disease):
        self.__pname = name
        self.__age = age
        self.__disease = disease

    def get_pname(self):
        return self.__pname

    def get_age(self):
        return self.__age

    def get_disease(self):
        return self.__disease

    def set_patient_name(self, newname):
        if newname!="":
            self.__pname = newname

    def set_patient_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
            print(f"Age updated to: {self.__age}")
        else:
            print("No update")

    def set_disease(self, new_disease):
        if new_disease != "":
            self.__disease = new_disease
            print(f"Disease updated to: {self.__disease}")
        else:
            print("Kindly properly name the disease")

    def is_senior(self):
        return self.__age >= 60

    def show_profile(self):
        print("Patient's profile: ")
        print(f"Patient name: {self.get_pname()}")
        print(f"Patient age: {self.get_age()}")
        print(f"Suffering from: {self.get_disease()}")

    def update_profile(self, pname, age, disease):
        self.set_patient_name(pname)
        self.set_patient_age(age)
        self.set_disease(disease)


class Hospital:
    """
    Class: Hospital
    Attributes:
    __hospital_name,
    __doctors → list of Doctor objects
    __patients → list of Patient objects
    Methods:
    add_doctor(doctor_obj)
    add_patient(patient_obj)
    show_all_doctors()
    show_all_patients()
    assign_disease(patient_name, new_disease)
    find_doctor_by_specialization(specialization)
    → Return all doctors with that specialization
    """
    def __init__(self,name):
        self.__hname = name
        self.__doctors = []
        self.__patients = []

    def get_hospital_name(self):
        return self.__hname

    def get_doctors(self):
        return self.__doctors
    
    def get_patients(self):
        return self.__patients

    def add_doctor(self, newdoctor):
        if newdoctor not in self.__doctors:
            self.__doctors.append(newdoctor)
        else:
            print(f"{newdoctor.get_dname()} already exists in hospital database.")


    def add_patient(self, newpatient):
        if newpatient not in self.__patients:
            self.__patients.append(newpatient)
        else:
            print(f"{newpatient.get_pname()} already exists in hospital database.")

    def show_all_doctors(self):
        print(f"\nDoctors at {self.get_hospital_name()}:")
        for doctor in self.__doctors:
            doctor.show_profile()
    
    def show_all_patients(self):
        print(f"\nPatients at {self.get_hospital_name()}:")
        for patient in self.__patients:
            patient.show_profile()

    def assign_disease(self, pname, new_disease):
        found = False
        for patient in self.__patients:
            if patient.get_pname() == pname:
                patient.set_disease(new_disease)
                found = True
                break
        if not found:
            print(f"No patient found with the name {pname}")


 

    def find_doctor_of(self,specialization):
        print(f"\nSearching for doctors in specialization: {specialization}")
        found = False
        for doctor in self.__doctors:
            if doctor.get_specialization().lower() == specialization.lower():
                doctor.show_profile()
                print("------")
                found = True
        if not found:
            print("No doctor found with that specialization.")

# ------------------- TESTING (GPT) -------------------

# Create doctors
doc1 = Doctor("Dr. Asad", "Cardiology", 15)
doc2 = Doctor("Dr. Sara", "Neurology", 7)

# Create patients
p1 = Patient("Ali", 65, "Heart Disease")
p2 = Patient("Maria", 45, "Migraine")
p3 = Patient("John", 25, "Allergy")

# Create hospital
my_hospital = Hospital("City Care Hospital")

# Add doctors and patients
my_hospital.add_doctor(doc1)
my_hospital.add_doctor(doc2)
my_hospital.add_patient(p1)
my_hospital.add_patient(p2)
my_hospital.add_patient(p3)

# Show everything
my_hospital.show_all_doctors()
my_hospital.show_all_patients()

# Test disease assignment
my_hospital.assign_disease("Maria", "Epilepsy")

# Test finding doctors by specialization
my_hospital.find_doctor_of("Neurology")
my_hospital.find_doctor_of("Oncology")  # Not available

    
#________________________happy end________________________
