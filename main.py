from fastapi import FastAPI
from routers import user_routes, form_routes
from database import user_collection


app = FastAPI()


@app.get("/")
async def check_conection():
    try:
        count = user_collection.count_documents({})
        return {"status": "Conect to MongoDB", "usuarios": count}
    except Exception as e:
        return {"error": str(e)}
app.include_router(user__routes.router)
app.include_router(form__routes.router)