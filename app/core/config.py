from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "X-Ray Disease Classifier"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/v1"
    MODEL_PATH: str = "app/models"
    UPLOAD_FOLDER: str = "uploads"
    MAX_CONTENT_LENGTH: int = 16 * 1024 * 1024  # 16MB max file size

    class Config:
        case_sensitive = True

settings = Settings() 