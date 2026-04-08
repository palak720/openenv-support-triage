
from fastapi import FastAPI
import uvicorn
from env.environment import SupportEnv

app = FastAPI()
env = SupportEnv()


@app.post("/reset")
def reset():
    obs = env.reset()

    return {
        "observation": obs,
        "reward": 0.0,
        "done": False,
        "info": {}
    }


@app.post("/step")
def step(action: dict):
    obs, reward, done, info = env.step(action)

    return {
        "observation": obs,
        "reward": float(reward),
        "done": bool(done),
        "info": info if info else {}
    }


@app.get("/")
def home():
    return {"message": "OpenEnv Support Triage Running"}


def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()