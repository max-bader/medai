from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import io
from app.database import forms_collection
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/upload")
async def upload_form(file: UploadFile = File(...)):
    try:
        # Read the uploaded file
        contents = await file.read()
        
        # Convert to PIL Image
        image = Image.open(io.BytesIO(contents))
        
        # Perform OCR
        text = pytesseract.image_to_string(image)
        
        # Generate unique ID for the form
        form_id = str(uuid.uuid4())
        
        # Store in database
        form_data = {
            "form_id": form_id,
            "filename": file.filename,
            "upload_date": datetime.utcnow(),
            "original_text": text,
            "status": "processed"
        }
        
        await forms_collection.insert_one(form_data)
        
        return JSONResponse(
            status_code=200,
            content={
                "message": "Form uploaded and processed successfully",
                "form_id": form_id,
                "extracted_text": text
            }
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing form: {str(e)}"
        ) 