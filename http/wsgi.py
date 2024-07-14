import functools
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import ClosingIterator

def after_response_wrapper(app):
    """Wrap a WSGI application to call after_response hooks after we have responded.

    This is done to reduce response time by deferring expensive tasks."""

    @functools.wraps(app)
    def application(environ, start_response):
        return ClosingIterator(
            app(environ, start_response),
            (
                # print("Response has been sent."),
                some_cleanup_task,  # 假设你有一个清理任务
                some_cleanup_task2,
            ),
        )

    return application

@after_response_wrapper
@Request.application
def application(request: Request):
    response = Response("Hello, World!", mimetype='text/plain')
    # 处理请求的其他逻辑可以在这里添加
    if request.method == 'POST':
        response = Response("Received POST request", mimetype='text/plain')
    return response

from werkzeug.serving import run_simple

run_simple(
    "0.0.0.0",
    8085,  # 你可以根据需要更改端口
    application
)

def some_cleanup_task():
    # 清理任务的逻辑
    print("Performing cleanup task")

def some_cleanup_task2():
    # 清理任务的逻辑
    print("Performing cleanup task2")

