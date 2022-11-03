from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from backend.core.config import settings

from backend.apis.general_pages.route_homepage import general_pages_router

import os


def include_router(app):
    app.include_router(general_pages_router)


def configure_static(app):
    script_dir = os.path.dirname(__file__)
    st_abs_file_path = os.path.join(script_dir, "static/")
    app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")
    # app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    return app


app = start_application()
