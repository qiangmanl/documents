import os
import json
# from test_data import areas


project_directory = ".HAllow"
current_path = os.path.abspath(os.path.curdir)
home_path = os.getenv("HOME")

def get_project_info():
    with open (f'{current_path}/data/project.json','r') as f:
        project_info = json.load(f)
    return project_info

project_info = get_project_info()
project_name = project_info["name"]
init = project_info["init"]
port = project_info["port"]
door = project_info["door"]

config_path = f'{home_path}/{project_directory}/{project_name}'
storage_path  = f'{config_path}/.storage'

door_path = f'{config_path}/{door}'
planes_json_file = "planes_data.json"

def get_planes():
    with open (f'{current_path}/data/{planes_json_file}','r') as f:
        planes = json.load(f)
    return planes

def create_background_path(area):
    background_path = f'{config_path}/www/background'
    os.system(f'mkdir -p {background_path}/{door}_{area}')

def create_area_lovelace():
    data = {
    "version": 1,
    "minor_version": 1,
    "key": "lovelace_dashboards",
    "data": {
        "items": [
        ]
    }
    }
    with open (f'{storage_path}/lovelace_dashboards','w') as f:
        json.dump(data, f, indent=2)


def apppend_area_lovelace(area_name):
    data = {
        "show_in_sidebar": True,
        "icon": "mdi:office-building-outline",
        "title": f'{area_name}',
        "require_admin": True,
        "mode": "storage",
        "url_path": f'lovelace-{area_name}',
        "id": f'{area_name}'
    }

    with open (f'{storage_path}/lovelace_dashboards','r+') as f:
        dashboard = json.load(f)
        dashboard['data']['items'].append(data)
        f.seek(0)
        json.dump(dashboard, f, indent=2)
        f.truncate() 

def create_plane_lovelace(area):
    name = f'{door}_{area}'
    data = {
        "version": 1,
        "minor_version": 1,
        "key": f'lovelace.{name}',
        "data": {
            "config": {
            "views": [
            ]
            }
        }
    }
    with open (f'{storage_path}/lovelace.{door}_{area}','w') as f:
        json.dump(data, f, indent=2)
	
def comp_plane_view(area, alias):
    view_data = {
        "theme": "Backend-selected",
        "title": f'{alias}',
        "path": f'{door}_{area}_{alias}',
        "badges": [],
        "cards": [
            {
                "type": "picture-elements",
                "elements": [
                    {
                        "type": "state-badge",
                        "entity": "",
                        "style": {
                            "top": "50%",
                            "left": "40%"
                        }
                    }
            ],
            "image": f'local/background/{door}_{area}/{alias}.png'
            }
        ]    
    },
    return view_data[0]

def create_plane_view(area, plane):
    view_data = comp_plane_view(area, plane)
    with open (f'{storage_path}/lovelace.{door}_{area}','r+') as f:
        area_ui = json.load(f)
        area_ui["data"]["config"]["views"].append(view_data)
        f.seek(0)
        json.dump(area_ui, f, indent=2)
        f.truncate() 


def create_runtime_command():
    command = f"""nerdctl create --name {project_name} \
    --restart always \
    --net bridge \
    --privileged \
    --env TZ=Asia/Shanghai \
    -p {port}:8123 \
    --mount type=bind,src="$HOME"/.HAllow/{project_name},dst=/config \
    ghcr.io/home-assistant/home-assistant:stable """

    return command
if init:

    os.system(f"mkdir -p {home_path}/.HAllow/{project_name}")
    runtime_command = create_runtime_command()
    if not os.path.exists(storage_path):
        if os.path.exists(f'{home_path}/.HAllow/{project_name}'):
            os.system(runtime_command)
            input('check the created container, type enter if container is running>>>')
        else:
            'main container no work'
            exit(0)
    
  
    # os.system(f'nerdctl start {project_name}')
    create_area_lovelace()
    planes = get_planes()
    for data in planes:
        area = data['area']
        apppend_area_lovelace(f'{door}_{area}')
        create_plane_lovelace(area)
        create_background_path(area)
        for plane in data['planes']:
            alias =  plane['alias']
            name = f'{area}_{alias}'
            create_plane_view(area, alias)

    os.system(f'nerdctl restart {project_name}')
# if not os.path.exists(storage_path):
#     print(f"project need to be initialized, please login on localhost:{port} and setup it to dashboard.")
#     exit(0)


























