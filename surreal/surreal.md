
```python
import os

def curl_req(data):
    req = f"""
    curl -k -L -s --compressed POST    --header "Accept: application/json"  \
            --header "NS: test"     --header "DB: test"     --user "cc:cc"   \
            --data "{data}"     \
            http://localhost:12345/sql     
    """
    os.system(req)
    
data = ""
data = "SELECT * FROM tasks;"
curl_req(data)

```
```python
import os
import json
import nanoid
#
# need_user_env = "EASY_LOGIN_USER"
# need_password_env = "EASY_LOGIN_PASSWD"
# door = "A"
nano_word = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# name = "ihotel"
# ns = name
# db = f'ihotel-{door}'
# url = "http://localhost:5001/sql"
id_size = 6

class DataRequest(object):
    def __init__(self,**kwargs):
        self.kwargs = kwargs




class SurrealRequest(DataRequest):
    
    def __init__(self, request, name, door ,**kwargs):
        self.door = door
        self.current_data = '' 
        self.name = name
        self.url = request
        self.user = kwargs.get("user",os.getenv("EASY_LOGIN_USER"))
        self.password = kwargs.get("password",os.getenv("EASY_LOGIN_PASSWD"))
        self.db = kwargs.get("db",f'{name}-{door}')
        self.ns = kwargs.get('ns',{name})
        super(SurrealRequest,self).__init__(**kwargs)

    def __toge_comm(self, data: str) -> str:
        command =  f"""
        curl --request POST \
        --header "Accept: application/json" \
        --user "{self.user}":"{self.password}" \
        --data "{data}" \
        --header "NS: {self.ns}" \
        --header "DB: {self.db}" \
           {self.url}
        """
        return command

    def _req_comm(self, command: str ):
        command = self.__toge_comm(command)
        data,err = self.__popen_comm(command)
        if err:
            return None ,err
        return data, ''
    def __popen_comm(self, command: str) -> dict:
        with os.popen(command,'r') as op:
            r = op.readlines()
        #jsonify
        if not r:
            return False,"NetWork Error,check for communication and interface."
        data = json.loads(r[0])
        return data, ''
    
    # def shit(self, req):
    #     print(req) 
    def __probe_creating_table(self, req):
        print(req)
        err = req[1]
        if err:
            return '', err
        else:
            data = req[0]
            if isinstance(data,list):
                data = data[0]
                if data["status"].upper() == "OK":
                    return data['result'][0],''
                elif data["status"].upper() == 'ERR':
                    return '',data.get('detail','no detail for explain status err.need manually debug for more')
            elif isinstance(data,dict):
                return '',data.get('information','no infomation probed. need manually debug for more detail') 
    #     # req为元组，第一个元素为data，第二个为err str 
    #     # req = req[0][0]
    #     if isinstance(req, dict):
    #         if req.get("code",0) == 400:
    #             return '',req.get('information','no infomation probed. need manually debug for more detail') 
    #     elif isinstance(req, list):
    #         req = req[0]
    #         if req["status"].upper() == "ok":
    #             return req['result'][0],''
    #         elif req["status"].upper() == 'err':
    #             return '',req.get('detail','no detail for explain status err.need manually debug for more')
            
    def get_db_info(self):
        DATA="INFO FOR DB;"
        return self._req_comm(DATA)[0]

    def remove_table_instant(self,table):
        DATA=f"REMOVE TABLE {table}"
        self._req_comm(DATA)
        return self.get_db_info()
    
    def delete_data(self, index):
        DATA = f'DELETE {index}' 
        return self._req_comm(DATA)

    def get_table_info(self, table):
        DATA= f"SELECT * FROM {table}"
        return self._req_comm(DATA)

    def create_hitch_state(self, states, state_type):
        require = ["id","created_at"]
        self.current_data = f"""CREATE hitch_state_set:{state_type} SET 
            created_at = time::now(),
            {states}
        """
        req = self._req_comm(self.current_data)
        # 静态表直接查表来确认

        data, err = self.__probe_creating_table(req)
        if err:
            return "", err
        elif all(elem in data.keys() for elem in require):
            return data, err 
        return '',f'hitch state incomplete created in hitch_state_set. \
            data:{data.__str__()}' 
    
    def create_plane_state(self, plane, states):
        require = ["created","id","dead","created_at"]
        self.current_data=f"""CREATE plane_state_set:{plane} SET 
            created_at = time::now(),
            {states}
        """
        req = self._req_comm(self.current_data)
        data, err = self.__probe_creating_table(req)
        if err:
            return "", err
        if all(elem in data.keys() for elem in require):
            return data, err 
        return '',f'plane state  incomplete created in plane_state_set. \
            data:{data.__str__()}' 
    
    def simplify_entity_type(self, entity_type):
        return entity_type

    def simplify_structure_type(self, structure_type):
        return structure_type

    def create_entity(self, entity):
        alias = entity.get("alias", nanoid.generate(nano_word, id_size))
        require = ["state", "alias","belong", "entity_type","structure_type","info"]
        entity_type = self.simplify_entity_type(entity["entity_type"])
        structure_type = self.simplify_structure_type(entity["structure_type"])
        index = f"{structure_type}_{entity_type}_{alias}"
        info = entity["info"]
        self.current_data = f"""CREATE entity_table:{index} SET 
            state = 'created',
            alias = '{alias}',
            belong = 'virtual_storage',
            entity_type = '{entity_type}',
            structure_type = '{structure_type}',
            created_at = time::now(),
            info = {info}
        """

        req = self._req_comm(self.current_data)
        data, err = self.__probe_creating_table(req)
        if err:
            return "", err
        if all(elem in data.keys() for elem in require):
            return data, err 
        return '',f'entity  incomplete created in entity_table. \
            data:{data.__str__()}'
    

        
    def create_source(self, entity_id, source_info):
        #state:living, dead, created
        require = ["created_at", "source_info", "state"]
        self.current_data = f"""CREATE virtual_storage:{entity_id} SET 
        created_at = time::now(),
        source_info = {source_info},
        state = 'created'
        """
        req = self._req_comm(self.current_data)
        data, err = self.__probe_creating_table(req)
        if err:
            return "", err
        if all(elem in data.keys() for elem in require):
            return data, err 
        return '',f'source  incomplete created in source_info. \
            data:{data.__str__()}'
    
    def create_area(self,area):
        require = ["created_at","id"]
        self.current_data = f""" CREATE area_table:{area} SET 
            created_at = time::now()
        """
        req = self._req_comm(self.current_data)
        data, err = self.__probe_creating_table(req)
        if err:
            return "", err
        if all(elem in data.keys() for elem in require):
            return data, err 
        return '',f'area  incomplete created in area_table. \
            data:{data.__str__()}'
        

    def create_plane(self, area, plane_type, picture_url, alias=''):
        require = ["id", "state", "plane_type", "area", "owned_entities", "picture_url"]
        # or query from plane_state_set[plane_type]
        if not alias:
            alias = nanoid.generate(nano_word, size=5)
        index = f'{self.door}_{area}_{alias}'
        self.current_data = f"""CREATE plane_table:{index} SET 
            state = 'suspend',
            plane_type = '{plane_type}',
            area = '{area}',
            picture_url = '{picture_url}',
            owned_entities = [],
            created_at = time::now()
        """
        req = self._req_comm(self.current_data)
        data, err = self.__probe_creating_table(req)
        if err:
            return "", err
        if all(elem in data.keys() for elem in require):
            return data, err 
        return '',f'plane  incomplete created in plane_table. \
            data:{data.__str__()}'

    def create_relation_table(self, entity_id, plane_id):
        # request: f"SELECT * FROM entity_plane_relation WHERE eid == {entity_id} and pid == {plane_id}"
        require = ["entity_id","plane_id"]
        self.current_data = f"""CREATE entity_plane_relation:{nanoid.generate(nano_word, size=16)} SET 
            entity_id =  '{entity_id}',
            plane_id = '{plane_id}',
            created_at = time::now()
        """
        req = self._req_comm(self.current_data)
        data, err = self.__probe_creating_table(req)
        if err:
            return "", err
        if all(elem in data.keys() for elem in require):
            return data, err 
        return '',f'relation  incomplete created in entity_plane_relation. \
            data:{data.__str__()}'

    def create_maintain_log(self, resource_url, entity_id, plane_id, reporter):
        require = ["process_state","plane_id","entity_id","reporter","resource_url","rp_created_at"]
        self.current_data = f"""CREATE maintain_log:{nanoid.generate(nano_word, size=16)} SET 
            process_state = 'reporting',
            plane_id = '{plane_id}',
            entity_id = '{entity_id}',
            reporter = '{reporter}',
            resource_url = {resource_url},
            rp_created_at = time::now()
        """
        req =  self._req_comm(self.current_data)
        data, err = self.__probe_creating_table(req)
        if err:
            return "", err
        if all(elem in data.keys() for elem in require):
            return data, err 
        return '',f'maintain log  incomplete created in maintain_log. \
            data:{data.__str__()}'

```
