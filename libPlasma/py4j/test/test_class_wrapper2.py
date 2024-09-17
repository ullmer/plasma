# Code generated by CoPilot on 2024-09-16, in response to query:
# "please provide example python and java code using py4j.  The java file should include a
#   class testClass with integer variables A and B.  The python file should provide a wrapper
#   that accesses these testClass variables."

# test_class_wrapper.py
from py4j.java_gateway import JavaGateway, GatewayParameters 

gwparam = GatewayParameters(address='172.25.49.14', port=25333)

# Connect to the Java Gateway
gateway = JavaGateway(gateway_parameters=gwparam)

# Access the TestClass instance
test_class = gateway.entry_point

# Get the values of A and B
A = test_class.getA()
B = test_class.getB()

print(f"Value of A: {A}")
print(f"Value of B: {B}")

# Set new values for A and B
test_class.setA(30)
test_class.setB(40)

# Get the updated values of A and B
A = test_class.getA()
B = test_class.getB()

print(f"Updated value of A: {A}")
print(f"Updated value of B: {B}")

### end ###
