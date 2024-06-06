from pydantic import BaseModel, Field, AnyUrl

class ImagePreviewModel(BaseModel):
    image_url: AnyUrl = Field(
        description='컷신', 
    )
