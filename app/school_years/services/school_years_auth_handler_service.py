import time
from typing import Dict

import jwt

from app.config import settings

SCHOOL_YEAR_SECRET = settings.SCHOOL_YEAR_SECRET
JWT_ALGORITHM = settings.ALGORITHM


def signJWT(skg: str, role:str) -> Dict[str, str]:
    payload = {
        "skg": skg,
        "role": role,
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, SCHOOL_YEAR_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, SCHOOL_YEAR_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}