```bash
#no persistence
docker run -it --rm \
  --name mysearch \
  -p 7700:7700 \
  -e MEILI_MASTER_KEY='22mq69uVK7ELCzLOMOR58Yej8wBj9ox4'\
  -v "$HOME"/backup/meili_data:/meili_data \
  getmeili/meilisearch:v1.0



docker run -it -d \
  --name mysearch \
  --restart always \
  -p 7700:7700 \
  -e MEILI_MASTER_KEY='22mq69uVK7ELCzLOMOR58Yej8wBj9ox4'\
  -v "$HOME"/backup/meili_data:/meili_data \
  getmeili/meilisearch:v1.0



```
```python
import meilisearch
import nanoid
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
http_addr = "http://127.0.0.1:7700"
master_key = "lVboGYgZUR8mnCcMLCCXUb2NvphGaMft"
index_space = "mysearch"

def generate_id(size:str=16)->str:
  random_string = nanoid.generate(characters, size=size)
  return random_string 
generate_id(24)


documents = []
for i in range(1000):
  documents.append(
    { 
      "uid" : generate_id(24),
      "title" : generate_id(64)
  })

client = meilisearch.Client(http_addr, master_key)
client.create_index(uid=index_space)
index = client.index(index_space)
index.delete_all_documents()
result = index.add_documents(documents) 
#

documents=[{"uid":"1ad","title":"pwdzxd","link":"http://baidu.com"}]

client.index('mysearch').update_settings({
  'stopWords': [
      '的'
  ],
})


#delete
client.delete_index("mysearch")
```

```bash
 准备 OR 数据 OR 搜
result : 准备写入搜索的数据
result : 准备一些礼品去参加婚礼

```


```bash
docker run -it --rm \
  -p 7700:7700 \
  -v $(pwd)/meili_data:/meili_data \
  getmeili/meilisearch:v1.0
  meilisearch --schedule-snapshot --snapshot-dir /meili_data/snapshots


  docker run -it --rm \
  -p 7700:7700 \
  -v $(pwd)/meili_data:/meili_data \
  getmeili/meilisearch:v1.0
  meilisearch --import-snapshot /meili_data/snapshots/data.ms.snapshot
 
 #delect from id
client.index('mysearch').delete_document(4)    
```


```bash
#start at  bash
#rm  -rf build
#change REACT_APP_MEILI_SERVER_ADDRESS in  package.json and 
#REACT_APP_MEILI_SERVER_ADDRESS=http://192.168.99.214:7700 yarn build
#yarn global add serve
serve -d build -p 8001

```

```js
// hide images
    <CustomCard>
      {/* <Box width={240} mr={4} flexShrink={0}> */}
      <Box width={0} mr={4} flexShrink={0}>
        {hit[imageKey] ? (
          <LazyLoadImage
            src={hit[imageKey] || null}
            width="100%"
            style={{ borderRadius: 10 }}
          />
        ) : (
          <EmptyImage />
        )}
      </Box>
```