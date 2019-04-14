#!/usr/bin/env bash

NGINX_ROOT_PATH=/nginx
NGINX_LIBS_PATH=$NGINX_ROOT_PATH/libs

-f $NGINX_LIBS_PATH || mkdir -p $NGINX_LIBS_PATH

(cd $NGINX_LIBS_PATH &&
wget http://nginx.org/download/nginx-1.15.11.tar.gz
tar -xvf nginx-1.15.11.tar.gz &
wget http://zlib.net/zlib-1.2.11.tar.gz
tar -xvf zlib-1.2.11.tar.gz &
wget http://downloads.sourceforge.net/project/pcre/pcre/8.41/pcre-8.41.tar.gz
tar -xvf pcre-8.41.tar.gz &
wget http://www.openssl.org/source/openssl-1.0.2f.tar.gz
tar -xvf openssl-1.0.2f.tar.gz
)
