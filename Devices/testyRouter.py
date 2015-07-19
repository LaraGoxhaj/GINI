from Core.Connection import *
from Core.Interfaceable import *
from Core.globals import environ
from PyQt4 import QtCore

class yRouter(Interfaceable):
    device_type = "yRouter"

    # Constructor: Initialise a router device
    def __init__(self):
	print 'success 0'
	Interfaceable.__init__(self)
        #Device.__init__(self)
	print 'success 1'
        self.interface = []
        self.num_interface=0
        self.connection=[]
        self.con_int={}                 # connection and interface pair
        self.next_interface_number=0
	self.menu = []
        # by default, auto compute routing table is off
        self.auto=0
	print 'success 2'
	# ifconfig parameters
        self.properties[QtCore.QString("destIP")]=""
        self.properties[QtCore.QString("destPort")]=""
        self.properties[QtCore.QString("ip")]=""
        self.properties[QtCore.QString("mac")]=""
	print 'success 3'
        self.interfaces.append({
            QtCore.QString("subnet"):QtCore.QString(""),
            QtCore.QString("mask"):QtCore.QString(""),
            QtCore.QString("ipv4"):QtCore.QString(""),
            QtCore.QString("mac"):QtCore.QString(""),
            QtCore.QString("routing"):[]})
	print 'success 4'
        self.lightPoint = QtCore.QPoint(-19,-3)
	print 'success 5'

    def generateToolTip(self):
        """
        Add subnet IP address to the tooltip for easier lookup.
        """
        tooltip = self.getName()
        interface = self.getInterface()
        tooltip += "\n\nSubnet: " + interface[QtCore.QString("subnet")] + "\n"
        tooltip += "IP: " + interface[QtCore.QString("ipv4")]
        self.setToolTip(tooltip)
