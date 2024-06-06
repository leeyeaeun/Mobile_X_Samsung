from typing import Literal

from pydantic import BaseModel, Field
                # # About Course
                # * Course Name: {model.course_name}
                # * Desired Field: {model.course_field}
                # * Grade: {model.grade}

                # # Environments
                # * Target Language: {model.language}

class InputModel(BaseModel):
    target_course: str = Field(
        default='꿀교양!',
    )
    course_field: Literal[
        '철학',
        '문학',
        '예술',
        '역사',
        '경제',
        '심리학',
        '경영',
    ] = Field(
        default='철학',
    )
    grade: Literal[
        'Freshman (1st grade)',
        'Sophomore (2nd grade)',
        'Junior (3rd grade )',
        'Senior (4th grade)',
    ] = Field(
        default='Freshman (1st grade)',
    )
    language: Literal[
        'English',
        'Korean',
    ] = Field(
        default='Korean',
    )

    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='Expected Questions',
    )
