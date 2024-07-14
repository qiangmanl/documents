NMS负责采样网络中agent的信息，并接受agent的trap
agent在UDP的161端口接收NMS的读写请求消息，NMS在UDP的162端口接收agent的事件通告消息。
get:  NMS get agent message
set: NMS  transport message to  agent for  set client 