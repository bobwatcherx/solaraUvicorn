from fastapi import FastAPI
import solara.server.fastapi

app = FastAPI()

@app.get("/")
def home():
	return {"hello":"sample home"}

# AND NOW FOR url /solara this solara will run
app.mount("/solara/",app=solara.server.fastapi.app)

# AND NOW YOU CREATE FILE sol.py FOR SOLARA CODE
