# The WIFI Network (200)

~~~
Name: The WIFI Network

Author: bashninja

Description: So we're still trying to get into the Jedi Archives. Let's try cracking the WiFi. Here's a WPA2 Handshanke I picked up while near the building.
~~~

cap to hccapx : https://hashcat.net/cap2hccapx/

rockyou.txt : http://www.mediafire.com/file/7d7nz2kku7urzor/rockyou.txt

~~~
> hashcat neverlan.hccapx -a 0 -m 2500 rockyou.txt
~~~

flag{obiwan17}