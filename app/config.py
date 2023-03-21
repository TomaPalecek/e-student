from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_HOSTNAME: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    USER_SECRET: str
    # SUPER_USER_SECRET: str
    # CLASSIC_USER_SECRET: str
    ALGORITHM: str


    # SCHOOL_YEAR_SECRET: str
    # YEARS_OF_STUDY_SECRET: str
    DB_NAME_TEST: str

    class Config:
        env_file = "./.env"


settings = Settings()
