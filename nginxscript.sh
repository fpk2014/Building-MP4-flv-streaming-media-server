tar -zxvf pcre-7.9.tar.gz
cd pcre-7.9
./configure && make && make install
cd ../
tar -zxvf zlib-1.2.3.tar.gz
cd zlib-1.2.3
./configure --prefix=/usr/local/pcre && make && make install
cd ../
apt-get install openssl openssl-devel
tar -zxvf yamdi-1.9.tar.gz
cd yamdi-1.9
make && make install
tar -zxvf nginx_mod_h264_streaming-2.2.7.tar.gz
unzip -zxvf nginx-rtmp-module-master.zip
tar -zxvf nginx-1.8.1.tar.gz
cd nginx-1.8.1
./configure --user=www --group=www --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module --with-http_spdy_module --with-http_gzip_static_module --with-ipv6 --with-http_sub_module --with-http_flv_module --with-http_mp4_module --with-pcre=/root/Building-MP4-flv-streaming-media-server/pcre-7.9 --with-zlib=/root/Building-MP4-flv-streaming-media-server/zlib-1.2.3 --add-module=/root/Building-MP4-flv-streaming-media-server/nginx_mod_h264_streaming-2.2.7 --with-http_mp4_module --with-debug --add-module=/root/Building-MP4-flv-streaming-media-server/nginx-rtmp-module-master
make && make install
