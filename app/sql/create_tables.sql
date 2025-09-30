-- =========================================
-- Tabla: patient
-- =========================================
CREATE TABLE IF NOT EXISTS patient (
    document_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(20) NOT NULL,
    race VARCHAR(20),
    region VARCHAR(20),
    urban_or_rural VARCHAR(10),
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50),
    address TEXT,
    created TIMESTAMP WITH TIME ZONE DEFAULT timezone('America/Bogota', now()) NOT NULL,
    edited TIMESTAMP WITH TIME ZONE DEFAULT timezone('America/Bogota', now()) NOT NULL
);

CREATE OR REPLACE FUNCTION update_patient_edited_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.edited = timezone('America/Bogota', now());
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS set_patient_edited_timestamp ON patient;

CREATE TRIGGER set_patient_edited_timestamp
BEFORE UPDATE ON patient
FOR EACH ROW
EXECUTE FUNCTION update_patient_edited_column();


-- =========================================
-- Tabla: clinical_histories
-- =========================================
CREATE TABLE IF NOT EXISTS clinical_histories (
    id SERIAL PRIMARY KEY,
    document_id VARCHAR(50) NOT NULL REFERENCES patient(document_id) ON DELETE CASCADE,
    -- Family and personal history
    family_history VARCHAR(10),
    previous_cancer_history VARCHAR(10),
    -- Diagnosis information
    stage_at_diagnosis VARCHAR(10) NOT NULL,
    tumor_aggressiveness VARCHAR(10) NOT NULL,
    -- Screening and access
    colonoscopy_access VARCHAR(10),
    screening_regularity VARCHAR(20),
    -- Lifestyle factors
    diet_type VARCHAR(20),
    bmi DECIMAL(5,2),
    physical_activity_level VARCHAR(20),
    smoking_status VARCHAR(20),
    alcohol_consumption VARCHAR(20),
    fiber_consumption VARCHAR(20),
    insurance_coverage VARCHAR(10),
    -- Treatment information
    time_to_diagnosis VARCHAR(20),
    treatment_access VARCHAR(20) NOT NULL,
    treatment_id INT,
    chemotherapy_received VARCHAR(10),
    radiotherapy_received VARCHAR(10),
    surgery_received VARCHAR(10),
    treatment_recommendation VARCHAR(10),
    -- Follow-up and outcomes
    follow_up_adherence VARCHAR(10) NOT NULL,
    recurrence VARCHAR(10),
    time_to_recurrence INT,
    created TIMESTAMP WITH TIME ZONE DEFAULT timezone('America/Bogota', now()) NOT NULL,
    edited TIMESTAMP WITH TIME ZONE DEFAULT timezone('America/Bogota', now()) NOT NULL
);

CREATE OR REPLACE FUNCTION update_clinical_histories_edited_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.edited = timezone('America/Bogota', now());
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS set_clinical_histories_edited_timestamp ON clinical_histories;

CREATE TRIGGER set_clinical_histories_edited_timestamp
BEFORE UPDATE ON clinical_histories
FOR EACH ROW
EXECUTE FUNCTION update_clinical_histories_edited_column();


-- =========================================
-- Índices para optimizar consultas
-- =========================================
CREATE INDEX IF NOT EXISTS idx_patient_document_id 
ON patient(document_id);

CREATE INDEX IF NOT EXISTS idx_clinical_histories_document_id 
ON clinical_histories(document_id);
