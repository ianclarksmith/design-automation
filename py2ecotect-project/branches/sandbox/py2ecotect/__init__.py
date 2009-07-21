#win32 is required: http://python.net/crew/mhammond/win32/
import win32ui
import win32api
import dde

#Create a conversation with Ecotect
server = dde.CreateServer()
server.Create("Ecotect-Server") 
conversation = dde.CreateConversation(server)

#Create the connection
#Start Ecotect if necessary
try:
    conversation.ConnectTo("Ecotect", "request")
except:
    win32api.WinExec("C:\\Program Files\\Autodesk\\Ecotect 2009\\ecotect.exe")
    conversation.ConnectTo("Ecotect", "request")
    
print "conv = ", conversation
print "Connection with Ecotect successful..."