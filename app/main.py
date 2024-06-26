from fastapi import FastAPI
from app.routers import products, brands, admin, users, permission,modules, user_management,role

app = FastAPI()

@app.get("/")
def root():
    return "Demo-Project"   

app.include_router(user_management.router)
app.include_router(users.router)
app.include_router(modules.router)
app.include_router(role.router)
app.include_router(permission.router)
app.include_router(brands.router)
app.include_router(products.router)

