# Expert System for Hospital Doctor Availability

This is a Python-based system designed to manage and query hospital and doctor availability. It uses a knowledge base of hospitals and doctors to facilitate efficient scheduling and patient management.

## Features

- **Hospital Management**:
  - Database of hospitals with their locations and specialties.
  - Retrieval of hospital names and specializations.

- **Doctor Management**:
  - Comprehensive database of doctors with details including:
    - Name, specialization, and contact information.
    - Availability (days and hours).
    - Maximum patients per day and current patients count.
    - Consultation duration.
  - Dynamic checks for doctor availability and capacity.

- **Expert System Integration**:
  - Utilizes the [Experta](https://github.com/experta/experta) library for managing `Fact`-based inference.
  - Converts doctor information into `DoctorAvailability` facts for decision-making.

## Knowledge Base

The system includes the following datasets:
1. **Hospitals**:
   - Information about each hospital, including `hospital_id`, `name`, `location`, and medical specialties offered.

2. **Doctors**:
   - Detailed records of doctors, including their specialization, affiliated hospital, availability schedule, and patient capacity.

## Requirements

- Python 3.8+
- Required libraries:
  - `experta`

Install dependencies using:

```bash
pip install experta
