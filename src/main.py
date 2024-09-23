import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.config import DEBUG


def create_app():
    fast_api_app = FastAPI(
        debug=bool(DEBUG),
        docs_url="/api/docs/",
    )

    fast_api_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return fast_api_app


fastapi_app = create_app()


if __name__ == "__main__":
    uvicorn.run(fastapi_app, host="0.0.0.0", port=5000)