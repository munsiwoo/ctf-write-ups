# Interweb Write-ups (1100pt)

### ajax_not_soap (100)
~~~
webhooks/get_username.php 로 이동하면 MrClean이란 username을 알려준다.
MrClean을 webhooks/get_pass.php?username=MrClean 이렇게 get_pass.php에 대입해주면
flag가 나온다. flag{hj38dsjk324nkeasd9}
~~~

### ajax_not_borax (200)
~~~
webhooks/get_username.php 로 이동하면 c5644ca91d1307779ed493c4dedfdcb7 라는 해시값이 나온다.
이걸 hashkiller에 놓고 돌리면 tideade가 나오고 webhooks/get_pass.php?username=tideade 이렇게 대입해주면
base64로 인코딩된 flag가 나온다. ZmxhZ3tzZDkwSjBkbkxLSjFsczlISmVkfQ==
flag{sd90J0dnLKJ1ls9HJed}
~~~

### the_red_or_blue_pill (100)
~~~
접속하면 red pill하고 blue pill을 선택할 수 있다.
red pill을 누르면 ?red 파라미터가, blue pill을 먹으면 ?blue 파라미터가 생기는데
밑에 "red pill하고 blue pill을 동시에 먹으면 안되냐?"라는 지문을 보고
red 파라미터와 blue 파라미터를 동시에 주었더니 flag가 나왔다. 
/?red&blue
# Well you chose option 3 which clearly was stated not to do. Good job! :)
# flag{breaking_the_matrix...I_like_it!}
~~~

### tik-tik-boom (300)
~~~
접속에서 html을 보면 username and password did not match: admin hahahaN0one1s3verGett1ngTh1sp@ssw0rd
라는 문구가 눈에 띈다, cookie에 username, password라는 cookie가 있는데
각각 username=admin;password=hahahaN0one1s3verGett1ngTh1sp@ssw0rd; 이렇게 바꿔주면 flag가 나온다.
단 *시 23분 59초에 새로고침해야 flag가 나온다.
~~~

### Das_blog (200)
~~~
로그인 페이지에서 주석처리된 테스트 계정을 확인할 수 있다.
이 테스트 계정으로 로그인하면 permissions=user라는 쿠키 세션이 생기는데
permissions을 admin으로 바꾸고 최상위 디렉토리로 이동하면 flag를 얻을 수 있다.

flag{C00ki3s_c4n_b33_ch4ng3d_?}
~~~

### What the LFI? (200)
~~~
워드프레스에서 발생하는 LFI 취약점을 다루는 문제다.
wpscan 도구를 사용해서 SAM Pro에서 발생하는 LFI 존재를 알 수 있었고
"wordpress SAM Pro LFI" 키워드로 검색해보니
/wp-content/plugins/sam-pro-free/sam-pro-ajax-admin.php 에서 LFI가 발생한다는 것을 알았다.

ref: https://www.pluginvulnerabilities.com/2016/10/28/local-file-inclusion-lfi-vulnerability-in-sam-pro-free-edition/

위 게시물을 확인할 수 있었고 해당 게시물을 토대로 공격하여 flag를 획득했다.
http://54.201.224.15:14099/wp-content/plugins/sam-pro-free/sam-pro-ajax-admin.php?action=NA&wap=L3Zhci93d3cvYmxhaC5waHA=

flag{dont_include_files_derived_from_user_input_kthx_bai}
~~~