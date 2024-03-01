from config import JsonConfig
config1 = JsonConfig("config.json")
config2 = JsonConfig("./conf/config.json")
print(dir(config1))
print(dir(config2))



class DictBase(dict):
    """dict like object that exposes keys as attributes"""

    __slots__ = ()
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    __setstate__ = dict.update


    def __getstate__(self):
        return self

    def update(self, *args, **kwargs):
        """update and return self -- the missing dict feature in python"""

        super().update(*args, **kwargs)
        return self

    def copy(self):
        return DictBase(self)


class DictClass(DictBase):
    def __init__(self,**kwargs):
        self.update(**kwargs)

import os
import json
class Config(DictClass):
    def __init__(self, config_file="config.json"):
        """ Load config file.

        Args:
            config_file: config json file.
        """
        self.config_file = '{}{}{}'.format(os.path.abspath(""),os.sep,config_file)
        self.configures = {}
        if config_file:
            try:
                with open(config_file) as f:
                    data = f.read()
                    #如果为空  data 为空str
                    if data:
                        self.configures = json.loads(data)
            except Exception as e:
                print(e)
                exit(0)
            if not self.configures:
                print("config json file error!")
                exit(0)


        self._update(self.configures)


    def _update(self, update_fields):
        """ Update config attributes.

        Args:
            update_fields: Update fields.
        """
        for k, v in update_fields.items():
            setattr(self, k, v)


    def dump(self,**kwargs:dict):
        for k,v in kwargs.items():
            self.configures[k] = v 

        with open(self.config_file, 'w') as j_f:
            json.dump(self.configures, j_f, indent=4)

# class Order:
#     def __init__(
#         self,
#         balance,
#         commission,
#     )->None:
#         self.balance = balance
#         self.commission = commission
#         self.order = DictClass(blance=blance, comission=commission)


#     def sell(self,)
