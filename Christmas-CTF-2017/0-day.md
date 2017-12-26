### 0-day 삽질한거

~~~
1. 파일 업로드에서 shtml, xml, xhtml 등 올려서 rce, xxe 시도
2. sqli, lfi 찾다가 없어서 포기
3. 세션에서 admin 계정 찾아보기 (session_parser.py 참고)
~~~

~~~
결론 : 진짜 0-day 였다.
~~~