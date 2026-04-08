# OpenEnv Support Triage

OpenEnv Support Triage is a small support-ticket simulation environment built for agent evaluation. It exposes a FastAPI server, task definitions, deterministic graders, and baseline agents for triage workflows such as category prediction, priority assignment, and response generation.

## Links

- Repository: https://github.com/palak720/openenv-support-triage
- Live demo: https://huggingface.co/spaces/Palakguptaaa/openenv-support-triage
- Swagger API docs: https://palakguptaaa-openenv-support-triage.hf.space/docs

## Technologies Used

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- OpenEnv
- Docker
- Hugging Face Spaces
- Requests
- OpenAI Python SDK

## What This Repo Includes

- An environment that simulates incoming customer support tickets
- API endpoints for `reset` and `step`
- Easy, medium, and hard task definitions
- Deterministic grading logic
- Baseline and advanced agent examples
- Docker and Python packaging for deployment

## Project Layout

This section describes each source and project file in the repository. Generated files such as `venv/` and `__pycache__/` are not part of the hand-written project structure.

### Root Files

- `README.md`: Project documentation and setup guide
- `pyproject.toml`: Python package metadata, dependencies, and CLI entry points (`server` and `start`)
- `requirements.txt`: Pip-compatible dependency list
- `uv.lock`: Lockfile for reproducible installs with `uv`
- `Dockerfile`: Container build instructions
- `openenv.yaml`: OpenEnv project configuration
- `inference.py`: Inference or evaluation entry script for the environment
- `leaderboard.json`: Stored leaderboard or score summary data
- `.gitignore`: Git ignore rules

### Server

- `server/__init__.py`: Marks `server` as a Python package
- `server/app.py`: FastAPI application, API routes, and `main()` server entry point

### Environment

- `env/__init__.py`: Marks `env` as a Python package
- `env/data.py`: Ticket or environment data helpers
- `env/environment.py`: Main support-triage environment logic
- `env/graders.py`: Shared grading utilities used by the environment
- `env/models.py`: Data models for observations, actions, or related objects
- `env/reward.py`: Reward calculation logic

### Agents

- `agent/__init__.py`: Marks `agent` as a Python package
- `agent/baseline.py`: Baseline support-triage agent
- `agent/advanced_agent.py`: More advanced agent implementation

### Graders

- `graders/__init__.py`: Marks `graders` as a Python package
- `graders/easy_grader.py`: Grader for the easy task
- `graders/medium_grader.py`: Grader for the medium task
- `graders/hard_grader.py`: Grader for the hard task

### Tasks

- `tasks/__init__.py`: Marks `tasks` as a Python package
- `tasks/easy_task.py`: Easy task definition
- `tasks/medium.py`: Medium task definition
- `tasks/hard_task.py`: Hard task definition

### Logs

- `logs/run_logs.json`: Run history or evaluation logs

## API

The FastAPI app lives in `server/app.py`.

Available endpoints:

- `GET /`: Health check
- `POST /reset`: Reset the environment and return the initial observation
- `POST /step`: Submit an action and receive the next observation, reward, and done flag

## Local Development

### Option 1: pip

```bash
pip install -r requirements.txt
python -m uvicorn server.app:app --reload --host 0.0.0.0 --port 7860
```

### Option 2: package entry point

After installing the project as a package, you can run either script entry point:

```bash
server
```

or

```bash
start
```

Both commands map to `server.app:main`.

## Docker

```bash
docker build -t openenv-support-triage .
docker run -p 7860:7860 openenv-support-triage
```

## Notes

- The package now exposes a `server` script for multi-mode deployment compatibility.
- If you add new source files later, this README should be updated so the file list stays accurate.
