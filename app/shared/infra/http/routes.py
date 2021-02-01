from fastapi import APIRouter

from ....modules.user.infra.http.routes.user import user_routes
from ....modules.user.infra.http.routes.session import session_routes

from ....modules.debit.infra.http.routes.debit import debit_routes


routes = APIRouter()

routes.include_router(user_routes, prefix='/user', tags=['user'])
routes.include_router(session_routes, prefix='/session', tags=['session'])
routes.include_router(debit_routes, prefix='/debit', tags=['debit'])
