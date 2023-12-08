# Encryption

  ## 
   ### gzexe
   > encrypt a shell script
   ```bash
    gzexe foo.sh
    cat foo.sh 
    ./foo.sh
   ```
   >exception
   ```
    /usr/bin/gzexe: foo.sh is already gzexe'd
    
   ```

   ### openssl
   > 
   ```bash
   sudo ps -e | grep ssh
   sudo /etc/init.d/ssh start
   sudo apt-get install openssh-server
   ```

   ### ufw
   >
   ```bash
  ufw status
  ufw enable
  ufw allow 22/tcp
  ufw deny $port/tcp
  ufw delete $port/tcp
   ```
