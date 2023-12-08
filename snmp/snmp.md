```bash

```
```
参数
–h：显示帮助。
–v：指定snmp的版本, 1或者2c或者3。
–c：指定连接设备SNMP密码。
–V：显示当前snmpwalk命令行版本。
–r：指定重试次数，默认为0次。
–t：指定每次请求的等待超时时间，单为秒，默认为3秒。
–l：指定安全级别：noAuthNoPriv|authNoPriv|authPriv。
–a：验证协议：MD5|SHA。只有-l指定为authNoPriv或authPriv时才需要。
–A：验证字符串。只有-l指定为authNoPriv或authPriv时才需要。
–x：加密协议：DES。只有-l指定为authPriv时才需要。
–X：加密字符串。只有-l指定为authPriv时才需要。


``` 
#-c 社区
public： 非敏感共享社区，访问无任何权限
Private社区：Private社区名称用于共享敏感信息的SNMP设备，只有经过授权的用户才能够使用该社区名称进行访问。

ReadOnly社区：ReadOnly社区名称用于共享只读信息的SNMP设备，只有读取权限的用户才能够使用该社区名称进行访问。

ReadWrite社区：ReadWrite社区名称用于共享读写信息的SNMP设备，只有读写权限的用户才能够使用该社区名称进行访问。

Trap社区：Trap社区名称用于发送SNMP Trap消息，它用于向管理站点发送SNMP设备的警告或错误信息。
```
通过OID查询

snmpwalk  -v 2c -c public 192.168.0.108  .1.3.6.1.2.1.4.20 


OID对应关键字参考表：
1	3	6	1	           2    1	   1      5      0
iso	org	dod	internet	mgmt	mib-2	system	sysName	end

通过关键字查询::省略掉OID对应的关键字，
snmpwalk -v 2c -c public 192.168.0.108 IF-MIB::ifDescr

翻译
snmptranslate -Td IF-MIB::ifDescr
snmptranslate -Td SNMPv2-MIB::system

节点取名
snmpset -v 2c -c public localhost SNMPv2-MIB::sysContact.0 s 'test'



ifDescr OBJECT-TYPE
    SYNTAX      DisplayString
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
            "A textual string containing information about the
            interface.  This string should include the name of the
            manufacturer, the product name and the version of the
            interface hardware/software."
    ::= { ifEntry 2 }


IF-MIB::ifDescr.1 = STRING: lo
IF-MIB::ifDescr.2 = STRING: eth0
IF-MIB::ifDescr.3 = STRING: wlan0
```



