
port=7700
key=$(openssl rand -base64 24)
echo $key >$(pwd)/master-key
docker run -itd --rm \
  -p $port:7700 \
  -v $(echo $HOME)/.meili_data:/meili_data \
  getmeili/meilisearch:v1.2   \
  meilisearch  --schedule-snapshot --snapshot-dir /meili_data/snapshots --master-key=$key
  
