```bash
#过滤去空行去头去尾
pmap  351456 |sed 's/.* //'|sed 's/]//'  | grep -v '^$' |head -n -1 |tail -n +2

#指定行awk好用 NR可以做不等条件
ls -al |awk 'NR==2'
ls -al |sed -n 1p


#awk 条件显示2-10
ls -al |nl |awk 'NR>=2 && NR <10'

#去掉空行
grep -v '^$'

#去尾1行
head -n -1 

#去头1行（n+1）
tail -n +2
# 's/.* //' 所有空格前面的所有内容全部替换成空   'aaa bbb 111 2,dd' =>'2,dd'
#sed 's/[^,]*,//'  第一个，的所有内容 + , 替换成空   'addda,fa'=> 'fa'
sed 's/.* //' SPY_1hour_sample.txt |sed 's/[^,]*,//'  
 #,后面的内容替换为空
sed 's/,.*//'


```

