
1.脚本需要安装lnmp,目前该脚本只在raspibian上测试过，支持debian系统，也可能支持ubuntu（待测试）

2.安装方法:
           chmod 777 nginxscript.sh
		   ./nginxscript.sh

3.编译nginx时可能有一些bug,这时候打开nginx目录下的Makefile文件，删除-Werror。再执行make && make install。
  其它问题待发现

4.脚本需要修改/opt/nginx/conf/nginx.conf，添加flv,mp4的支持
 
  输入nano /opt/nginx/conf/nginx.conf
******************************************************************************************************************** 
  server
  
    {
    
        listen 80 default_server;
        
        #listen [::]:80 default_server ipv6only=on;
        
        server_name www.lnmp.org;
        
        index index.html index.htm index.php;
        
        root  /home/wwwroot/default;

        #error_page   404   /404.html;
        
        include enable-php.conf;
********************************************添加的东西****************************************************************
        
        location ~ \.flv$
        {
          flv;
        }
		location ~ \.mp4$ {
          mp4;
        }
        
***********************************************************************************************************************
        location /nginx_status
        {
            stub_status on;
            access_log   off;
        }
