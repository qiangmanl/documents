
curl --request POST  --header "Accept: application/json"     --user "$EASY_LOGIN_USER":"$EASY_LOGIN_PASSWD"  --data "${DATA}"     --header "NS: test"        --header "DB: test"     http://localhost:5001/sql



#删除测试表格
DATA="REMOVE TABLE office_set"
#查询表格
DATA="INFO FOR DB;"



#建筑体的状态集合
#ignore不监视状态 suspend 未准备好的，刚上线的，
DATA="CREATE construct_structure__state:windows SET 
 ignore = 10,
 suspend = 0,
 healthy = 1,
 repair = 2,
 dead = 99,
"

DATA="CREATE construct_structure__state:ground SET 
 ignore = 10,
 suspend = 0,
 healthy = 1,
 repair = 2,
 dead = 99,
"

#建筑体的状态集合结束






#创建窗户实体 
DATA="CREATE entity_construct:0 SET info={ 
  name : '1720',
  text : '50*20',
  }
  entity_state = 1,
  type='ground',
  maintain = [maintain_logs:0],
"


DATA="CREATE hitch_state_set:process SET 
		reporting = 1,
		receiving = 2,
		resolved = 3,
		disputing = 4,
		rejected = 10,
	}
"

DATA="CREATE hitch_state_set:weight SET 

	urgent = 100,
	important = 80,
	standard = 60,
	unimportant = 40,
	noidea = 20,
	indifferent = 0,


		
"
#result为1是正常处理 result 为0驳回处理，需要添加新的表保存日志,当result 为0时，resolver等于maintain_rejected_log 的appeaser
"CREATE maintain_logs:0 SET 
	process_state = 1
	plane = plane_state:A_17f_1,
	entity= entity_construct:0,
	reporter='',
	report_at = time::now();
	receiver='',
	receiver_at = time::now();
	resolver = ''
	result = 1
	resolver_at = time::now();
	resource_urls = [],
"

#添加新的表保存日志，索引查询的ID与maintain_logs 一致，
"CREATE maintain_rejected_log:0 SET 
	entity= entity_construct:0,
	plane = plane_state:A_17f_1,
	reason = ''
	rejecter = '' 
	appeaser = ''
	success = true

"


#创建区域模块：公共区域的对象 
DATA="CREATE plane_state_set:public SET 
    data= {	
	1 : 'healthy',
	2 : 'repair',
	0 : 'suspend',
	20: 'dirty',
    }"
    
    
#创建区域模块：客房区域的对象 和状态
DATA="CREATE plane_state_set:rest SET 
    state= {	
	1: 'healthy',
	2: 'repair',
	0: 'suspend',
	20: 'dirty',
	11:'booking',
	12:'lodging',
    }"

    

#创建区域模块实体：客房模块 1701,owned_entity 存的是online的索引，通过这个索引获取  实体索引的位置
DATA="CREATE plane_state:A_17f_1 SET 
	state = 1,
	plane_type = 'rest',
	owned_entity = [0],
	created_at = time::now();
"


DATA="CREATE entity_online:0 SET 
	entity_id = entity_construct:0,
	belong = 'A_17f_1'
	created_at = time::now();"
"

#push
