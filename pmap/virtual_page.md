```bash
printf %x  $((0x7fb97738e000 - 0x7fb97738c000)) \n

十六进制先装换成十进制再相加
echo $((0x55b852ea2000 + 0x00036000))
#获得页面大小
getconf PAGE_SIZE

#更详细
sudo cat /proc/<PID>/maps


PAGE_SIZE=2^x  其中x是偏移量
例如PAGE_SIZE 为4096
页面号为地址偏移x

echo $((0x0000000000711000 >> 12)) #1809
cat /proc/<pid>/pagemap |grep 1809

00007fffa5e2b000 
echo $((0x00007fffa5e2b000 >> 12)) 
```
