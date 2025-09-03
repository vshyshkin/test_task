import io
import fitz

from logging import getLogger
logger = getLogger(__name__)

def extract_text_from_pdf_ocr(file_content):

    pdf_file = io.BytesIO(file_content)
    text_all = ""
    with fitz.open(stream=pdf_file, filetype="pdf") as doc:
        for page in doc:
            tp = page.get_textpage_ocr(
                language="eng",  
                dpi=300,
                full=True,
            )

            text = page.get_text("text", textpage=tp)

            text_all += text

    return text_all

def extract_text_from_pdf(file_content):
    """
    Extract text from a PDF file content.
    
    Args:
        file_content (bytes): The PDF file content as bytes
        
    Returns:
        str: Extracted text from the PDF
    """
    try:
        pdf_file = io.BytesIO(file_content)
        
        doc = fitz.open(stream=pdf_file, filetype="pdf")
        
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
            
        return text.strip()
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {str(e)}")
        raise Exception(f"Failed to extract text from PDF: {str(e)}")