from fastapi import APIRouter, HTTPException
from core.config import settings
from core.llm_processor import LLMProcessor
from logging import getLogger

logger = getLogger(__name__)


router = APIRouter(
    prefix="/llm_processor",
    tags=["llm_processor"]
)

@router.post("/process-text")
async def process_text(text: str, 
                       extraction_instructions: str,
                       model: str):
    try:
        llm_processor = LLMProcessor(
            model=model,
            api_key=settings.LLM_API_KEY
        )
        result = await llm_processor.extract_data(text=text,
                                                  extraction_instructions=extraction_instructions,
                                                  output_format={"format": "json"})
        return {"result": result}
    except Exception as e:
        logger.error(f"Error processing text: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))