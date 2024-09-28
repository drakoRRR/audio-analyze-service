import uvicorn
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from sqladmin import Admin

from src.config import DEBUG
from src.calls.routers import call_router
from src.categories.routers import categories_router
from src.admin.auth import authentication_backend
from src.admin.models import CallAdmin, CategoryAdmin
from src.database import async_engine, async_session
from src.categories.utils import create_default_categories


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


@fastapi_app.on_event("startup")
async def startup_event():
    async with async_session() as db:
        await create_default_categories(db)


admin = Admin(fastapi_app, async_engine, authentication_backend=authentication_backend)

admin.add_view(CallAdmin)
admin.add_view(CategoryAdmin)


main_api_router = APIRouter()
fastapi_app.include_router(call_router, prefix="/api/call", tags=["Call"])
fastapi_app.include_router(categories_router, prefix="/api/category", tags=["Categories"])
fastapi_app.include_router(main_api_router)


if __name__ == "__main__":
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8080)
