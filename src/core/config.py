from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional, List
from enum import Enum

class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "Intelligent Collections Agent"
    VERSION: str = "1.0.0"
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"

    # Security
    SECRET_KEY: str = Field(default="change-this-in-production", min_length=32)
    API_KEY_HEADER: str = "X-API-Key"
    API_KEYS: List[str] = Field(default=["dev-key-1", "dev-key-2"])
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 30
    CORS_ORIGINS: List[str] = ["*"]

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None
    REDIS_SSL: bool = False
    REDIS_MAX_CONNECTIONS: int = 50
    CACHE_TTL: int = 3600  # 1 hour
    CACHE_PREFIX: str = "collections:"

    # Database
    DATABASE_URL: str = "postgresql://user:pass@localhost:5432/collections"
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 10
    DB_POOL_TIMEOUT: int = 30
    DB_ECHO: bool = False
    DB_POOL_PRE_PING: bool = True

    # LangChain/LangGraph
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    MODEL_PROVIDER: str = "openai"  # openai, anthropic
    MODEL_NAME: str = "gpt-4-turbo-preview"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    TEMPERATURE: float = 0.1
    MAX_TOKENS: int = 2000
    REQUEST_TIMEOUT: int = 60

    # Monitoring
    ENABLE_METRICS: bool = True
    METRICS_PORT: int = 9090
    SENTRY_DSN: Optional[str] = None
    SENTRY_TRACES_SAMPLE_RATE: float = 1.0
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"

    # Communication
    SMS_PROVIDER: str = "twilio"
    EMAIL_PROVIDER: str = "sendgrid"
    WHATSAPP_PROVIDER: str = "twilio"

    # Twilio
    TWILIO_ACCOUNT_SID: Optional[str] = None
    TWILIO_AUTH_TOKEN: Optional[str] = None
    TWILIO_PHONE_NUMBER: Optional[str] = None
    TWILIO_WHATSAPP_NUMBER: Optional[str] = None

    # SendGrid
    SENDGRID_API_KEY: Optional[str] = None
    SENDGRID_FROM_EMAIL: Optional[str] = None
    SENDGRID_FROM_NAME: str = "Collections Team"

    # Business Rules
    MAX_DELINQUENCY_DAYS_BEFORE_LEGAL: int = 90
    MIN_PAYMENT_PLAN_AMOUNT: float = 10.0
    MAX_PAYMENT_PLAN_MONTHS: int = 12
    RISK_THRESHOLD_HIGH: float = 0.7
    RISK_THRESHOLD_CRITICAL: float = 0.9
    COMMUNICATION_ATTEMPT_LIMIT: int = 3
    COMMUNICATION_COOLDOWN_HOURS: int = 24

    # Workers
    WORKER_CONCURRENCY: int = 10
    WORKER_MAX_RETRIES: int = 3
    WORKER_RETRY_DELAY_SECONDS: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


settings = Settings()
