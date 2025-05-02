from fastapi import FastAPI
import random
import json


try:
    with open("public/quotes.json", "r") as f:
        AllQuotes = json.load(f)
except FileNotFoundError:
    raise Exception("quotes.json file not found. Please ensure it's deployed correctly.")


app = FastAPI()

@app.get('/')
def index():
    category = random.choice(list(AllQuotes.keys()))
    quote = random.choice(AllQuotes[category])
    return {"quote": quote["quote"], "writer": quote["writer"], "category": category}

@app.get("/categories")
def categories():
    return {"categories":list(AllQuotes.keys())}

@app.get("/blooming_love")
def blooming_love():
    quote = random.choice(AllQuotes["blooming_love"])
    return {"quote": quote["quote"], "writer": quote["writer"]}

@api.get("/wisdom")
def wisdom():
    quote = random.choice(AllQuotes["wisdom"])
    return {"quote": quote["quote"], "writer": quote["writer"]}

@app.get("/motivation")
def motivation():
    quote = random.choice(AllQuotes["motivation"])
    return {"quote": quote["quote"], "writer": quote["writer"]}

@app.get("/heartbreak")
def heartbreak():
    quote = random.choice(AllQuotes["heartbreak"])
    return {"quote": quote["quote"], "writer": quote["writer"]}

@app.get("/deep_love")
def deep_love():
    quote = random.choice(AllQuotes["deep_love"])
    return {"quote": quote["quote"], "writer": quote["writer"]}
