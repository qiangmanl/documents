#### 建镜像时， 把zh.csv 复制到 ~/frappe-bench/apps/erpnext/erpnext/translations 	即可

#### docker ps -aq|xargs -r docker rm 
#### 定向删除  docker volume ls -q  |grep my |xargs -r docker volume rm
#### docker volume prune 
#### home : http://127.0.0.1:8080/app/home 
#### 默认用户 Administrator 需要修改为可用邮箱  密码为数据库密码，需要修改为使用密码，采用邮箱登录
#### api在用户设置中生成   key和api_secret 781359e3eace199:72cfd1aba536bed
```bash
import requests
url = "http://127.0.0.1:8080/api/method/frappe.auth.get_logged_user"

headers = {
    'Authorization': f'token 0f018e24c1c33aa:55b3c688a66287b',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
response



url = "http://127.0.0.1:8080/api/resource/Assets?fileds=["item_code","name"]"
headers = {
    'Authorization': f'token 0f018e24c1c33aa:55b3c688a66287b',
    'Content-Type': 'application/json'
}
params = {
    "fields": json.dumps(["asset_name", "item_code","location"])
}
response = requests.get(url, headers=headers, params=params)
if response.ok:
    print(response.json())

```
##### 在用户设置 生成api d3b8fcc6a83219f 


##### 位置 

```
    父类是组, 父类继承一般不超过3级
    继承名称例如:
    format:{location_name} {parent_location}
```
##### 物料号 选固定资产 名称不改默认和ID 一样

```
新建一个易于识别用途物料组名称(数字资产成品)  所属所有组 
物料号采用集成系统类型 + 分割符号(例如下划线) + 设备类型
物料号建议统一长度
物料名称与物料号一致
勾选 允许资产 选择资产类别  一个物料组包含所有集成系统多个资产类别 一个资产类别包含多个 物料号

```
##### 资产
资产编号 自定义  建议包含日期 自动编号 例如  format:{asset_name}-{YYYY}{####}
资产通过建立一个或多个标签 快速查询 
资产添加附件
打印资产列表先切换到报表视图


##### sql 
```sql
mysql -u root -p 
-- 找到数据库
SHOW DATABASES;
USE $DATABASE;
SHOW TABLES;
select * from $TABLE;
-- 增加一个对资产只读权限的用户

CREATE USER 'rdouser'@'%' IDENTIFIED BY 'rdopswd';
SHOW GRANTS FOR 'rdouser'@'%';

-- 
GRANT SELECT ON `_5e5899d8398b5f7b`.`tabAsset` TO 'rdouser'@'%';
GRANT SELECT ON `_5e5899d8398b5f7b`.`tabItem` TO 'rdouser'@'%';

REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'rdouser'@'%';

-- show tables; 只显示一个资产表名
mysql -u rdouser -p
use $DATABASE;
show tables;
INSERT INTO tabAsset () VALUES();
-- INSERT command denied to user 拒绝写入

SHOW COLUMNS FROM tabAsset;

select name, asset_name, location, item_code, item_name  from tabAsset where asset_name = "CMM_SWL2";
quit;

select name, item_group  from tabItem;

```

#### 脚本
##### 触发案例
```
https://blog.csdn.net/weixin_46665865/article/details/132633857

```
#####  过滤限定表单字段
```js
// foo:doctype  aa:列名
frappe.ui.form.on('foo', {
    refresh: function(frm) {
        frm.set_query('aa', function() {
            return {
                filters: {
                    'item_group': 'aa'
                }
            };
        });
    }
});

```


##### 提示删重
```js
frappe.ui.form.on('foo', {
    before_save: function(frm) {
        let hasAsset = [];
        let member_values = frm.doc.member;
        member_values.forEach(value => {
            if (! hasAsset.includes(value.asset)) {
                hasAsset.push(value.asset);
                // console.log(hasAsset)
            } else{
                frappe.validated = false;
                frappe.throw(`检查并删除重复的设备后再保存`)
            }
        });
    }
});
```

##### 
```js

frappe.ui.form.on('Asset Group Of System Integration', {
    refresh: function(frm) {
        let member_values = frm.doc.成员组;

        member_values.forEach(value => {
            // console.log(frm);
            // 使用 frappe.call 获取与成员匹配的 Asset 文档
            frappe.call({
                method: 'frappe.client.get_list',
                args: {
                    doctype: 'Asset',  // 目标 Doctype
                    filters: {
                        'name': value.成员  // 过滤条件
                    },
                    fields: ['location']  // 指定要返回的字段
                },
                callback: function(response) {
                    if (response.message) {
                        let location = response.message;
                     
                        let idx = frm.doc.成员组.findIndex(member => member.成员 === value.成员);
                        if (idx !== -1) {
                            frm.doc.成员组[idx].locax =  location[0].location;
                        }
            
                    }
                }
            });
        });

    }
});

```

```js
frappe.ui.form.on('Asset Group Of System Integration', {
    refresh: function(frm) {
        let member_values = frm.doc.成员组;

        member_values.forEach(value => {
            console.log(value.成员);
            // 使用 frappe.call 获取与成员匹配的 Asset 文档
            frappe.call({
                method: 'frappe.client.get_list',
                args: {
                    doctype: 'Asset',  // 目标 Doctype
                    filters: {
                        'name': value.成员  // 过滤条件
                    },
                    fields: ['location']  // 指定要返回的字段
                },
                callback: function(response) {
                    if (response.message) {
                        let location = response.message;
                        console.log(location, value.成员);  // 输出获取的 Asset 对象列表
                        // 根据需要进一步处理 assets
                    }
                }
            });
        });

    }
});

```



##### 子表  
```
多项子表 需要在新建文档时设置添加移除项
```

##### 链路类型
```
```


##### callback

```js
import frappe
//server
@frappe.whitelist()
def get_options_for_b():
    options = frappe.get_all('Doctype A', fields=['x'])
    return [opt['x'] for opt in options]

//client
frappe.ui.form.on('Doctype B', {
    refresh: function(frm) {
        frappe.call({
            method: "path.to.your.script.get_options_for_b",
            callback: function(r) {
                if(r.message) {
                    frm.set_df_property('field_in_b', 'options', r.message.join('\n'));
                }
            }
        });
    }
});
```