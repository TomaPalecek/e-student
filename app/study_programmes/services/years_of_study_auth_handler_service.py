import time
from typing import Dict

import jwt

from app.config import settings

YEARS_OF_STUDY_SECRET = settings.YEARS_OF_STUDY_SECRET
JWT_ALGORITHM = settings.ALGORITHM


def signJWT(id: str, role:str) -> Dict[str, str]:
    payload = {
        "id": id,
        "role": role,
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, YEARS_OF_STUDY_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, YEARS_OF_STUDY_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}