import anvil.server
import gkeepapi

anvil.server.connect("QJVRB4LEFOFXTTI4QK3DVVXR-R4IKANFI5NQKZ2RD")

@anvil.server.callable
def test_call():
    keep = gkeepapi.Keep()
    success = keep.login('isburenkov@gmail.com', 'EpZiL6xOeH')
    
    note = keep.createNote('Todo', 'Eat breakfast')
    note.pinned = True
    note.color = gkeepapi.node.ColorValue.Red
    keep.sync()
	
@anvil.server.callable
def say_hello(name):
	print("Hello from your own machine, %s!" % name)
	
anvil.server.wait_forever()