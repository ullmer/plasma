#Generated by co-pilot, 2024-09-17, per query
# python and java example for py4j code where a java event drives a python callback.

from py4j.java_gateway import JavaGateway, CallbackServerParameters

class PythonCallback:
    def onEvent(self):
        print("Event triggered from Java")

if __name__ == "__main__":
    gateway = JavaGateway(callback_server_parameters=CallbackServerParameters())
    event_trigger = gateway.entry_point
    callback = PythonCallback()
    event_trigger.setCallback(callback)
    
    # Trigger the event from Java
    event_trigger.triggerEvent()
    
    # Keep the Python script running to listen for events
    gateway.callback_server.start()
