#! /usr/bin/env python
#conding =utf-8

import os
import sys
import platform
import tarfile
import re
import commands


distribution = platform.linux_distribution()[0]
if distribution == "Ubuntu" or distribution == "Debian":
    print "you platform is suporting"
else :
    print "your platform is not suporting"
    exit()
if os.getuid()!=0:
    print "This program must be run as root. Aborting."
    exit()

    
def path(name):
    return os.path.join(sys.path[0],name)

def untar(tname):
    print "untar" + tname
    f = tarfile.open(path(tname))
    f.extractall()
    
def installOp(command, name):
    print "install" + name
    print "execute" + command
    status,output = commands.getstatusoutput(command)
    print output
    
def install(name):
    print "install "+name
    filepath = path(name)
    printOp('cd %s && ./configure && make && make install'%filepath)


untar('pcre-7.9.tar.gz')
untar('zlib-1.2.3.tar.gz')
untar('nginx_mod_h264_streaming-2.2.7.tar.gz')
untar('yamdi-1.9.tar.gz')
untar('nginx-1.8.1.tar.gz')

print "unzip nginx-rtmp-module-master.zip"
rtmp = os.path.join(sys.path[0],'nginx-rtmp-module-master.zip')
status,output = commands.getstatusoutput('unzip %s'%rtmp)
print output

installOp('apt-get install openssl openssl-devel', "openssl")
install('pcre-7.9')
install('yamdi-1.9')
installOp('cd %s && ./configure --prefix=/usr/local/pcre && make && make install'%path('zlib-1.2.3'), "zlib")


com = 'cd %s && ./configure --user=www --group=www --prefix=/usr/local/nginx \
    --with-http_stub_status_module --with-http_ssl_module --with-http_spdy_module \
    --with-http_gzip_static_module --with-ipv6 --with-http_sub_module --with-http_flv_module \
    --with-http_mp4_module --with-pcre=%s \
    --with-zlib=%s \
    --add-module=%s \
    --with-http_mp4_module --with-debug \
    --add-module=%s'%(path('nginx-1.8.1'),path('pcre-7.9'),path("zlib-1.2.3"),path('nginx_mod_h264_streaming-2.2.7'),path('nginx-rtmp-module-master'))
installOp(com, "configure nginx")

print "write '-Werror' into Makefile"
bugpath = path('nginx-1.8.1') + "/objs/Makefile"
with open(bugpath) as f:
    data = f.read();
f.close()
filestring=re.subn('-Werror','',data)[0]
with open(bugpath, "w+") as f:
    f.write(filestring)
f.close()

installOp('cd %s && make && make install' % nginxpath, "nginx")
print 'install ngninx success'
