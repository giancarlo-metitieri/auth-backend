from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth.crypto import hash_password, verify_password
from auth.dto import AccessRequest, SignupRequest, GetUserRequest
from auth.permissions import maybe_get_permission_from_str
from auth.roles import can_role_do
from auth.token_utils import create_access_token, verify_access_token
from auth.model import User, SessionLocal
from datetime import timedelta
from auth.model import Base, engine
from config.roles import PreDefinedRoles
from auth.predefined_user import predefined_users_list

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to create default roles
def create_default_roles():
    db = SessionLocal()
    for u in predefined_users_list:
        user = db.query(User).filter(User.username == u['username']).first()
        if not user:
            new_user = User(username=u['username'], hashed_password=hash_password(u['password']), roles=u['roles'])
            db.add(new_user)
    db.commit()
    db.close()

def get_admin_role_str():
    return str(PreDefinedRoles.ADMIN).split(".")[1].lower()

def is_user_admin(roles):
    return get_admin_role_str() in roles




@app.on_event("startup")
def startup_event():
    create_default_roles()
    Base.metadata.create_all(bind=engine)

# Sign Up Endpoint
@app.post("/signup")
def signup(req: SignupRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == req.username).first()
    if user:
        raise HTTPException(status_code=400, detail="User Already exists")

    hashed_password = hash_password(req.password)
    user = User(username=req.username, hashed_password=hashed_password, roles=["student"])
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully", "username": user.username}


# Login Endpoint
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Access Denied")

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Refresh Token Endpoint
@app.post("/refresh-token")
def refresh_token(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    new_token = create_access_token(data={"sub": payload["sub"], "role": payload["role"]})
    return {"access_token": new_token}

@app.get("/data")
def get_user(request: GetUserRequest, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=403, detail="Access denied")
    request_username = str(payload.get("sub"))

    user = db.query(User).filter(User.username == request_username).first()
    if not user:
        raise HTTPException(status_code=403, detail="Access Denied")
    if request.username == request_username or is_user_admin(user.roles):
        return {"id": str(user.id), "username": str(user.username), "is_active": bool(user.is_active), "roles": list(user.roles)}
    return {"message": "Access Denied"}

@app.get("/permission")
def can_user_do(request: AccessRequest,token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=403, detail="Access denied")
    username: str = payload.get("sub")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=403, detail="Access Denied")
    roles: list[str] = user.roles
    permission = maybe_get_permission_from_str(request.permission)
    if not permission:
        return {"result": False}
    for r in roles:
        if can_role_do(r, permission) or r == get_admin_role_str():
            return {"result": True}

    return {"result": False}

