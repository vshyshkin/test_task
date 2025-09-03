from fastapi import APIRouter, UploadFile, File, HTTPException
from core.pdf_processor import extract_text_from_pdf, extract_text_from_pdf_ocr
from logging import getLogger

logger = getLogger(__name__)

router = APIRouter(
    prefix="/pdf_processor",
    tags=["pdf_processor"]
)


@router.post("/extract-text-ocr")
async def extract_text_ocr(file: UploadFile = File(...)):
    """
    Extracts text from a scanned PDF file using OCR.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="File must be a PDF"
        )

    try:
        file_content = await file.read()
        extracted_text = extract_text_from_pdf_ocr(file_content)

        return {"filename": file.filename, "text": extracted_text}
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to extract text from PDF: {str(e)}"
        )

@router.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):
    """
    Extracts text from a PDF file.
    
    Args:
        file: The PDF file to extract text from
        
    Returns:
        dict: A dictionary containing the extracted text
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="File must be a PDF"
        )
    
    try:
        file_content = await file.read() 
        extracted_text = extract_text_from_pdf(file_content)
        
        return {"filename": file.filename, "text": extracted_text}
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to extract text from PDF: {str(e)}"
        )