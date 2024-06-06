# FastAPI 라우터 설정
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from llm.chat import build
from llm.store import LLMStore
from models.course_recommend import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

class ErrorResponse(BaseModel):
    detail: str

###############################################
#                   Actions                   #
###############################################

@router.post(f'/func/{NAME}', response_model=OutputModel, responses={500: {"model": ErrorResponse}})
async def call_acrostic_generator(model: InputModel) -> OutputModel:
    try:
        # 입력 데이터 디버깅 출력
        print(f"Received input: {model}")

        # Create a LLM chain
        chain = build(
            name=NAME,
            llm=store.get(model.llm_type),
        )

        result = chain.invoke({
            'input_context': f'''
                # About Course
                * Desired Field: {model.course_field}
                * Grade: {model.grade}

                # Environments
                * Target Language: {model.language}
            ''',
        })

        # 결과 디버깅 출력
        print(f"Generated output: {result}")

        return OutputModel(output=result)

    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"JSON 디코딩 오류: {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"오류 발생: {e}")
    
    import requests
import json



