import os
import json
import yaml
from datura.const import YAML_CONFIG_NAME, JSON_CONFIG_NAME, YML_CONFIG_NAME
from datura.baseobjects import DictBase
from datura.exception import ConfigInitError
from .tools import gen_random_id


class Config(DictBase):

    def __init__(self,base_mode=False) -> None:
        """ Load config file.

        Args:
            config_file: config json file.
        """
        self._permanent_configures = None
        # 优先使用yaml格式
        if os.path.exists(f'{os.path.abspath("")}{os.sep}{YAML_CONFIG_NAME}'):
            self._config_file_path = f'{os.path.abspath("")}{os.sep}{YAML_CONFIG_NAME}'

        elif os.path.exists(f'{os.path.abspath("")}{os.sep}{YML_CONFIG_NAME}'):
            self._config_file_path = f'{os.path.abspath("")}{os.sep}{YML_CONFIG_NAME}'

        elif os.path.exists(f'{os.path.abspath("")}{os.sep}{JSON_CONFIG_NAME}'):
            self._config_file_path = f'{os.path.abspath("")}{os.sep}{JSON_CONFIG_NAME}'
        else:
            if base_mode == False:
                raise ConfigInitError(f'{__name__}: config file not exist')
            else:
                self._permanent_configures = config_seed
                self._config_file_path = f'{os.path.abspath("")}{os.sep}{YAML_CONFIG_NAME}'
                self._config_type = self._config_file_path.split('.')[-1]
                self._update_file_config(self._permanent_configures)
                return
        try:
            with open(self._config_file_path) as f:
                data = f.read()
                #如果为空  data 为空str
                self._config_type = self._config_file_path.split('.')[-1]
                if data == '':
                    raise ConfigInitError(f'{__name__}:load {self._config_file_path} but empty data')
                match self._config_type:
                    case "yaml"|"yml":
                        self._permanent_configures = yaml.safe_load(data)
                    case "json":
                        self._permanent_configures = json.loads(data)
                if isinstance(self._permanent_configures, dict) == False:
                     raise ConfigInitError(f'{__name__}:load config with other error')
                else:
                    self._update_file_config(self._permanent_configures)
        except Exception as e:
            print(e)
            exit() 

    def _update_file_config(self, update_fields) -> None:
        """ Update config attributes.

        Args:
            update_fields: Update fields.
        """
        for k, v in update_fields.items():
            self.__setattr__(k, v)

    def update_item(self, temporary=False , **kwargs) -> None:
        """
        Usage:
            config.update(x=11)
        """
        for k,v in kwargs.items():
            self.__setattr__(k , v)
            if temporary == False:
                self._permanent_configures[k] = v
                self.dump_config(inplace=True)

    def remove_item(self,item,temporary=True) -> None:
        if item in self._permanent_configures:
            del self._permanent_configures[item]
            if temporary == False:
                self.dump_config(inplace=True)

    def dump_config(self,inplace:bool=False) -> None:
        if inplace:
            config_file = self._config_file_path
        else:
            config_file = f'{self._config_file_path}.new'
        with open(config_file, 'w') as j_f:
            match self._config_type:
                case "yaml" | "yml":
                    yaml.dump(self._permanent_configures, j_f, default_flow_style=False)
                case "json":
                    json.dump(self._permanent_configures, j_f, indent=4)
     

config_seed = {
    "project" : "unknown",
    "kind" : "backtest",
    "node_id" : f'{gen_random_id()}',
    "node_group" : 'default'
}