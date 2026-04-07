
from fastapi import FastAPI
from env.environment import SupportEnv
from env.models import Action

# default environment
env = SupportEnv(task="easy")  

app = FastAPI()
env = SupportEnv()

@app.get("/")
def home():
     return {"message": "OpenEnv Support Triage API Running 🚀"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()


@app.post("/step")
def step(action: Action):
    obs, reward, done, _ = env.step(action)

    return {
        "observation": obs.dict() if obs else None,
        "reward": reward,
        "done": done
    }


@app.get("/state")
def state():
    return env.state()