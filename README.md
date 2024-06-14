# Introduction
This is a simple ticketing system. Using the distributed architecture of Zookeeper, We applied Zookeeper not just as a database tool, but also for server load balancing to prevent crashes due to server overload. 

# Activate Zookeeper 
After downloding the apache-zookeeper, activate two zookeeper server about: 
```bin/zkServer.sh start-foreground conf1/zoo.cfg```
```
bin/zkServer.sh start-foreground conf2/zoo.cfg
```
# Activate ticket server
run server1, server2, server3

# Activate the app
