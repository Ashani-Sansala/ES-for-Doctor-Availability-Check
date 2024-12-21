from experta import Fact

class DoctorAvailability(Fact):
    pass

HOSPITAL_DATABASE = [
    {
        "hospital_id": "H001",
        "name": "Colombo General Hospital",
        "location": "Colombo",
        "specialties": [
            "Cardiology", "Pediatrics", "General Medicine", 
            "Neurology", "Oncology", "Emergency Medicine",
            "Dermatology", "Psychiatry"
        ]
    },
    {
        "hospital_id": "H002", 
        "name": "Kandy Teaching Hospital",
        "location": "Kandy",
        "specialties": [
            "Dermatology", "Orthopedics", "Neurology", 
            "Psychiatry", "Endocrinology", "Pediatrics",
            "Cardiology"
        ]
    },
    {
        "hospital_id": "H003",
        "name": "Karapitiya Teaching Hospital",
        "location": "Galle",
        "specialties": [
            "Cardiology", "Pediatrics", "Dermatology", 
            "Gynecology", "Urology", "Sports Medicine"
        ]
    },
    {
        "hospital_id": "H004",
        "name": "Jaffna General Hospital",
        "location": "Jaffna",
        "specialties": [
            "Family Medicine", "Internal Medicine", "Geriatrics", 
            "Pulmonology", "Cardiology", "Oncology", "Dermatology"
        ]
    },
    {
        "hospital_id": "H005",
        "name": "Teaching Hospital Peradeniya",
        "location": "Peradeniya",
        "specialties": [
            "Neurology", "Orthopedics", "Sports Medicine", 
            "Rehabilitation", "Pain Management", "Physical Therapy",
            "Cardiology", "Dermatology"
        ]
    }
]


DOCTOR_DATABASE = [
    # Colombo General Hospital Doctors
    {
        "doctor_id": "DR001",
        "name": "Dr. Nuwan Perera",
        "specialization": "Cardiology",
        "hospital_id": "H001",
        "hospital_name": "Colombo General Hospital",
        "availability_days": ["Monday", "Wednesday", "Friday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"}
        },
        "max_patients_per_day": 20,
        "current_patients": 0,
        "consultation_duration": 30,
        "contact": "nuwan.perera@colombohosp.lk"
    },
    {
        "doctor_id": "DR002",
        "name": "Dr. Amaya Wickramasinghe",
        "specialization": "Pediatrics",
        "hospital_id": "H001",
        "hospital_name": "Colombo General Hospital",
        "availability_days": ["Tuesday", "Thursday", "Saturday"],
        "availability_hours": {
            "Tuesday": {"start": "08:30", "end": "16:30"},
            "Thursday": {"start": "09:00", "end": "17:00"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 15,
        "current_patients": 0,
        "consultation_duration": 45,
        "contact": "amaya.wickramasinghe@colombohosp.lk"
    },
    
    # Kandy Teaching Hospital Doctors
    {
        "doctor_id": "DR003",
        "name": "Dr. Rajitha De Silva",
        "specialization": "Dermatology",
        "hospital_id": "H002",
        "hospital_name": "Kandy Teaching Hospital",
        "availability_days": ["Monday", "Thursday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "11:00", "end": "19:00"},
            "Thursday": {"start": "08:00", "end": "16:00"},
            "Saturday": {"start": "09:00", "end": "13:00"}
        },
        "max_patients_per_day": 18,
        "current_patients": 0,
        "consultation_duration": 40,
        "contact": "rajitha.desilva@kandyhosp.lk"
    },
    {
        "doctor_id": "DR004",
        "name": "Dr. Nishantha Karunaratne",
        "specialization": "Orthopedics",
        "hospital_id": "H002",
        "hospital_name": "Kandy Teaching Hospital",
        "availability_days": ["Tuesday", "Wednesday", "Friday"],
        "availability_hours": {
            "Tuesday": {"start": "09:00", "end": "17:00"},
            "Wednesday": {"start": "14:00", "end": "20:00"},
            "Friday": {"start": "07:30", "end": "15:30"}
        },
        "max_patients_per_day": 16,
        "current_patients": 0,
        "consultation_duration": 50,
        "contact": "nishantha.karunaratne@kandyhosp.lk"
    },
    
    # Karapitiya Teaching Hospital Doctors
    {
        "doctor_id": "DR005",
        "name": "Dr. Malini Fernando",
        "specialization": "Gynecology",
        "hospital_id": "H003",
        "hospital_name": "Karapitiya Teaching Hospital",
        "availability_days": ["Monday", "Thursday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "09:00", "end": "17:00"},
            "Thursday": {"start": "13:00", "end": "20:00"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 12,
        "current_patients": 0,
        "consultation_duration": 60,
        "contact": "malini.fernando@karapitiya.lk"
    },
    
    # Jaffna General Hospital Doctors
    {
        "doctor_id": "DR006",
        "name": "Dr. Sanjeewa Kumarasinghe",
        "specialization": "Family Medicine",
        "hospital_id": "H004",
        "hospital_name": "Jaffna General Hospital",
        "availability_days": ["Monday", "Wednesday", "Friday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "10:00", "end": "18:00"},
            "Friday": {"start": "07:30", "end": "15:30"}
        },
        "max_patients_per_day": 20,
        "current_patients": 0,
        "consultation_duration": 30,
        "contact": "sanjeewa.kumarasinghe@jaffnahosp.lk"
    },
    
    # Teaching Hospital Peradeniya Doctors
    {
        "doctor_id": "DR007",
        "name": "Dr. Ashan Wijesinghe",
        "specialization": "Orthopedics",
        "hospital_id": "H005",
        "hospital_name": "Teaching Hospital Peradeniya",
        "availability_days": ["Monday", "Wednesday", "Friday"],
        "availability_hours": {
            "Monday": {"start": "10:00", "end": "18:00"},
            "Wednesday": {"start": "08:00", "end": "16:00"},
            "Friday": {"start": "12:00", "end": "20:00"}
        },
        "max_patients_per_day": 15,
        "current_patients": 0,
        "consultation_duration": 50,
        "contact": "ashan.wijesinghe@peradeniya.lk"
    },

    {
        "doctor_id": "DR008",
        "name": "Dr. Ashani Perera",
        "specialization": "Cardiology",
        "hospital_id": "H001",
        "hospital_name": "Colombo General Hospital",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 20,
        "current_patients": 0,
        "consultation_duration": 30,
        "contact": "nuwan.perera@colombohosp.lk"
    },

    {
        "doctor_id": "DR013",
        "name": "Dr. Nimal Perera",
        "hospital_id": "H001",
        "hospital_name": "Colombo General Hospital",
        "specialization": "Cardiology",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 20,
        "current_patients": 0,
        "consultation_duration": 30,
        "contact_email": "nimal.perera@citycentral.lk"
    },
    {
        "doctor_id": "DR014",
        "hospital_id": "H003",
        "name": "Dr. Shalini Fernando",
        "hospital_name": "Karapitiya Teaching Hospital",
        "specialization": "Cardiology",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 18,
        "current_patients": 0,
        "consultation_duration": 40,
        "contact_email": "shalini.fernando@metropolitan.lk"
    },
    {
        "doctor_id": "DR015",
        "hospital_id": "H001",
        "name": "Dr. Anura Wickramasinhe",
        "hospital_name": "Colombo General Hospital",
        "specialization": "Cardiology",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 15,
        "current_patients": 0,
        "consultation_duration": 45,
        "contact_email": "anura.wickramasinghe@greenwood.lk"
    },
    {
        "doctor_id": "DR016",
        "hospital_id": "H003",
        "name": "Dr. Kumudunu Jayawardena",
        "hospital_name": "Karapitiya Teaching Hospital",
        "specialization": "Cardiology",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 20,
        "current_patients": 0,
        "consultation_duration": 30,
        "contact_email": "kumudini.jayawardena@sunrise.lk"
    },
    {
        "doctor_id": "DR017",
        "hospital_id": "H003",
        "name": "Dr. Chathura Ranasinghe",
        "hospital_name": "Karapitiya Teaching Hospital",
        "specialization": "Cardiology",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 18,
        "current_patients": 0,
        "consultation_duration": 35,
        "contact_email": "chathura.ranasinghe@riverside.lk"
    },
    {
        "doctor_id": "DR018",
        "hospital_id": "H001",
        "name": "Dr. Dilini Pathirana",
        "hospital_name": "Colombo General Hospital",
        "specialization": "Dermatology",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 15,
        "current_patients": 0,
        "consultation_duration": 45,
        "contact_email": "dilini.pathirana@sunrise.lk"
    },
    {
        "doctor_id": "DR019",
        "hospital_id": "H003",
        "name": "Dr. Roshantha Jayasekara",
        "hospital_name": "Karapitiya Teaching Hospital",
        "specialization": "Dermatology",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 18,
        "current_patients": 0,
        "consultation_duration": 40,
        "contact_email": "roshantha.jayasekara@citycentral.lk"
    },
    {
        "doctor_id": "DR020",
        "hospital_id": "H001",
        "name": "Dr. Priyanga Samarasekara",
        "hospital_name": "Colombo General Hospital",
        "specialization": "Dermatology",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 20,
        "current_patients": 0,
        "consultation_duration": 30,
        "contact_email": "priyanga.samarasekara@metropolitan.lk"
    },
    {
        "doctor_id": "DR021",
        "hospital_id": "H001",
        "name": "Dr. Harni Silva",
        "hospital_name": "Colombo General Hospital",
        "specialization": "Dermatology",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 12,
        "current_patients": 0,
        "consultation_duration": 50,
        "contact_email": "harini.silva@riverside.lk"
    },
    {
        "doctor_id": "DR022",
        "hospital_id": "H004",
        "name": "Dr. Madhavi Senanayake",
        "hospital_name": "Greenwood Community Hospital",
        "specialization": "Dermatology",
        "availability_days": ["Monday", "Wednesday", "Friday", "Saturday"],
        "availability_hours": {
            "Monday": {"start": "08:00", "end": "16:00"},
            "Wednesday": {"start": "09:00", "end": "17:00"},
            "Friday": {"start": "07:30", "end": "15:30"},
            "Saturday": {"start": "10:00", "end": "14:00"}
        },
        "max_patients_per_day": 15,
        "current_patients": 0,
        "consultation_duration": 45,
        "contact_email": "madhavi.senanayake@greenwood.lk"
    }
]


def initialize_doctor_facts():
    """
    Convert doctor database into Experta Facts
    
    Returns:
    List of DoctorAvailability Facts
    """
    doctor_facts = []
    for doctor in DOCTOR_DATABASE:
        doctor_fact = DoctorAvailability(**doctor)
        doctor_facts.append(doctor_fact)
    
    return doctor_facts

def get_hospital_names():
    return [hospital['name'] for hospital in HOSPITAL_DATABASE]

# Helper functions for availability checks
def is_doctor_available(doctor, day, time):
    if day not in doctor['availability_days']:
        return False
    
    day_hours = doctor['availability_hours'][day]
    return (day_hours['start'] <= time <= day_hours['end'])

def can_accept_more_patients(doctor):
    """
    Check if doctor can accept more patients
    
    Args:
    - doctor (dict): Doctor information
    
    Returns:
    bool: Whether doctor can accept more patients
    """
    return doctor['current_patients'] < doctor['max_patients_per_day']


def get_all_specializations():
    """
    Retrieve unique list of specializations
    
    Returns:
    List of specializations
    """
    specializations = set()
    for doctor in DOCTOR_DATABASE:
        specializations.add(doctor['specialization'])
    return sorted(list(specializations))