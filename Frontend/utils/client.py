import httpx
from pydantic import BaseModel, Field, ValidationError
from pydantic_core import Url
from typing import Type, Optional

# class MobileXClient(BaseModel):
#     base_url: Url = Field(
#         default=Url('http://localhost:8000'),
#     )

#     def call(self, function: str, input: BaseModel, output_model: Type[BaseModel]) -> Optional[BaseModel]:
#         try:
#             response = httpx.post(
#                 url=f'{self.base_url}/func/{function}',
#                 json=input.dict(),  # Pydantic v1: input.dict() / Pydantic v2: input.model_dump()
#                 timeout=300.0,
#             )
#             response.raise_for_status()  # HTTP 상태 코드가 200이 아니면 예외를 발생시킵니다.

#             # 응답 내용 확인 및 디버깅 출력
#             print(f"응답 상태 코드: {response.status_code}")
#             print(f"응답 내용: {response.text}")

#             try:
#                 data = response.json()
#             except httpx.JSONDecodeError as json_err:
#                 print(f"JSON 디코딩 오류 발생: {json_err}")
#                 print(f"응답 내용: {response.text}")
#                 return None

#             return output_model.parse_obj(data)  # Pydantic v1: parse_obj / Pydantic v2: model_validate

#         except httpx.HTTPStatusError as http_err:
#             print(f"HTTP 오류 발생: {http_err}")
#             print(f"응답 내용: {response.text}")
#         except httpx.RequestError as req_err:
#             print(f"요청 오류 발생: {req_err}")
#         except ValidationError as val_err:
#             print(f"모델 검증 오류 발생: {val_err}")

#         return None  # 오류가 발생한 경우 None을 반환합니다.

import httpx
from pydantic import BaseModel, Field
from pydantic_core import Url


class MobileXClient(BaseModel):
    base_url: Url = Field(
        default=Url('http://localhost:8000'),
    )

    def call[To: BaseModel](
        self,
        function: str,
        input: BaseModel,
        output_model: type[To],
    ) -> To | None:
        response = httpx.post(
            url=f'{self.base_url}func/{function}',
            json=input.model_dump(),
            timeout=300.0,
        )
        data = response.json()
        if data is None:
            return None
        
        return output_model.model_validate(data)
