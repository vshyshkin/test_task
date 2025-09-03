import litellm
import os
import json
from typing import Any, Optional

from logging import getLogger

logger = getLogger(__name__)

class LLMProcessor:
    """
    A class to handle LLM requests for data extraction from text using LiteLLM.
    """
    
    def __init__(self, 
                 model: str = "gpt-4", 
                 api_key: Optional[str] = None):
        """
        Initialize the LLM processor with a specific model.
        
        Args:
            model (str): The model to use for data extraction (default: gpt-4)
            api_key (str, optional): API key for the LLM service. If None, will try to use environment variable.
        """
        self.model = model
        self.api_key = api_key

    async def extract_data(self, 
                    text: str, 
                    extraction_instructions: str,
                    output_format: Optional[dict[str, Any]] = None,
                    temperature: float = 0.0) -> dict[str, Any] | str:
        """
        Extract structured data from text based on user-specified instructions.
        
        Args:
            text (str): The text to extract data from
            extraction_instructions (str): Specific instructions about what data to extract
            output_format (dict, optional): Expected output format schema
            temperature (float): Model temperature setting (lower = more deterministic)
            
        Returns:
            Union[dict[str, Any], str]: Extracted data in the requested format
        """

        system_prompt = """
        You are a precise data extraction assistant. Extract only the specific information requested.
        Follow these guidelines:
        1. Extract exactly what is requested in the instructions
        2. Use the exact output format specified
        3. Only include information that is explicitly present in the text
        4. If requested information is not found, indicate with "Not found" or null values
        5. Do not make assumptions or add information not present in the text
        """
        
        user_message = f"""
        INSTRUCTIONS:
        {extraction_instructions}
        
        TEXT TO PROCESS:
        {text}
        """
        
        # Add output format instructions if provided
        if output_format:
            format_str = json.dumps(output_format, indent=2)
            user_message += f"""       
            OUTPUT FORMAT:
            Please return the extracted data in this exact JSON format:
            {format_str}
            """
        
        try:
            response = litellm.completion(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=temperature,
                api_key=self.api_key
            )
            
            # Extract the response content
            content = response.choices[0].message.content
            
            # If output_format was specified, try to parse as JSON
            if output_format:
                try:
                    return json.loads(content)
                except json.JSONDecodeError:
                    logger.warning("Failed to parse LLM response as JSON. Returning raw response.")
                    return content
            
            return content
            
        except Exception as e:
            logger.error(f"Error making LLM request: {str(e)}")
            raise
    
