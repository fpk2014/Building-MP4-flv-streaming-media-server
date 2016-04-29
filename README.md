
1.本脚本需要安装lnmp,目前该脚本在raspibian上顺利安装nginx，支持debian系统，也可能支持ubuntu（待测试）
  
  lnmp一键安装包：http://lnmp.org/

2.如果文件夹中已经存在了解压出来的文件夹：nginx_mod_h264_streaming-2.2.7，nginx-1.8.1，nginx-rtmp-module-master，
  pcre-7.9，yamdi-1.9，zlib-1.2.3，安装前需要删除这些文件夹。

3.安装方法:
           python nginxscript.py

4.安装完成输入nginx -V，查看是否已经安装了zlib,pcre,nginx_mod_h264_streaming,nginx-rtmp-module

5.脚本需要修改/opt/nginx/conf/nginx.conf，添加flv,mp4的支持
 
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
        
*********************************************添加的东西**************************************************************************
        location /nginx_status
        {
            stub_status on;
            access_log   off;
        }


联系：994347033@qq.com
