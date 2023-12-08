```bash
#生成一个RSA私钥文件  
openssl genpkey -algorithm RSA   -out private.key
#生成一个椭圆加密私钥文件  
openssl ecparam -genkey -name prime256v1 -out private.key

openssl req -new -key private.key -out certificate.csr

openssl x509 -req -days 365 -in certificate.csr -signkey private.key -out ihotel.com.crt




```

```json
example.com {
    tls /path/to/example-ec.crt /path/to/example-ec.key
    # 其他 Caddy 配置项
}
```

