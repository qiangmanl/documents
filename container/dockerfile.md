
  ## DockerFile
   ### dockerfile format
   >FROM <image>:<tag>
   >MAINTAINER #who are the maintainer
   >RUN #run with container building
   >ADD #步骤，tomcat镜像，这个tomcat压缩包，添加内容
   >WORKDIR #镜像的挂载目录
   >VOLUME #挂载的目录
   >EXPOST #export container's port
   >CMD #run with container run
   >ENTRYPOINT #指定这个容器启动的时候要运行的命令，可以追加命令
   >COPY #类似ADD，将我们文件拷贝到镜像中
   >ENV #构建的时候设置环境变量

