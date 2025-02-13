from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret-key"
ALGORITHM = "HS256"

payload = {
    "sub": "user123",  # user identifier
    "exp": datetime.utcnow() + timedelta(hours=1)  # expiration time
}

token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print(token)