from sanic import Blueprint
from sanic.response import json


common_bp = Blueprint("common")


@common_bp.route("/version")
async def get_version(request):
    """获取工具版本信息"""
    # TODO: 获取工具版本信息
    return json({})


@common_bp.route("/license")
async def get_license(request):
    """获取证书信息"""
    # TODO: 获取工具的证书信息
    return json({})
