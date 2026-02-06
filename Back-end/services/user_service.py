# --------------------------- user_service.py ---------------------------
from datetime import datetime, timedelta
from fastapi import HTTPException
from database.connection import get_db
from schemas.user import UserCreate, UserLogin
from utils.helpers import create_access_token
import hashlib
import secrets

db = get_db()
users_collection = db["users"]

# --------------------------- Password helpers ---------------------------
# Simple and reliable password hashing without passlib issues

def hash_password(password: str) -> str:
    """Hash password using PBKDF2 with SHA256."""
    # Generate a random salt
    salt = secrets.token_bytes(32)
    # Use PBKDF2 with 100,000 iterations
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    # Return salt + hash as a combined string (both hex-encoded)
    return f"{salt.hex()}${pwd_hash.hex()}"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against stored hash."""
    try:
        salt_hex, pwd_hash_hex = hashed_password.split('$')
        salt = bytes.fromhex(salt_hex)
        stored_hash = bytes.fromhex(pwd_hash_hex)
        # Recompute hash with the stored salt
        computed_hash = hashlib.pbkdf2_hmac('sha256', plain_password.encode(), salt, 100000)
        # Compare hashes (constant time comparison)
        return secrets.compare_digest(computed_hash, stored_hash)
    except (ValueError, AttributeError):
        return False

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
