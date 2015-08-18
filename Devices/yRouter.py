from Router import *
from PyQt4 import QtCore

class yRouter(Router):
    device_type="yRouter"

    def __init__(self):
        Device.__init__(self)

        self.interface = []
        self.num_interface=0
        self.connection=[]
        self.con_int={}                         # the connection and interface pair connection
        self.next_interface_number=0

        # by default, auto compute routing table is off
        self.auto=0

        self.interfaces.append({
            QtCore.QString("subnet"):QtCore.QString(""),
            QtCore.QString("mask"):QtCore.QString(""),
            QtCore.QString("ipv4"):QtCore.QString(""),
            QtCore.QString("mac"):QtCore.QString(""),
            QtCore.QString("routing"):[]})

        self.lightPoint = QPoint(-14,15)

    def generateToolTip(self):
        """
        Add subnet IP address to the tool tip for easier lookup.
        """
        tooltip = self.getName()
        interface = self.getInterface()
        tooltip += "\n\nSubnet: " + interface[QtCore.QString("subnet")] + "\n"
        tooltip += "IP: " + interface[QtCore.QString("ipv4")]          
        self.setToolTip(tooltip)

