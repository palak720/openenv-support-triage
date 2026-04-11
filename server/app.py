from fastapi import FastAPI
import uvicorn
from env.environment import SupportEnv
from graders import GRADERS
from tasks import TASKS

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


@app.get("/tasks")
def list_tasks():
    return {"tasks": TASKS}


@app.post("/grader")
def grade(payload: dict):
    task_id = payload.get("task_id") or payload.get("task")
    action = payload.get("action", {})
    reward = payload.get("reward")
    ground_truth = payload.get("ground_truth", {})

    if reward is not None:
        return {"score": float(reward)}

    grader = GRADERS.get(str(task_id))
    if grader is None:
        return {"score": 0.0, "error": f"Unknown task_id: {task_id}"}

    return {"score": float(grader(action, ground_truth))}


@app.get("/")
def home():
    return {"message": "OpenEnv Support Triage Running"}


def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
