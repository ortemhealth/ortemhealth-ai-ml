from fastapi import APIRouter, Body
router = APIRouter(prefix='/triage-symptoms', tags=["SymptomTriage"])

@router.post('/')
def triage(data: dict = Body(...)):
    # Example: data = {"symptoms": ["fever", "cough"], "duration_days": 4}
    # Dummy rules, replace with ML pipeline
    urgent = any(s in ["chest pain", "shortness of breath", "seizure"] for s in data["symptoms"])
    triage = "urgent" if urgent else "routine"
    specialist = "General Physician" if not urgent else "ER"
    return {"triage": triage, "suggested_specialist": specialist}
