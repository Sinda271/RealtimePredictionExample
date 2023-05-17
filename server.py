from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from server_utils import pred_loop

class PredictionTrigger(BaseModel):
    trigger: str

app = FastAPI()

@app.get("/")
def index():
    return {"response": "Hello world!"}

# Get version
@app.get("/predict/get")
async def get_realtime_prediction():
    return StreamingResponse(
        content=pred_loop(),
        media_type="text/event-stream",
    )

# Post version
@app.post("/predict/post")
async def post_realtime_prediction(trigger: PredictionTrigger):

    t = trigger.trigger
    if t == "start":
        response = StreamingResponse(
            content=pred_loop(),
            media_type="text/event-stream",
        )
    else:
        response = {"response": "Realtime prediction stopped"}
    return response