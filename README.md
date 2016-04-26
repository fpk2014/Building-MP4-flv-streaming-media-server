# Building-MP4-flv-streaming-media-server
这是一个小白写的搭建MP4，flv拖动播放的脚本。
1.脚本需要安装lnmp,目前该脚本只在raspibian上测试过，支持debian系统，也可能支持ubuntu（待测试）
  推荐lnmp一键安装脚本
2.安装方法:
           chmod 777 nginxscript.sh
		   ./nginxscript.sh
3.编译nginx时可能有一些bug,这时候打开nginx目录下的Makefile文件，删除-Werror。再执行make && make install。
  其它问题待发现
4.脚本需要修改/opt/nginx/conf/nginx.conf，添加flv,mp4的支持
