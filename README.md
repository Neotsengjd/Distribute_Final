# Introduction
This is a simple ticketing system using the distributed architecture of Zookeeper. 
We applied Zookeeper not just as a database tool, but also for back server load balancing to prevent crashes due to overload situationss. 

# Zookeeper setup
## Configuration file setup
First of all, unzip the apache-zookeeper pack, and you'll have to look into the conf1 and conf2 folder. In these two folders, we need to modify the data path in zoo.cfg file respectively.
For example:
```
dataDir = /yourLocalPath/apache-zookeeper-3.8.4-bin/data1
```

## Activate Zookeeper server
After setting up zoo.cfg files, we can activate zookeeper servers on two different terminals using the following commands: 

```
bin/zkServer.sh start-foreground conf1/zoo.cfg
```

```
bin/zkServer.sh start-foreground conf2/zoo.cfg
```
This will start a zookeeper ensemble, which is necessary to our system.

## Monitor zookeeper server using Zookeeper client API
You can watch the znode in the zookeeper server by connecting to server via zookeeper API 
```
bin/zkCli.sh -server localhost:2181
```
For more detailed API operations, please check out official document https://zookeeper.apache.org/doc/current/zookeeperCLI.html

---

# Ticketing system
## Activate back server
run server1, server2, server3 on different terminal respectively
```
python3 server1.py 
```
```
python3 server2.py
```
```
python3 server3.py 
```
## Start the system
```
flask run app.py
```
