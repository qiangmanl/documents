```bash
#$HOME/.profile


export PATH=$PATH:/usr/local/go/bin
export EASY_LOGIN_PASSWD=AlloWorld1
export EASY_LOGIN_USER=AlloUser1
export ACCESS_TOKEN_USER=JI7NEmhcBgIav1R0
export ACCESS_TOKEN_PASSWD=rnQuNEZrTyIq1E0iZE6ga9ApwTY8JB4u

source .profile

#memory
docker container create --name ha-state --restart always -p 5000:8000 \
  surrealdb/surrealdb:latest start\
  -u "$EASY_LOGIN_USER" -p "$EASY_LOGIN_PASSWD"  

#
docker container create --name ha-persis --restart always -p 5001:8000 -v $HOME/backup/surrealdb/homeassistant/ha-home:/home surrealdb/surrealdb:latest start  -u  "$EASY_LOGIN_USER"  -p "$EASY_LOGIN_PASSWD"  "file:///home/data.db" 


docker start ha
docker logs ha
docker rm ha
docker stop ha

  
DATA="INFO FOR DB;"
curl --request POST \
	--header "Accept: application/json" \
	--user "$EASY_LOGIN_USER":"$EASY_LOGIN_PASSWD" \
	--data "${DATA}" \
    --header "NS: test" \
	--header "DB: test" \
	http://localhost:5001/sql


# property -------------------------------------------------

# property type
DATA="CREATE property_category:office  SET property_type ={
	'pr' : 'printer',
	'pc' : 'computer',
}"




DATA="CREATE property_category:communication SET property_type ={
	'rt' : 'router'
	'sw' : 'switch'
	'tl' : 'trunk_line'
}"

DATA="CREATE property_office_pr:0 SET 

"



DATA="CREATE property_category:viocesystem SET property_type ={

}"

DATA="CREATE property_category:vision SET property_type ={

}"
DATA="CREATE property_category:machinery SET property_type ={

}"


DATA="CREATE property_category:construct SET property_type ={
	'wd' : 'windows',
	'gr' : 'ground',
	'wl' :  'wall',
}"


DATA="CREATE property_category:kitchenware SET property_type ={
	'im' : 'icemaker'
}"

DATA="CREATE property_category:supervisory SET property_type ={

}"

DATA="CREATE property_category:furniture SET property_type ={
	'tv' : 'television',
	'dk' : 'desk',
	'bc'   : 'bed_cupboard',
	'lm'  : 'lamp',
}"





"
DATA="CREATE property_online:office_pr_1 SET 
	property = property_office_pr:1
	created_at = time::now();"
"






# ----------------------------------------------------------

#plane-----------------------------------------
DATA="CREATE plane_type:99 SET 
		en = "public"
"
DATA="CREATE plane_state_set:public SET state=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"


DATA="CREATE plane_type:98 SET 
		en = "toilet"
"

DATA="CREATE plane_state_set:toilet SET state=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"


DATA="CREATE plane_type:97 SET 
		en = "stair"
"
DATA="CREATE plane_state_set:stair SET state=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"



DATA="CREATE plane_type:96 SET 
		en = "park"
"
DATA="CREATE plane_state_set:park SET state=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"



DATA="CREATE plane_type:1 SET 
		en = "office"
"


DATA="CREATE plane_state_set:office SET state=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"


DATA="CREATE plane_type:10 SET 
		en = "rest"
"
DATA="CREATE plane_state_set:rest SET state=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"


DATA="CREATE plane_type:12 SET 
		en = "hall"
"
DATA="CREATE plane_state_set:hall SET state=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"


DATA="CREATE plane_type:13 SET 
		en = "snug"
"
DATA="CREATE plane_state_set:snug SET state=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"


DATA="CREATE plane_type:14 SET 
		en = "kitchen"
"
DATA="CREATE plane_state_set:kitchen SET state=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"


DATA="CREATE plane_type:15 SET 
		en = "gym"
"

DATA="CREATE plane_state_set:gym SET state=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"



DATA="CREATE plane_type:16 SET 
		en = "machinery"
"
DATA="CREATE plane_state_set:machinery SET data=
	{
		1: "ok",
		2: "off",
		3: "maintain"
	}
"


# plane-------------------------------------------


#db:maintain_system
DATA="plane_property:A_17f_1 set property = [

]"
DATA="CREATE plane_entity:A_17f_1 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"


DATA="CREATE plane_state:A_17f_2 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_3 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_4 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_5 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_6 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_7 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_8 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_9 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_10 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_11 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_12 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_13 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_14 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_15 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_16 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_18 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"

DATA="CREATE plane_state:A_17f_19 SET 
	state = 1
	plane_type =  10
	created_at = time::now();"



DATA="CREATE plane_state:A_17f_20 SET 
	state = 1
	plane_type =  10
	created_at = time::now();
"
DATA="CREATE plane_property:A_17f_20 SET ownedid=[


]
"






#db:maintain_system
DATA="CREATE hitch_state_set:machinery SET state=
	{
		1: "report" ,
		2: "receive" ,
		3: "ignore" ,
		4: "suspending"
	}
"

DATA="CREATE hitch_weight_set SET weight=
	{
		100 : "urgent" ,
		80 :  "important"
		60:   "standard" ,
		40:   "unimportant" ,
		20:   "noidea" ,
		0 :   "indifferent",
	}	
"

DATA = "CREATE hitch_state_set:process SET state = 
	{
		1: "reporting"
		2: "receiving"
		3: "resolved"
		4: "disputing"
		10: "rejected"
	}
" 

DATA = "CREATE resources_url SET urls = [url1,url2,url3,...]"


#db:maintain_system
# get  resources_url_id to resources_url table first
DATA="CREATE log_A_17f_20:1 SET 
	report = "a",
	process=  1 ,
	property = ""
	resources_url_id = ""
	report_at = time::now()
	"

DATA="INSERT INTO log_A_17f_20:1 {
    receive ="b",
	process = 2,
	receive_at = time::now()
}"


#normal resolve
DATA="INSERT INTO log_A_17f_20:1 {
    resolve ="c",
	process = 3,
	resolve_at = time::now()
}"

# or disputing resolve

DATA="INSERT INTO log_A_17f_20:1 {
	process = 4
}"

#then
DATA="CREATE rejected_logs: A_17f_20_1 {
    first_reject = "x",
	reject_reason = "",
	first_reject_at = time::now()
}"
#first reject done


DATA="INSERT INTO rejected_logs: A_17f_20_1 
	second_reject = "y",
	second_reject_at = time::now()
"
#then
DATA="INSERT INTO log_A_17f_20:1 {
    resolve ="c",
	process = 10,
	resolve_at = time::now()
}"



	# receive ="",
	# solution = "",
	# report_text = "",
	# report_voice = "",
	# report_pictrue = "",
	# report_film = "",

	# reject_reason = "",
	# first_rejection = false
	# second_rejection = false
	# created_at = time::now();
	# reject_at ="",	
	# receive_at = "";


# {"created_at":"2023-03-19T05:16:11.284011115Z","id":"account:blzoq8tdb7hbbrl4kpq7","name":"ACME Inc"}
 


```
