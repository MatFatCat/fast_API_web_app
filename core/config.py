from starlette.config import Config

config = Config(".env")
DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str,
                    default="c336abc92a491bf7057d1f4f934cd798343ad9fdebaab7eef90df3176025d9ed")

