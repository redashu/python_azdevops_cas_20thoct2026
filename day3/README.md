# python_azdevops_cas_20thoct2026

### Review 

<img src="rev1.png">

### Installing pytest module 

```
root@docker-ubuntu:~/ashu-codes# source  casinoar-ashu/bin/activate
(casinoar-ashu) root@docker-ubuntu:~/ashu-codes# pip3 install pytest 
Collecting pytest
  Downloading pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
Collecting iniconfig>=1.0.1 (from pytest)


===>

casinoar-ashu) root@docker-ubuntu:~/ashu-codes# pip3 list 
Package            Version
------------------ ----------
certifi            2026.10.19
charset-normalizer 3.5.2
idna               3.20
iniconfig          2.3.1
packaging          26.3
pip                24.0
pluggy             1.7.0
Pygments           2.21.0
pytest             9.1.1
requests           2.34.2
urllib3            2.8.0
(casinoar-ashu) root@docker-ubuntu:~/ashu-codes# pip3 install pytest 




```

### using pytest to of automated testing 

```
pytest  -v  day3/test_cal.py  
======================================== test session starts =========================================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.7.0 -- /root/ashu-codes/casinoar-ashu/bin/python3
cachedir: .pytest_cache
rootdir: /root/ashu-codes
collected 1 item                                                                                     

day3/test_cal.py::test_add PASSED                                                              [100%]

========================================= 1 passed in 0.01s ==========================================
(casinoar-ashu) root@docker-ubuntu:~/ashu-codes# 

```