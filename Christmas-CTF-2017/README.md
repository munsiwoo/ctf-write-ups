# x-mas-ctf-2017 (1st)


#### session-parser.py
~~~
그누보드에는 /data/session/에서 세션을 관리한다.
/data/session/에 있는 세션에서 admin 세션을 찾는 스크립트
~~~

#### 0-day.md
~~~
0-day 문제 풀면서 삽질했던 거 정리해봤다.
~~~

#### pictube1.html
~~~
픽튜브1 풀며 원평이형, 석찬이와 삽질했던 내용이다.
픽튜브1는 거의 다 풀었는데 대회가 끝나버렸다.
pictube1.html 와 같은 방식으로 풀 수 있고, jsfuck 난독화를 해서 풀수도 있었다.
내가 쓴 pictube1.html 방법은 ([]+prompt)[0] 이런식으로 문자를 만들고
self['docu'+'ment']['cookie'] 이렇게 'document', 'cookie'자리에 넣어서
객체에 접근하거나 함수를 실행시키는 방식이었는데, location이 사용 불가능하다는 것을
대회 끝나고 알았다. 다음에는 location 말고도 여러 방법으로 접근해봐야겠다.
~~~
