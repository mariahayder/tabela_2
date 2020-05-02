import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.on_event("startup")
async def startup():
    app.db_connection = sqlite3.connect('chinook.db')


@app.on_event("shutdown")
async def shutdown():
    app.db_connection.close()



@app.get("/tracks/composers/{composer_name}")
async def root(composer_name: str):
    if composer_name==null:
        raise HTTPException(status_code=404, detail="no composer given")
    cursor = app.db_connection.cursor()
    data = app.db_connection.execute("SELECT name FROM tracks WHERE composer={composer_name} ORDER BY name").fetchall()
    return data


@app.get("/tracks/composers/")
async def root():
    raise HTTPException(status_code=404, detail="no composer given")





