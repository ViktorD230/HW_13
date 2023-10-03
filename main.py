from sqlalchemy import text
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from  routes import contacts, auth
from sqlalchemy.orm import Session
from database.db import get_db

app = FastAPI()

#route implementation using the routing mechanism
app.include_router(auth.router, prefix='/api')
app.include_router(contacts.router, prefix='/api')

#default route for the application
@app.get("/")
async def read_root():
    return {"message": "Welcome to FastApi"}


@app.get("/api/healthchecker/")
async def healthchecker(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome, connection established!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.7", port=8000)