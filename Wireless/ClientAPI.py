import xmlrpclib, os

#TODO: Get IP address of the user machine directly, no need to pass it to the Create and Delete functions

#ServerIP = "localhost"
#ServerPort = 50000

client_ip1 = "79.79.79.79"
client_ip2 = "192.168.54.14"

XMLstring1 = open("/home/laragoxhaj/gini-src/gini/lib/gini/gbuilder/Wireless/topinterferenc1.xml").read()
#XMLstring2 = open("topinterferenc2.xml").read()

class wgini_client:
	def __init__(self, ip, port):
		self.conn = xmlrpclib.ServerProxy("http://" + str(ip) + ":" + str(port))

	def Check(self):
		return self.conn.Check()

	def Create(self, XMLstring, ip):
		return self.conn.Create(XMLstring, ip)

	def Delete(self, ip):
		return self.conn.Delete(ip)

#client = wgini_client(ServerIP, ServerPort)

#status = client.Create(XMLstrisng, client_ip)

#print status
