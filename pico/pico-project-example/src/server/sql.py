import json
import os
from server.config import sql_config, devices

class SurrealRequest(object):
    def __init__(self, surreal_config) -> None:
        self.requested_data = ""
        self.req_template = f'''
            curl -k -L -s --compressed POST    --header "Accept: application/json"  \
            --header "NS: {surreal_config["name_space"]}"  \
            --header "DB: {surreal_config["data_base"]}"    \
            --user "{surreal_config["username"]}:{surreal_config["password"]}"   \
            --data "%s"     \
            {surreal_config["addr"]}    
        '''
    def cmd(self, data:str):
            command = self.req_template%data
            self.requested_data = data
            return self.__popen(command)
    
    def __popen(self, command):
        with os.popen(command,'r') as op:
            r = op.readlines()
        #jsonify
            if not r:
                return False,"NetWork Error,check for network or surreal interface."
            data = json.loads(r[0])
            return data, ''
         


class RelayCtrl(SurrealRequest):
    def __init__(self, surreal_config) -> None:
        super().__init__(surreal_config)


    def update_relay_task(self, device, channel, switch, act):
        data=f"""UPDATE relay_tasks:{device} SET
            ch = {channel},
            switch = '{switch}',
            act = {act},
            created_at = time::now();"""
        req,err = (self.cmd(data))    
        if err:
            print(err)
            return
        else:
            print(req)
            if req[0]["status"] == "OK":
                result = req[0]["result"]
                if result != []:
                    return result[0]
                return 

    def create_relay_task(self, device):
        """switch:OFF||ON"""
        data=f"""CREATE relay_tasks:{device} SET
            ch = 99,
            switch = '',
            act = 0,
            created_at = time::now();"""
        result,err = self.cmd(data)

    def del_relay_device(self, device):
        data = f"""DELETE relay_tasks:{device};"""
        result,err = self.cmd(data)

    def get_relay_task(self, device):
        data = f"""
            SELECT * FROM relay_tasks:{device};
        """

        req,err = (self.cmd(data))    
        if err:
            print(err)
            return
        else:
            print(req)
            if req[0]["status"] == "OK":
                result = req[0]["result"]
                if result != []:
                    return result[0]

    


if sql_config["name"] == "surreal":
    relay_ctrol = RelayCtrl(sql_config)  



for device in devices:
    task = relay_ctrol.get_relay_task(device)
    if not task:
        relay_ctrol.create_relay_task(device)