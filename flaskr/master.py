import os
from re import split
import time
import threading
import ipaddress
import socket
from traceback import print_tb
from kazoo.client import KazooClient
from kazoo.exceptions import KazooException, LockTimeout
from kazoo.handlers.threading import KazooTimeoutError



def connect_to_server(ip, port, ticket):
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((ip, int(port)))
            
            client_socket.sendall(ticket.encode())

            message_from_server = client_socket.recv(1024).decode()
            print(f"message from server: {message_from_server}")

            client_socket.close()
            break

        except Exception as e:
            print(f"connect failed!: {e}")
            time.sleep(1)  # 等待一秒再嘗試連接



def start_service(zk, ticket):
    try:
        children = zk.get_children('/server')
        while True:
            if len(children) == 0:
                return False
            else:
                for child in children:
                    child_path = '/server/' + child 
                    lock_path =  '/server/' + child.split("_")[1] 
                    if zk.exists(lock_path):
                        continue
                    else:
                        zk.create(lock_path)
                        data, _ = zk.get(child_path)
                        ip, port = data.decode().split(":")
                        print(f"Connecting to server {ip}:{port} ...")
                        connect_to_server(ip, port, ticket)
                        zk.delete(lock_path)
                        return True
    except Exception as e:
        print(f"Kazoo connect error : {e}")
                
            

def main(ticket, buyer):
    try:
        print(f"Processing ticket {ticket} for {buyer}...")
        zk = KazooClient(hosts='127.0.0.1:2181')
        zk.start(timeout=10)
        
        available_server = zk.get_children('/server')
        if len(available_server) == 0:
            return False
        else:
            service_state =  start_service(zk, ticket)
            zk.stop()
            return service_state
        
    except KazooTimeoutError:
        print("Zookeeper connection timed out")
    except KazooException as e:
        print(f"An error occurred with KazooClient: {e}")
