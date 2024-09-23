import uvicorn
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from src.config import DEBUG
from src.calls.routers import call_router
from src.categories.routers import categories_router


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

main_api_router = APIRouter()
fastapi_app.include_router(call_router, prefix="/call", tags=["Call"])
fastapi_app.include_router(categories_router, prefix="/category", tags=["Categories"])
fastapi_app.include_router(main_api_router)


if __name__ == "__main__":
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8080)
