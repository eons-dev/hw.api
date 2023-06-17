import logging
import apie

class id(apie.Endpoint):
    def __init__(this, name="Hardware Identification"):
        super().__init__(name)

        this.supportedMethods = ['GET']
        this.mime = 'plain/text'
        this.clobberContent = False

        this.requiredKWArgs.append('os')
        this.requiredKWArgs.append('arch')
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
            'arch': 0,
            'version': 0,
            'hostname': 0
        }
        #TODO...
        this.response.code = 200
        this.response.content.string = "".join([str(s) for s in numericIdSegments.values()])