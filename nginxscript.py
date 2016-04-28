#! /usr/bin/env python
#conding =utf-8

import os
import sys
import platform
import tarfile
import re
import commands
distribution = platform.linux_distribution()[0]
print distribution
if distribution == 'debian':
    print "true"
else :
    print distribution
    print "your platform is not suport"
    exit()

if os.getuid()!=0:
    print "This program must be run as root. Aborting."
    exit()
else :
    print True
	
commands.getstatusoutput('apt-get install openssl openssl-devel')

def path(name):
    return os.path.join(sys.path[0],name)

def untar(tname):
    f = tarfile.open(tname)
    f.extractall()

def popen(name):
    filepath = path(name)
    commands.getstatusoutput('cd %s && ./configure && make && make install'%filepath)


pcre = path('pcre-7.9.tar.gz')
zlib = path('zlib-1.2.3.tar.gz')
h264_streaming = path('nginx_mod_h264_streaming-2.2.7.tar.gz')
yamdi = path('yamdi-1.9.tar.gz')
rtmp = os.path.join(sys.path[0],'nginx-rtmp-module-master.zip')
nginx = path('nginx-1.8.1.tar.gz')

print 'tar pcre'
untar(pcre)
print 'tar zlib'
untar(zlib)
print 'h264_streaming'
untar(h264_streaming)
print 'yamdi'
untar(yamdi)
print 'nginx'
untar(nginx)
status,output = commands.getstatusoutput('unzip %s'%rtmp)
print output

print 'install pcre\n'
popen('pcre-7.9')

print 'install yamdi\n'
yamdi=path('yamdi-1.9')
commands.getstatusoutput('cd %s && ./configure && make && make install'%yamdi)

print 'install zlib'
zlibpath = path('zlib-1.2.3')
commands.getstatusoutput('cd %s && ./configure --prefix=/usr/local/pcre && make && make install'%zlibpath)
nginxpath = path('nginx-1.8.1')
try:
    print 'install nginx'
    com = 'cd %s && ./configure --user=www --group=www --prefix=/usr/local/nginx \
    --with-http_stub_status_module --with-http_ssl_module --with-http_spdy_module \
    --with-http_gzip_static_module --with-ipv6 --with-http_sub_module --with-http_flv_module \
    --with-http_mp4_module --with-pcre=%s \
    --with-zlib=%s \
    --add-module=%s \
    --with-http_mp4_module --with-debug \
    --add-module=%s'%(nginxpath,path('pcre-7.9'),zlibpath,path('nginx_mod_h264_streaming-2.2.7'),path('nginx-rtmp-module-master'))
    commands.getstatusoutput(com)
    bugpath = nginxpath + "/objs/Makefile"
    file1=open(bugpath)
    fileread=file1.read()
    file1.close()
    file2=open(bugpath,'w+')
    pattern=re.compile('-Werror')
    finalfile=re.subn(pattern,'',fileread)
    filestring=finalfile[0]
    file2.write(filestring)
    file2.close()
    commands.getstatusoutput('cd %s && make && make install' % nginxpath )
    print 'OK'
except:
    print "install falsed"
    
