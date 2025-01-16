# main.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from utils import fetch_query_response
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

#using langsmith for tracing
from langsmith import utils
utils.tracing_is_enabled()

class QueryRequest(BaseModel):
    query: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/query", response_class=JSONResponse)
async def process_query(request: QueryRequest):
    
    user_query = request.query
    response = fetch_query_response(user_query)
    return JSONResponse(content=response)
