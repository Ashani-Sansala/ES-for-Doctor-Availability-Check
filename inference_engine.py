from experta import KnowledgeEngine, Rule, MATCH
from knowledge_base import (
    DoctorAvailability, 
    DOCTOR_DATABASE, 
    HOSPITAL_DATABASE, 
    get_all_specializations 
)

class DoctorAvailabilityEngine(KnowledgeEngine):
    def __init__(self, doctors=None):
        super().__init__()
        self.doctors = doctors or DOCTOR_DATABASE
        self.available_doctors = []
        self.hospitals = HOSPITAL_DATABASE
        self.all_specializations = get_all_specializations()
    
    def find_alternative_specializations(self, target_specialization):
        """
        Find alternative specializations similar to the target specialization
        
        Args:
        - target_specialization (str): Original specialization searched
        
        Returns:
        list: Alternative specializations
        """
        # alternative finding strategy
        alternatives = {
            "Cardiology": ["Internal Medicine", "Family Medicine"],
            "Pediatrics": ["Family Medicine", "Internal Medicine"],
            "Neurology": ["Psychiatry", "Internal Medicine"],
            "Orthopedics": ["Sports Medicine", "Rehabilitation"],
            "Dermatology": ["General Medicine"],
            "Psychiatry": ["Neurology", "Family Medicine"],
            "Gynecology": ["Family Medicine"],
            "Sports Medicine": ["Orthopedics", "Family Medicine"],
            "Geriatrics": ["Internal Medicine", "Family Medicine"]
        }
        
        if target_specialization in alternatives:
            return [alt for alt in alternatives[target_specialization] 
                    if alt in self.all_specializations]
        
        return [spec for spec in self.all_specializations 
                if spec != target_specialization]
    
    def search_available_doctors(self, specialization=None, hospital=None, day=None, time=None):

        results = []
        for doctor in self.doctors:
            if specialization and doctor['specialization'] != specialization:
                continue

            if hospital and doctor['hospital_name'] != hospital:
                continue

            if day and day not in doctor['availability_days']:
                continue

            if time:
                day_hours = doctor['availability_hours'].get(day, {})
                if not (day_hours.get('start', '00:00') <= time <= day_hours.get('end', '23:59')):
                    continue
            
            if doctor['current_patients'] < doctor['max_patients_per_day']:
                results.append(doctor)
        
        confidence_score = self.calculate_overall_confidence(results, specialization, hospital, day, time)

        if not results and specialization:
            alternative_specs = self.find_alternative_specializations(specialization)
            alternative_results = []
            
            for alt_spec in alternative_specs:
                for doctor in self.doctors:
                    if doctor['specialization'] != alt_spec:
                        continue
                    
                    if hospital and doctor['hospital_name'] != hospital:
                        continue
                    
                    if day and day not in doctor['availability_days']:
                        continue
                    
                    if time:
                        day_hours = doctor['availability_hours'].get(day, {})
                        if not (day_hours.get('start', '00:00') <= time <= day_hours.get('end', '23:59')):
                            continue
                    
                    if doctor['current_patients'] < doctor['max_patients_per_day']:
                        alternative_results.append(doctor)
            
            return {
                "primary_results": results,
                "alternative_results": alternative_results,
                "alternative_specializations": alternative_specs
            }
        
        # If results found or no specialization, return standard result
        return {
            "primary_results": results,
            "alternative_results": [],
            "alternative_specializations": [],
            "confidence_score": confidence_score
        }
    
    def book_appointment(self, doctor_id):
        # Book an appointment and update current patient count
        for doctor in self.doctors:
            if doctor['doctor_id'] == doctor_id:
                if doctor['current_patients'] < doctor['max_patients_per_day']:
                    doctor['current_patients'] += 1
                    return True
                return False
        return False

    def calculate_overall_confidence(self, primary_results, specialization, hospital, day, time):
        if not specialization and not hospital and not day and not time:
            # No criteria provided, confidence is irrelevant
            return 1.0

        total_weight = 0
        matched_weight = 0

        # Weights for each criterion
        weights = {
            "specialization": 0.4,
            "hospital": 0.3,
            "day": 0.2,
            "time": 0.1,
        }

        # Check each criterion and accumulate weights
        if specialization:
            total_weight += weights["specialization"]
            if any(doctor['specialization'] == specialization for doctor in primary_results):
                matched_weight += weights["specialization"]

        if hospital:
            total_weight += weights["hospital"]
            if any(doctor['hospital_name'] == hospital for doctor in primary_results):
                matched_weight += weights["hospital"]

        if day:
            total_weight += weights["day"]
            if any(day in doctor['availability_days'] for doctor in primary_results):
                matched_weight += weights["day"]

        if time:
            total_weight += weights["time"]
            if any(
                doctor['availability_hours'].get(day, {}).get('start', '00:00') <= time <= 
                doctor['availability_hours'].get(day, {}).get('end', '23:59') for doctor in primary_results
            ):
                matched_weight += weights["time"]

        # Normalize confidence score
        return round(matched_weight / total_weight if total_weight > 0 else 0, 2)
