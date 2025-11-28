from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from privacy.pseudonymize import pseudonymize_record
from dp.mechanisms import laplace_mechanism

app = FastAPI(title="Sanitized Privacy-Aware Health API")

class PatientRecord(BaseModel):
    patient_id: str
    age: int
    systolic_bp: int
    diastolic_bp: int
    diagnosis_code: str

@app.post("/ingest/")
async def ingest(record: PatientRecord):
    """Ingests a patient record and returns a pseudonymized version.
    This endpoint simulates server-side pseudonymization and lightweight DP.
    """
    # Pseudonymize identifiable elements
    pseudonym = pseudonymize_record(record.patient_id)
    # Apply a simple DP mechanism to numeric vitals (example)
    noisy_systolic = laplace_mechanism(record.systolic_bp, sensitivity=1.0, epsilon=1.0)
    noisy_diastolic = laplace_mechanism(record.diastolic_bp, sensitivity=1.0, epsilon=1.0)

    # Construct sanitized payload
    sanitized = {
        "pseudonym": pseudonym,
        "age": record.age,
        "systolic_bp": int(noisy_systolic),
        "diastolic_bp": int(noisy_diastolic),
        "diagnosis_code": record.diagnosis_code
    }

    return {"status": "ok", "sanitized_record": sanitized}

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "alive"}
