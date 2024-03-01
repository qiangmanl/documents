from datura.utils.config import Config
from datura.logger import Logger
from datura.exception import ConfigInitError
from  threading import local

try:
    config = Config()
except ConfigInitError as e:
    logger = Logger()
    logger.warning(e.__repr__())
    logger.debug("config using base mode.")
    config = Config(base_mode=True)
    config.dump_config(inplace=False)

local = local()
local.project_name = config.project 
local.kind = config.kind
local.node_id = config.node_id
local.node_group = config.node_group