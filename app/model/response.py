from pydantic import BaseModel, Field


class GreetResponse(BaseModel):
    name: str = Field(title='Name')

    def response_format(self):
        return {'message': f'Hello, {self.name}!'}
