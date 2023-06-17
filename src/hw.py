import logging
import apie

class hw(apie.Endpoint):
    def __init__(this, name="Hardware Synchronization Endpoint"):
        super().__init__(name)

        this.supportedMethods = [] #All

    # Required Endpoint method. See that class for details.
    def GetHelpText(this):
        return '''\
H A R D W A R E
'''

    def Call(this):
        this.response.code = 200
        this.response.content.string = "OK"
