from dotenv import load_dotenv
import os

load_dotenv()

TOKEN: str = os.getenv("TOKEN") # type: ignore
ADMIN: str = os.getenv("ADMIN") # type: ignore

SCREENSHOT_PATH: str = os.getenv("SCREENSHOT_PATH") # type: ignore

if not all([TOKEN, ADMIN, SCREENSHOT_PATH]):
    raise ValueError("Missing TOKEN (bot), SCREENSHOT_PATH or ADMIN (user_id) in .env variables")