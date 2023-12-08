from server.config import server_config
from server.utils import gene_rand_id
from sanic import Sanic




class Server:
    """
    """
    def __init__(self,server_config:dict=server_config)->None:
        appname = server_config.get("appname",gene_rand_id(10))
        self.__app__ = Sanic(appname)

    @property
    def add_http_route(self)->None:
        return self.__app__.add_route

    def run(self, **kwargs)->None:
        self.__app__.run(**kwargs)

server = Server()