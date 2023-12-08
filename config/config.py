import os
import json
class JsonConfig:
    def __init__(self, config_file="config.json"):
        """ Load config file.

        Args:
            config_file: config json file.
        """
        self.config_file = '{}{}{}'.format(os.path.abspath(""),os.sep,config_file)
        configures = {}
        if config_file:
            try:
                with open(config_file) as f:
                    data = f.read()
                    configures = json.loads(data)
            except Exception as e:
                print(e)
                exit(0)
            if not configures:
                print("config json file error!")
                exit(0)


        self._update(configures)


    def _update(self, update_fields):
        """ Update config attributes.

        Args:
            update_fields: Update fields.
        """
        for k, v in update_fields.items():
            setattr(self, k, v)

