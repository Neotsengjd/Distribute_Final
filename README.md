# Introduction
This is a simple ticketing system using the distributed architecture of Zookeeper. <br />
We utilize Zookeeper not just as a database tool, but also provide back server load balancing to prevent crashes due to overload situations. 
<br />
# Zookeeper setup
## Configuration file setup
First of all, unzip the apache-zookeeper pack and look into the conf1 and conf2 folder. <br />
In these two folders, we need to modify the data path in zoo.cfg file respectively. <br />
For example:
```
dataDir = /yourLocalPath/apache-zookeeper-3.8.4-bin/data1
```

## Activate Zookeeper server
After setting up zoo.cfg files, we can activate Zookeeper servers on two different terminals using the following commands: 

```
bin/zkServer.sh start-foreground conf1/zoo.cfg
```

```
bin/zkServer.sh start-foreground conf2/zoo.cfg
```
This will start a zookeeper ensemble, which is necessary to our system.

## Monitor zookeeper server using Zookeeper client API
You can watch the znodes in the zookeeper server by connecting to server via Zookeeper API.
```
bin/zkCli.sh -server localhost:2181
```
For more detailed API operations, please check out official document https://zookeeper.apache.org/doc/current/zookeeperCLI.html

---

# Ticketing system
## Kazoo and Flask
### Kazoo
Kazoo is a Python library designed to make working with Zookeeper a more hassle-free experience that is less prone to errors. <br />
Use the following command to install kazoo:
```
pip install kazoo
```

### Flask
Flask is a lightweight and flexible web framework for Python, which allows us to build a ticketing system website. <br />
Use the following command to install kazoo:
```
pip install flask
```

## Activate back server
Run server1, server2, server3 on different terminal respectively.
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
python3 app.py
```
Click on the generated link and you'll be able to open the ticketing system website.