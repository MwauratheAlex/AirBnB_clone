from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetimr.now()

    def __str__(self):
        pass

    def save(self):
        pass

    def to_dict(self):
        pass

