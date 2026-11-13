# Docker for AI & ML

Practical, beginner-friendly examples for packaging Python applications and machine-learning models with Docker. Start with a small Flask container, add Redis as a second service with Docker Compose, then run an Iris classifier through a web interface.

<p align="center">
  <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" alt="Docker"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"></a>
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white" alt="Flask"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="Apache 2.0 License"></a>
</p>

## Contents

- [What you will learn](#what-you-will-learn)
- [Examples at a glance](#examples-at-a-glance)
- [Repository layout](#repository-layout)
- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
- [Run each example](#run-each-example)
- [Iris model details](#iris-model-details)
- [Common Docker commands](#common-docker-commands)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Connect with me](#connect-with-me)

## What you will learn

- Build a Docker image from a Python application and its `Dockerfile`.
- Publish a container port to your local machine.
- Run a Flask service alongside Redis using Docker Compose.
- Package a saved scikit-learn model and serve predictions from a Flask app.
- Rebuild images after changing application code or dependencies.

## Examples at a glance

| Example | What it demonstrates | Local address |
| --- | --- | --- |
| [Flask Hello World](flask-hello-world) | A minimal Flask app packaged as a Docker image | `http://localhost:5000` |
| [Flask + Redis Counter](flask-redis-counter) | A web service and Redis running together with Compose | `http://localhost:8000` |
| [Iris Classifier](iris-classifier) | A Flask UI that loads a scikit-learn model and predicts an Iris species | `http://localhost:5000` |

## Repository layout

```text
.
├── flask-hello-world/
├── flask-redis-counter/
├── iris-classifier/
│   ├── data/                     # Iris CSV data
│   ├── models/                  # Saved model used by the web app
│   ├── scripts/                 # Model training script
│   ├── static/                  # CSS and JavaScript
│   └── templates/               # Flask HTML template
├── LICENSE
└── README.md
```

Each example is self-contained and has its own `Dockerfile` and dependency list. Run Docker commands from that example's directory so the build context and relative paths are correct.

## Prerequisites

- [Docker Desktop](https://docs.docker.com/get-docker/) (Windows/macOS) or Docker Engine (Linux).
- Docker Compose v2, included with current Docker Desktop and available as `docker compose`.
- Git, if you are cloning this repository.

Check that Docker is installed and running:

```bash
docker --version
docker compose version
```

## Quick start

Clone the repository and enter the first example:

```bash
git clone https://github.com/Md-Emon-Hasan/Docker-for-AI-and-ML.git
cd Docker-for-AI-and-ML/flask-hello-world
```

Build and run the container:

```bash
docker build -t flask-hello-world .
docker run --rm -p 5000:5000 flask-hello-world
```

Open [http://localhost:5000](http://localhost:5000). Stop the running container with `Ctrl+C`.

## Run each example

### 1. Flask Hello World

This is the smallest example: one Flask route, a requirements file, and a Docker image.

```bash
cd flask-hello-world
docker build -t flask-hello-world .
docker run --rm -p 5000:5000 flask-hello-world
```

The app listens on port `5000` inside the container. The `-p 5000:5000` option maps it to port `5000` on your computer.

### 2. Flask + Redis Counter

Docker Compose starts both the Flask app and Redis. The app connects to Redis using the Compose service name `redis` and increments a counter for each page visit.

```bash
cd flask-redis-counter
docker compose up --build
```

Visit [http://localhost:8000](http://localhost:8000) and refresh to increment the counter. The Compose file maps host port `8000` to container port `5000`.

Stop and remove the containers and network with:

```bash
docker compose down
```

### 3. Iris Classifier

This example serves a saved Random Forest classifier through a Flask form. Enter sepal and petal measurements in centimeters to get a predicted species.

```bash
cd iris-classifier
docker build -t iris-classifier .
docker run --rm -p 5000:5000 iris-classifier
```

Open [http://localhost:5000](http://localhost:5000), enter all four measurements, and select **Predict**. The image includes `models/iris_model.pkl`, which the app loads at startup.

## Iris model details

The included training script trains a `RandomForestClassifier` on scikit-learn's built-in Iris dataset and saves the result to `models/iris_model.pkl`:

```bash
cd iris-classifier
python -m venv .venv
```

Activate the virtual environment, then install the example dependencies and train:

```bash
python -m pip install -r requirements.txt
python scripts/train_model.py
```

On Windows PowerShell, activate it with `.\.venv\Scripts\Activate.ps1`; on macOS/Linux, use `source .venv/bin/activate`.

The app expects the model file at `models/iris_model.pkl`. Rebuild the Docker image after training to include an updated model:

```bash
docker build -t iris-classifier .
```

> **Model file note:** `joblib`/pickle model files can execute code when loaded. Only load model files you created or otherwise trust.

## Common Docker commands

| Command | Purpose |
| --- | --- |
| `docker build -t NAME .` | Build an image from the current example directory |
| `docker image ls` | List local images |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers, including stopped ones |
| `docker logs CONTAINER` | View a container's output |
| `docker stop CONTAINER` | Stop a running container |
| `docker compose up --build` | Build and start services declared in Compose |
| `docker compose down` | Stop and remove Compose containers and network |

## Troubleshooting

- **Docker cannot connect to the daemon:** Start Docker Desktop or the Docker service, then retry.
- **Port is already in use:** Choose another host port, for example `-p 5001:5000`, and open `http://localhost:5001`.
- **The Iris app cannot find its model:** Build and run from `iris-classifier`; make sure `models/iris_model.pkl` exists.
- **The Redis example cannot connect:** Start it with `docker compose up --build` from `flask-redis-counter`. The app expects the Compose service hostname `redis`.
- **Changes do not appear in the container:** Rebuild the image with `docker build --no-cache -t NAME .` or use `docker compose up --build`.

## Contributing

Issues, corrections, and new examples are welcome. To contribute:

1. Fork the repository and create a branch for your change.
2. Keep each example self-contained with its own Docker configuration and dependencies.
3. Update this README when adding or changing an example.
4. Open a pull request describing the change and how to run it.

For bugs or ideas, [open an issue](https://github.com/Md-Emon-Hasan/Docker-for-AI-and-ML/issues).

## License

This project is distributed under the [Apache License 2.0](LICENSE).

## Connect with me

- 🌐 **Portfolio:** [emonlabs-ai.hitechparks.com](https://emonlabs-ai.hitechparks.com)
- 💻 **GitHub:** [Md-Emon-Hasan](https://github.com/Md-Emon-Hasan)
- 💼 **LinkedIn:** [Md Emon Hasan](https://www.linkedin.com/in/md-emon-hasan-695483237/)
- 🤗 **Hugging Face:** [emonHasan01](https://huggingface.co/emonHasan01)
- 📧 **Email:** [emon.mlengineer@gmail.com](mailto:emon.mlengineer@gmail.com)
- 📱 **WhatsApp:** [+880 1834-363533](https://wa.me/8801834363533)
