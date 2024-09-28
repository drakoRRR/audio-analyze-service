from sqladmin.authentication import AuthenticationBackend
from fastapi import Request

from src.config import SECRET_KEY, USER_ADMIN_LOGIN, USER_ADMIN_PASSWORD


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = str(form["username"]), str(form["password"])
        if username == USER_ADMIN_LOGIN and password == USER_ADMIN_PASSWORD:
            request.session.update({"token": USER_ADMIN_PASSWORD})

            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        return token == USER_ADMIN_PASSWORD


authentication_backend = AdminAuth(secret_key=SECRET_KEY)