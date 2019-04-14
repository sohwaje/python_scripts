#!/usr/bin/env bash

NGINX_ROOT_PATH=/nginx
NGINX_CONF_PATH=$NGINX_ROOT_PATH/conf
NGINX_PID_PATH=$NGINX_ROOT_PATH/pid
NGINX_ACCESS_LOG_PATH=$NGINX_ROOT_PATH/log
NGINX_ERROR_LOG_PATH=$NGINX_ROOT_PATH/log
NGINX_LIBS_PATH=$NGINX_ROOT_PATH/libs
NGINX_ADDITIONAL_MODULE_PATH=$NGINX_ROOT_PATH

mkdir -p $NGINX_ROOT_PATH
mkdir -p $NGINX_CONF_PATH
mkdir -p $NGINX_PID_PATH
mkdir -p $NGINX_ACCESS_LOG_PATH
mkdir -p $NGINX_ERROR_LOG_PATH
mkdir -p $NGINX_LIBS_PATH
mkdir -p $NGINX_ADDITIONAL_MODULE_PATH

(cd $NGINX_LIBS_PATH/nginx-1.15.11 &&


./configure \
--sbin-path=$NGINX_ROOT_PATH \
--conf-path=$NGINX_CONF_PATH/nginx.conf \
--pid-path=$NGINX_PID_PATH/nginx.pid \
--error-log-path=$NGINX_ERROR_LOG_PATH/error.log \
--http-log-path=$NGINX_ACCESS_LOG_PATH/access.log \
--with-pcre=$NGINX_LIBS_PATH/pcre-8.41 \
--with-zlib=$NGINX_LIBS_PATH/zlib-1.2.11 \
--with-openssl=$NGINX_LIBS_PATH/openssl-1.0.2f \
--with-http_ssl_module \
--with-http_v2_module \
--with-http_realip_module \
--with-http_addition_module \
--with-http_xslt_module \
--with-http_image_filter_module \
--with-http_geoip_module \
--with-http_sub_module \
--with-http_dav_module \
--with-http_flv_module \
--with-http_mp4_module \
--with-http_gunzip_module \
--with-http_gzip_static_module \
--with-http_auth_request_module \
--with-http_random_index_module \
--with-http_secure_link_module \
--with-http_slice_module \
--with-http_degradation_module \
--with-http_stub_status_module \
--with-http_perl_module \
--with-mail \
--with-mail_ssl_module \
--with-stream \
--with-stream_ssl_module \
--with-google_perftools_module \
--with-cpp_test_module \
--with-debug \
--prefix=$NGINX_ADDITIONAL_MODULE_PATH &&

make install)
