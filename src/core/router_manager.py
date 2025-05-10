from aiogram import Router

import src.handlers.user.message as user_message
import src.handlers.user.callback as user_query
import src.handlers.admin.message as admin_message
import src.handlers.admin.callback as admin_query


def setup_routers():
    router = Router()

    routers = [user_message, user_query, admin_message, admin_query]

    for _router in routers:
        _router.register_handlers()

    router.include_routers(*[_router.router for _router in routers])

    return router
