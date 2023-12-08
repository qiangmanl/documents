from surreal import SurrealRequest
from test_data import plane_states, entity_data ,plane_data,hitch_states ,areas
import nanoid
url = "http://localhost:5001/sql"
door = "A"
name = "ihotel"





entity = entity_data[0]
nano_word = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

sr = SurrealRequest( request=url, name=name, door=door)

class IhotelModel(object):
    def __init__(self, url, door, name, destroy=False):
        self.request = SurrealRequest( request=url, name=name, door=door)
        if destroy:
            self.destroy()

    def destroy(self):
            self.request.remove_table_instant("entity_table")
            self.request.remove_table_instant("virtual_storage")
            self.request.remove_table_instant("hitch_state_set")
            self.request.remove_table_instant("plane_state_set")
            self.request.remove_table_instant("plane_table")
            self.request.remove_table_instant("area_table")  
            print(self.request.get_db_info())

    def init_table(self):
        self.set_area()
        self.set_hitch_states()
        self.set_plane_states()
        self.set_plane()
        self.set_entity(entity)


    def set_area(self):
        require = ["created_at","id"]
        for area in areas:
            result,err = self.request.create_area(area=area)
            if result:
                all(elem in result.keys() for elem in require)
        return result

    def set_hitch_states(self):
        for hitch in hitch_states:
            result = self.request.create_hitch_state(state_type=hitch["type"], states=hitch["states"])
        return result
    
    def set_plane_states(self):
        """
            probe = 1
            success result:
            [{'time': '69.888µs',
            'status': 'OK',
            'result': [{'dirty': 20,
            'healthy': 1,
            'id': 'plane_state_set:public',
            'repairing': 3,
            'suspend': 0,
            'unhealthy': 2}]}]

        """
        for  plane in plane_states:
            result = self.request.create_plane_state(plane=plane["type"], states=plane["states"])
        return result


    def set_plane(self):
        for plane  in plane_data:
            result = self.request.create_plane(area = plane["area"], alias=plane["alias"], picture_url=plane["picture_url"],\
                                             plane_type=plane["type"])
        return result

    def set_entity(self, entity):
        #  entity = entity_data[0]
        data,err = ( self.request.create_entity(
            entity=entity
            ) 
        )
        # 如果已有 entity 或者其他错误不执行
        if not data:
            return "",err
        else:
            _id = data["id"]
            entity_id = _id.split(":")[1]
            source,err = self.request.create_source(entity_id=entity_id, source_info=entity["source_info"])
            if err:
                # 虽然创建entity成功，但是resource没有创建成功，所以删除entity
                self.request.delete_data(_id)
                return "",err     
            else:
                return source["id"],""



if __name__ == "__main__":
    i  = IhotelModel(url,door,name,destroy=1)
    i.init_table()
    print(i.set_entity(entity))
    # i.set_entity(entity,2,1)