# Introduction
This is a simple ticketing system. Using the distributed architecture of Zookeeper, We applied Zookeeper not just as a database tool, but also for server load balancing to prevent crashes due to server overload. 

# Activate Zookeeper server
After downloding the apache-zookeeper, activate two zookeeper server about: 
```
bin/zkServer.sh start-foreground conf1/zoo.cfg
```
```
bin/zkServer.sh start-foreground conf2/zoo.cfg
```
In the begining, you have to create the conf1 and conf2 folder. In these two folders, we need to create zoo.cfg respectively. 
Then, we can refer to the example built in Zookeeper.
In our given Download.zip, we have already default the settings, all you need to revise the "dataDir" path to your own path. 
# watch zookeeper server by client
You can watch the znode in the zookeeper server by connecting to server via client 
```
bin/zkCli.sh -server localhost:2181
```
Zookeeper APIs are available.
# Activate ticket server
run server1, server2, server3

# Activate the app
