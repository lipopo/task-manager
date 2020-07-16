from sanic import Blueprint


from backend.view.common import common_bp  # noqa: F401
from backend.view.task import task_bp  # noqa: F401
from backend.view.static import static_bp  # noqa: F401


def mount(app):
    bps = filter(
        lambda _module: isinstance(_module, Blueprint),
        globals().values())
    for bp in bps:
        app.blueprint(bp)
