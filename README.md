# config_comparision
How to compare configs between two config files. 

Python difflib has been used for comparing purpose. 

Sample output 1: 

1. difference in file_1: 
                           description "Allow UDP snmp port 161
2. difference in file_2: 
                           description "Allow UDP snmp port 161-163"

--------------------------------------------------------------------------------
3. difference in file_1: 
                           src
4. difference in file_2: 
                           src-ip 10.5.15.46/32

--------------------------------------------------------------------------------
5. difference in file_1: 
               policy
6. difference in file_2: 
               policy-statement "REJECT-BOGON-ZZZ"

--------------------------------------------------------------------------------
7. difference in file_2: 
 AA

--------------------------------------------------------------------------------
8. difference in file_1: 
                           community add "RT
9. difference in file_2: 
                           community add "RT-DOOWN-RI-VRF-1-5152-EQUINIX-SV"

--------------------------------------------------------------------------------

Sample output 2: 

1. difference in file_1: 
                   server 1 address 172.22.64.59 secret "Cb26t3Rtuv3ItaYfwhf.0d8hX8bpZ7Ab" hash2

2. difference in file_2: 
                   server 1 address 172.22.64.59 secret "Cb26t3Rtuv3ItaYfwhf.0d8hX8bpZ7Aj" hash2

--------------------------------------------------------------------------------

Sample output 3

1. difference in file_1: 
                   port 1/1/21

2. difference in file_2: 
                   port 1/1/14

--------------------------------------------------------------------------------
3. difference in file_1: 
                       backup 10.100.3.249

4. difference in file_2: 
                       backup 10.100.5.249

--------------------------------------------------------------------------------
5. difference in file_1: 
               interface "IPTV
6. difference in file_2: 
               interface "IPTV-ALT-KNS-V12-EXTERNAL" create

--------------------------------------------------------------------------------
7. difference in file_1: 
               static
8. difference in file_2: 
               static-route-entry 10.100.42.0/24

--------------------------------------------------------------------------------
9. difference in file_1: 
               static
10. difference in file_2: 
               static-route-entry 10.100.59.0/24

--------------------------------------------------------------------------------
11. difference in file_1: 
               static
12. difference in file_2: 
               static-route-entry 10.22.12.0/32

--------------------------------------------------------------------------------
13. difference in file_1: 
               static
14. difference in file_2: 
               static-route-entry 10.222.1.32/32

--------------------------------------------------------------------------------
15. difference in file_1: 
                   interface "IPTV
16. difference in file_2: 
                   interface "IPTV-VLN-U126-OFFICE"

--------------------------------------------------------------------------------
17. difference in file_1: 
                       query
18. difference in file_2: 
                       query-interval 5

--------------------------------------------------------------------------------
19. difference in file_1: 
                       query
20. difference in file_1: 
                       no shutdown

21. difference in file_1: 
                   exit

22. difference in file_1: 
                   interface "IPTV
23. difference in file_2: 
                       query-interval 12

--------------------------------------------------------------------------------
24. difference in file_2: 
                       no shutdown

--------------------------------------------------------------------------------
25. difference in file_2: 
                   exit

--------------------------------------------------------------------------------
26. difference in file_2: 
                   interface "IPTV-BMC"

--------------------------------------------------------------------------------
27. difference in file_1: 
                   interface "IPTV
28. difference in file_2: 
                   interface "IPTV-SAT-PC"

--------------------------------------------------------------------------------
29. difference in file_1: 
                       version 2

30. difference in file_2: 
                       version 56

--------------------------------------------------------------------------------
