import logging
import apie

class id(apie.Endpoint):
    def __init__(this, name="Hardware Identification"):
        super().__init__(name)

        this.supportedMethods = ['GET']
        this.cacheable = True

        this.requiredKWArgs.append('os')
        this.requiredKWArgs.append('machine')
        this.requiredKWArgs.append('arch')
        this.requiredKWArgs.append('processor')
        this.requiredKWArgs.append('version')

        this.optionalKWArgs['hostname'] = 'localhost'

    # Required Endpoint method. See that class for details.
    def GetHelpText(this):
        return '''\
Get a unique identifier for the given hardware.
'''

    def Call(this):
        numericIdSegments = {
            'os': 0,
            'machine': 0,
            'arch': 0,
            'processor': 0,
            'version': 0,
            'hostname': 0
        }
        #TODO...
        this.response.code = 200
        this.response.content.data = numericIdSegments
