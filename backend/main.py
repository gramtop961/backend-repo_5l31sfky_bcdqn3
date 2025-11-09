from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from database import create_document, db
from schemas import ContactMessage

app = FastAPI(title="VitalEdge API", version="1.0.0")

# Allow frontend origin during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "ok", "service": "vitaledge-api"}


@app.get("/test")
async def test_db():
    try:
        # Attempt a basic command to validate connection
        names = db.list_collection_names() if db is not None else []
        return {"database": "connected", "collections": names}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/contact")
async def submit_contact(payload: ContactMessage):
    try:
        doc_id = create_document("contactmessage", payload)
        return {"success": True, "id": doc_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
