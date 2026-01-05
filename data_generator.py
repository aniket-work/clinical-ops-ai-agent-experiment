import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_clinical_data(num_records=500):
    """
    Generates synthetic clinical trial data for the 'ClinicalOps AI Agent' experiment.
    Includes data points for: Patient ID, Age, Gender, Site ID, Enrollment Date,
    Adverse Events, and Vital Signs.
    """
    print("🔬 GENERATING SYNTHETIC CLINICAL TRIAL DATA...")

    # Seeds for reproducibility
    np.random.seed(42)
    random.seed(42)

    # 1. Demographics
    patient_ids = [f"PT-{str(i).zfill(4)}" for i in range(1, num_records + 1)]
    ages = np.random.randint(18, 85, size=num_records)
    genders = np.random.choice(['Male', 'Female', 'Non-Binary'], size=num_records, p=[0.48, 0.48, 0.04])
    site_ids = [f"SITE-{str(random.randint(101, 110))}" for _ in range(num_records)]

    # 2. Timeline
    start_date = datetime(2024, 1, 1)
    enrollment_dates = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(num_records)]

    # 3. Clinical Outcomes / Safety Data
    # Adverse Events (AE): None, Mild, Moderate, Severe
    ae_severity = np.random.choice(['None', 'Mild', 'Moderate', 'Severe'], size=num_records, p=[0.6, 0.25, 0.1, 0.05])
    
    # Vital Signs: Systolic BP (simulated correlation with age + random noise)
    systolic_bp = [int(110 + (age * 0.3) + np.random.normal(0, 10)) for age in ages]

    # Create DataFrame
    df = pd.DataFrame({
        'Patient_ID': patient_ids,
        'Site_ID': site_ids,
        'Age': ages,
        'Gender': genders,
        'Enrollment_Date': enrollment_dates,
        'Adverse_Event_Severity': ae_severity,
        'Systolic_BP': systolic_bp
    })

    # Save to CSV
    output_file = 'clinical_trial_data.csv'
    df.to_csv(output_file, index=False)
    print(f"✅ Data saved to {output_file}")
    print(f"   Shape: {df.shape}")
    print("\n   Sample Data:")
    print(df.head())

if __name__ == "__main__":
    generate_clinical_data()
