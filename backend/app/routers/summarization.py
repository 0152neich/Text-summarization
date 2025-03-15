from fastapi import APIRouter, HTTPException, Body, status
from fastapi.responses import JSONResponse
import logging
from app.models.summarization import APIInput, APIOutput
from app.utils.summarization import TextSummarizationModel, TextSummaryModelInput

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

text_summary = APIRouter(prefix="/v1")

# Init the summarization model
try:
    text_summary_service = TextSummarizationModel()
    logger.info("Text summarization model initialized successfully.")
except Exception as e:
    logger.error(f"Failed to initialize model: {str(e)}")
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to init model: {str(e)}")

# Define API input
@text_summary.post(
    '/summarize',
    response_model=APIOutput,
    responses={
        status.HTTP_200_OK: {
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Process successfully !!!',
                        'info': {
                            'text': '',
                        }
                    }
                }
            }
        },
        status.HTTP_400_BAD_REQUEST: {
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Bad request !!!',
                        'info': {
                            'text': '',
                        }
                    }
                }
            }
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Internal server error !!!',
                        'info': {
                            'text': '',
                        }
                    }
                }
            }
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Unprocessable entity !!!',
                        'info': {
                            'text': '',
                        }
                    }
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Not found !!!',
                        'info': {
                            'text': '',
                        }
                    }
                }
            }
        }
    }
)
async def summarize_text(inputs: APIInput = Body(...)):
    if not inputs.text:
        logger.warning("Bad request: Empty input text.")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request: Input text cannot be empty.")

    try:
        logger.info(f"Processing text: {inputs.text[:50]}{'...' if len(inputs.text) > 50 else ''}")
        # Summarize the text
        summary = text_summary_service.process(
            TextSummaryModelInput(text=inputs.text)
        )
        logger.info("Text summarized successfully.")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Process successfully !!!",
                "info": {
                    "text": summary.summary
                }
            }
        )
    except FileNotFoundError as e:
        logger.error(f"File not found error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"File error: {str(e)}")
    except ValueError as e:
        logger.error(f"Value error during processing: {str(e)}")
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Invalid input or processing error: {str(e)}")
    except RuntimeError as e:
        logger.error(f"Runtime error during inference: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Inference error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error during processing: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")