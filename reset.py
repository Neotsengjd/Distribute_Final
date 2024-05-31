from kazoo.client import KazooClient

zk = KazooClient(hosts='localhost:2181')
zk.start()

groups = ["A", "B", "C"]
default_quantity = 3

for ticketType in groups:
    ticket_path = f"/data/ticket/{ticketType}/quantity"
    try:
        zk.set(ticket_path, str(default_quantity).encode("utf-8"))
    except Exception as e:
        print(f"Failed to set quantity for {ticketType}: {e}")

zk.stop()