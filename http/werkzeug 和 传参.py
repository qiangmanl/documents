from werkzeug.wrappers import Request, Response
from werkzeug.local import LocalStack


context_stack = LocalStack()

def simple_app(environ, start_response):
    request = Request(environ)
    response = Response("Hello, Werkzeug!", content_type="text/plain")

    current_request = context_stack.top
    import pdb
    pdb.set_trace()
    response.headers["X-Request-Method"] = current_request.method
    return response(environ, start_response)
from werkzeug.serving import run_simple
run_simple('localhost', 4000, simple_app)

#url
# http://localhost:4000

#---------------------------------------------------------------
#query string
from werkzeug.wrappers import Request, Response
from werkzeug.local import LocalStack

context_stack = LocalStack()

def simple_app(environ, start_response):
    request = Request(environ)
    query_string = request.args.get('param_name')
    context_stack.push(request)
    response = Response(f"Hello, {query_string}!", content_type="text/plain")
    current_request = context_stack.top
    response.headers["X-Request-Method"] = current_request.method
    response.headers["X-Query-String-Param"] = query_string
    return response(environ, start_response)

from werkzeug.serving import run_simple
run_simple('localhost', 4000, simple_app)


#url get
# http://localhost:4000


# @--------------------------------------------------------------
#header
from werkzeug.wrappers import Request, Response
from werkzeug.local import LocalStack

context_stack = LocalStack()

def simple_app(environ, start_response):
    request = Request(environ)
    custom_header = request.headers.get('X-Custom-Header')
    context_stack.push(request)  
    response = Response(f"Hello, {custom_header}!", content_type="text/plain")
    current_request = context_stack.top
    response.headers["X-Request-Method"] = current_request.method
    response.headers["X-Custom-Header-Value"] = f'{custom_header} to response'
    return response(environ, start_response)

from werkzeug.serving import run_simple
run_simple('localhost', 4000, simple_app)

#requests
import requests
headers = {'X-Custom-Header': 'custom header info'}
response = requests.get('http://localhost:4000', headers=headers)
print(response.text)
print(response.headers)
#
#script
    # <script>
    #     document.getElementById("sendRequest").addEventListener("click", function () {
    #         var xhr = new XMLHttpRequest();
    #         xhr.open("GET", "http://localhost:4000", true);

    #         // 设置自定义HTTP请求头
    #         xhr.setRequestHeader("X-Custom-Header", "MyCustomHeaderValue");

    #         xhr.onreadystatechange = function () {
    #             if (xhr.readyState === 4 && xhr.status === 200) {
    #                 console.log(xhr.responseText);
    #             }
    #         };

    #         xhr.send();
    #     });
    # </script>

# ---------------------------------------------------------------------------


from werkzeug.wrappers import Request, Response
from werkzeug.local import LocalStack
from werkzeug.utils import redirect

context_stack = LocalStack()
def simple_app(environ, start_response):
    request = Request(environ)
    context_stack.push(request)

    if request.method == 'POST':
        data = request.get_data(as_text=True)  
        response = Response(f"Received POST data: {data}", content_type="text/plain")
    else:
        response = Response(f"no data", content_type="text/plain")
    
    current_request = context_stack.top
    response.headers["X-Request-Method"] = current_request.method
    return response(environ, start_response)

from werkzeug.serving import run_simple
run_simple('localhost', 4000, simple_app)



# $curl -X POST -d "This is the request body" http://localhost:4000
#return
# Received POST data: This is the request body

#---------------------------------------------------------------------------------------------
# LocalStore

from werkzeug.wrappers import Request, Response
from werkzeug.local import LocalStack

context_stack = LocalStack()

def simple_app(environ, start_response):
    request = Request(environ)
    context_stack.push(request)
    local_storage_param = request.args.get('localStorageParam')
    response = Response(f"Hello, {local_storage_param}!", content_type="text/plain")
    current_request = context_stack.top
    response.headers["X-Request-Method"] = current_request.method
    response.headers["X-LocalStorage-Param"] = local_storage_param

    return response(environ, start_response)

from werkzeug.serving import run_simple
run_simple('localhost', 4000, simple_app)



# <!DOCTYPE html>
# <html>
# <head>
#     <title>Local Storage Example</title>
# </head>
# <body>
#     <button id="setLocalStorage">Set Local Storage</button>
#     <button id="getRequest">get Request</button>
#     <button id="setRequest">Send Request</button>
#     <script>
#         // 设置LocalStorage的值
#         document.getElementById("setLocalStorage").addEventListener("click", function () {
#             localStorage.setItem('localStorageParam', 'Alice');
#         });
        
#         // 发送GET请求，传递LocalStorage的值作为查询参数
#         document.getElementById("getRequest").addEventListener("click", function () {
#             var localStorageParam = localStorage.getItem('localStorageParam');
#             console.log(localStorageParam)
#         });
#         // as a args like query string  put in request to server

#     </script>
# </body>
# </html>



#----------------------------------------------------------------------------------------------
# route
from werkzeug.wrappers import Request, Response
from werkzeug.local import LocalStack
from werkzeug.routing import Map, Rule


context_stack = LocalStack()

# 创建路由规则，将名字作为路径参数
url_map = Map([
    Rule('/hello/<name>', endpoint='hello'),
])

def simple_app(environ, start_response):
    request = Request(environ)
    context_stack.push(request)
    adapter = url_map.bind_to_environ(environ)

    try:
        endpoint, values = adapter.match()
        if endpoint == 'hello':
            name = values.get('name')
            response = Response(f"Hello, {name}!", content_type="text/plain")
        else:
            response = Response("Not Found", status=404)
    except Exception as e:
        response = Response("Error: " + str(e), status=500)

    # 从上下文中获取请求对象
    current_request = context_stack.top
    response.headers["X-Request-Method"] = current_request.method

    return response(environ, start_response)

from werkzeug.serving import run_simple
run_simple('localhost', 4000, simple_app)


#url get
# http://localhost:4000/hello/John

# -----------------------------------------------------------------------------------
# cookies  or session
from werkzeug.wrappers import Request, Response
from werkzeug.local import LocalStack
from werkzeug.routing import Map, Rule

context_stack = LocalStack()

url_map = Map([
    Rule('/set_name/<name>', endpoint='set_name'),
    Rule('/get_name',endpoint='get_name')
])

def simple_app(environ, start_response):
    request = Request(environ)
    context_stack.push(request)
    adapter = url_map.bind_to_environ(environ)
    
    try:
        endpoint, values = adapter.match()
        if endpoint == 'set_name':
            name = values.get('name')

            response = Response(f"set name: {name}!", content_type="text/plain")
            response.set_cookie("username",name)
        elif endpoint == 'get_name':
            username = request.cookies.get('username')
            if username:
                response = Response(f"Hello, {username}!", content_type="text/plain")
            else:
                response = Response(f"not set name!", content_type="text/plain")
        else:
            response = Response("Not Found", status=404)
    except Exception as e:
        response = Response("Error: " + str(e), status=500)

    current_request = context_stack.top
    response.headers["X-Request-Method"] = current_request.method

    return response(environ, start_response)

from werkzeug.serving import run_simple
run_simple('localhost', 4000, simple_app)


#url get
# http://localhost:4000/get_name
# http://localhost:4000/set_name/John
## http://localhost:4000/get_name


#-------------------------------------------------------------------------------
