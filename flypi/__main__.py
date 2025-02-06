import uvicorn

from flypi.utils import env


def start():
    uvicorn.run(
        "flypi.utils.fastapi:app",
        host="0.0.0.0",
        port=env.port,
        log_level="info" if env.environment != "production" else "warning",
    )


if __name__ == "__main__":
    start()
