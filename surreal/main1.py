import os
import json
from cc import CircleChain

def curl_popen( data: str) -> dict:
    req = f"""
    curl -k -L -s --compressed POST    --header "Accept: application/json"  \
            --header "NS: test"     --header "DB: test"     --user "cc:cc"   \
            --data "{data}"     \
            http://localhost:12345/sql     
    """
    with os.popen(req,'r') as op:
        r = op.readlines()
    #jsonify
    if not r:
        return False,"NetWork Error,check for communication and interface."
    data = json.loads(r[0])
    return data, ''

class DataRequest(CircleChain):
    def __init__(self, chain,participate=True) -> None:
        super().__init__(chain)
  
        if participate == False:
            task = test_chain[0]
            data = f"""Create tasks:0 SET
                task = '{task}'
            """    
            curl_popen(data)
    def _save_ack_task(self, task):
            
        data = f"""UPDATE tasks:0 SET
            task = '{task}'
        """    
        curl_popen(data)
        print(f'save a task:{task}')
    def _get_ack_task(self): 
        data = "SELECT task FROM tasks;"
        task = curl_popen(data)
        if task[0][0]["result"] == []:
            return None
        task = task[0][0]["result"][0]["task"]
        print(f'get :{task}')
        return task
    

test_chain = [str(i) for i in range(1000)]
dr = DataRequest(test_chain,participate=True)
dr.rolling()