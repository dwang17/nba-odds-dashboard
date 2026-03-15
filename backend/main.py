import os

from fastapi import FastAPI
import httpx
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("ODDS_API_KEY")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/moneylines") #returns moneyline data for nba games
async def get_top_stocks():
    url = f"https://api.the-odds-api.com/v4/sports/basketball_nba/odds?regions=us&markets=h2h,spreads,totals&oddsFormat=american&apiKey={API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return data

