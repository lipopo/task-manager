from sanic import Blueprint
from sanic.response import json


task_bp = Blueprint("task")


@task_bp.route("/tasks")
async def get_tasks(request):
    """获取任务列表"""
    # TODO: 设置任务获取流程
    return json({})


@task_bp.route("/task")
async def get_task(request):
    """获取任务详情"""
    # TODO: 设置获取任务详情
    return json({})


@task_bp.route("/task", methods=["POST"])
async def create_task(request):
    """任务创建"""
    # TODO: 创建任务流程
    return json({})


@task_bp.route("/task", methods=["PUT"])
async def update_task(request):
    """任务更新(幂等操作)"""
    # TODO: 创建任务更新流程
    return json({})


@task_bp.route("/task", methods=["PATCH"])
async def modify_task(request):
    """任务变更(非幂等操作)"""
    # TODO: 进行任务的变更操作
    return json({})


@task_bp.route("/task", methods=["DELETE"])
async def delete_task(request):
    """任务删除"""
    # TODO: 删除任务
    return json({})
