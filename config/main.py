from config import JsonConfig
config1 = JsonConfig("config.json")
config2 = JsonConfig("./conf/config.json")
print(dir(config1))
print(dir(config2))