
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()  # Connect to the JVM
raft_node = gateway.entry_point  # Get the RaftNodeApp instance

status = raft_node.getStatus()
print(f"RAFT Node Status: {status}")
