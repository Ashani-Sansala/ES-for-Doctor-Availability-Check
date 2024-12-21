import tkinter as tk
from tkinter import ttk, messagebox
from knowledge_base import get_hospital_names
from inference_engine import DoctorAvailabilityEngine

class DoctorAvailabilityApp:
    def __init__(self, master):
        self.master = master
        master.title("Doctor Availability Checker")
        master.geometry("900x800")  # Increased size to accommodate new results
        
        # Create inference engine
        self.engine = DoctorAvailabilityEngine()
        
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12))
        self.style.configure("Alternative.TLabel", foreground="dark blue")
        
        # Search Frame
        search_frame = ttk.LabelFrame(master, text="Search Doctors")
        search_frame.pack(padx=10, pady=10, fill="x")
        
        # Hospital Dropdown
        ttk.Label(search_frame, text="Hospital:").grid(row=0, column=0, padx=5, pady=5)
        self.hospital_var = tk.StringVar()
        hospitals = ["All"] + get_hospital_names()
        self.hospital_dropdown = ttk.Combobox(search_frame, 
                                              textvariable=self.hospital_var, 
                                              values=hospitals, 
                                              state="readonly")
        self.hospital_dropdown.set("All")
        self.hospital_dropdown.grid(row=0, column=1, padx=5, pady=5)
        
        # Specialization Dropdown
        ttk.Label(search_frame, text="Specialization:").grid(row=1, column=0, padx=5, pady=5)
        self.specialization_var = tk.StringVar()
        specializations = ["All"] + self.engine.all_specializations
        self.specialization_dropdown = ttk.Combobox(search_frame, 
                                                    textvariable=self.specialization_var, 
                                                    values=specializations, 
                                                    state="readonly")
        self.specialization_dropdown.set("All")
        self.specialization_dropdown.grid(row=1, column=1, padx=5, pady=5)
        
        # Day Dropdown
        ttk.Label(search_frame, text="Day:").grid(row=2, column=0, padx=5, pady=5)
        self.day_var = tk.StringVar()
        days = ["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.day_dropdown = ttk.Combobox(search_frame, 
                                         textvariable=self.day_var, 
                                         values=days, 
                                         state="readonly")
        self.day_dropdown.set("All")
        self.day_dropdown.grid(row=2, column=1, padx=5, pady=5)
        
        # Time Entry
        ttk.Label(search_frame, text="Time (HH:MM):").grid(row=3, column=0, padx=5, pady=5)
        self.time_var = tk.StringVar()
        self.time_entry = ttk.Entry(search_frame, textvariable=self.time_var)
        self.time_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Search Button
        search_button = ttk.Button(search_frame, text="Search", command=self.search_doctors)
        search_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Add Confidence Score Label
        self.confidence_label = ttk.Label(master, text="Confidence Score: N/A", font=("Arial", 14), foreground="green")
        self.confidence_label.pack(padx=10, pady=5)
        
        # Primary Results Frame
        primary_results_frame = ttk.LabelFrame(master, text="Available Doctors")
        primary_results_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Primary Results Tree
        self.primary_results_tree = ttk.Treeview(primary_results_frame, 
                                         columns=("Name", "Specialization", "Hospital", "Days", "Hours"), 
                                         show="headings")
        self.primary_results_tree.heading("Name", text="Name")
        self.primary_results_tree.heading("Specialization", text="Specialization")
        self.primary_results_tree.heading("Hospital", text="Hospital")
        self.primary_results_tree.heading("Days", text="Available Days")
        self.primary_results_tree.heading("Hours", text="Hours")
        
        self.primary_results_tree.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Alternative Results Frame
        alternative_results_frame = ttk.LabelFrame(master, text="Alternative Suggestions")
        alternative_results_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Alternative Results Label
        self.alternative_label = ttk.Label(alternative_results_frame, 
                                           text="No alternative suggestions found.",
                                           style="Alternative.TLabel")
        self.alternative_label.pack(padx=5, pady=5)
        
        # Alternative Results Tree
        self.alternative_results_tree = ttk.Treeview(alternative_results_frame, 
                                         columns=("Name", "Specialization", "Hospital", "Days", "Hours"), 
                                         show="headings")
        self.alternative_results_tree.heading("Name", text="Name")
        self.alternative_results_tree.heading("Specialization", text="Specialization")
        self.alternative_results_tree.heading("Hospital", text="Hospital")
        self.alternative_results_tree.heading("Days", text="Available Days")
        self.alternative_results_tree.heading("Hours", text="Hours")
        
        self.alternative_results_tree.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Book Appointment Button
        book_button = ttk.Button(master, text="Book Appointment", command=self.book_appointment)
        book_button.pack(padx=10, pady=10)
    
    def search_doctors(self):
        # Clear previous results
        for i in self.primary_results_tree.get_children():
            self.primary_results_tree.delete(i)
        for i in self.alternative_results_tree.get_children():
            self.alternative_results_tree.delete(i)
        
        # Get search parameters
        hospital = None if self.hospital_var.get() == "All" else self.hospital_var.get()
        spec = None if self.specialization_var.get() == "All" else self.specialization_var.get()
        day = None if self.day_var.get() == "All" else self.day_var.get()
        time = self.time_var.get() if self.time_var.get() else None

        # Search doctors
        results = self.engine.search_available_doctors(spec, hospital, day, time)
        
        # Populate primary results
        for doctor in results.get('primary_results', []):
            self.primary_results_tree.insert("", "end", values=(
                doctor['name'], 
                doctor['specialization'], 
                doctor['hospital_name'],
                ', '.join(doctor['availability_days']),
                ', '.join([f"{k}: {v['start']}-{v['end']}" for k, v in doctor['availability_hours'].items()])
            ), tags=(doctor['doctor_id'],))
        
        # Handle alternative results
        alt_results = results.get('alternative_results', [])
        alt_specs = results.get('alternative_specializations', [])
        
        if alt_results:
            if spec:
                alt_spec_str = ", ".join(alt_specs)
                self.alternative_label.config(text=f"No doctors found for {spec}. "
                                            f"Here are alternatives in: {alt_spec_str}")
            else:
                self.alternative_label.config(text="Alternative Suggestions:")
            
            for doctor in alt_results:
                self.alternative_results_tree.insert("", "end", values=(
                    doctor['name'], 
                    doctor['specialization'], 
                    doctor['hospital_name'],
                    ', '.join(doctor['availability_days']),
                    ', '.join([f"{k}: {v['start']}-{v['end']}" for k, v in doctor['availability_hours'].items()])
                ), tags=(doctor['doctor_id'],))
        else:
            if spec:
                self.alternative_label.config(text=f"No alternative doctors found for {spec}.")
            else:
                self.alternative_label.config(text="No alternative suggestions found.")
        
        # Calculate Confidence Score
        total_filters = 4
        num_filters_matched = 0

        # Check matches
        if spec and any(doctor['specialization'] == spec for doctor in results.get('primary_results', [])):
            num_filters_matched += 1
        if hospital and any(doctor['hospital_name'] == hospital for doctor in results.get('primary_results', [])):
            num_filters_matched += 1
        if day and any(day in doctor['availability_days'] for doctor in results.get('primary_results', [])):
            num_filters_matched += 1
        if time:
            for doctor in results.get('primary_results', []):
                day_hours = doctor['availability_hours'].get(day, {})
                if day_hours and (day_hours.get('start', '00:00') <= time <= day_hours.get('end', '23:59')):
                    num_filters_matched += 1
                    break
        
        # Adjust for alternatives
        penalty_for_alternatives = 20 if alt_results else 0
        confidence_score = max(0, (num_filters_matched / total_filters) * 100 - penalty_for_alternatives) if total_filters > 0 else 100

        # Display Confidence Score
        self.confidence_label.config(text=f"Confidence Score: {confidence_score:.2f}%")


    
    def book_appointment(self):
        # Try to book from primary results first
        selected_item = self.primary_results_tree.selection()
        tree_to_use = self.primary_results_tree
        
        # If no primary result selected, check alternative results
        if not selected_item:
            selected_item = self.alternative_results_tree.selection()
            tree_to_use = self.alternative_results_tree
        
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a doctor to book an appointment.")
            return
        
        doctor_id = tree_to_use.item(selected_item[0], 'tags')[0]
        
        if self.engine.book_appointment(doctor_id):
            messagebox.showinfo("Success", "Appointment booked successfully!")
        else:
            messagebox.showerror("Error", "Could not book appointment. Doctor's capacity is full.")

def main():
    root = tk.Tk()
    app = DoctorAvailabilityApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()