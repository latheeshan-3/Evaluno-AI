# --------------------------- user_service.py ---------------------------
import bcrypt
bcrypt.__about__ = type('obj', (), {'__version__': '4.3.0'})  # workaround

from passlib.hash import bcrypt as passlib_bcrypt
from datetime import datetime, timedelta
from fastapi import HTTPException
from database.connection import get_db
from schemas.user import UserCreate, UserLogin
from utils.helpers import create_access_token

db = get_db()
users_collection = db["users"]

# --------------------------- Password helpers ---------------------------
from passlib.context import CryptContext

# Force modern bcrypt variant
pwd_context = CryptContext(
    schemes=["bcrypt"],
    bcrypt__ident="2b",
    bcrypt__rounds=12,
    deprecated="auto"
)

def truncate_password(password: str, max_bytes: int = 72) -> str:
    """Truncate string so that its UTF-8 encoding is at most max_bytes."""
    encoded = password.encode("utf-8")
    if len(encoded) <= max_bytes:
        return password
    # truncate safely without breaking multibyte chars
    truncated = encoded[:max_bytes]
    while True:
        try:
            return truncated.decode("utf-8")
        except UnicodeDecodeError:
            truncated = truncated[:-1]

def hash_password(password: str) -> str:
    safe_password = truncate_password(password)
    return pwd_context.hash(safe_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    safe_password = truncate_password(plain_password)
    return pwd_context.verify(safe_password, hashed_password)

# --------------------------- Async functions ---------------------------
async def create_user(user: UserCreate) -> str:
    existing = await users_collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)

    result = await users_collection.insert_one(user_dict)
    return str(result.inserted_id)

async def authenticate_user(data: UserLogin) -> str:
    user = await users_collection.find_one({"email": data.email})
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_data = {
        "sub": user["email"],
        "username": user.get("username"),
        "user_type": user.get("user_type"),
        "user_id": str(user["_id"])
    }
    token = create_access_token(token_data)
    return token
