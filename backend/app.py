from sanic import Sanic

from backend import view


app = Sanic(__name__)
view.mount(app)  # 装载view层
