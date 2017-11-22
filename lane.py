class lane:

    # Initialize lane.
    #
    # scp - starting car position
    # sip - starting intersection position
    # eip - ending intersection position
    # ecp - ending car position
    def __init__(self, scp, sip, eip, ecp):
        self.scp = scp
        self.sip = sip
        self.eip = eip
        self.ecp = ecp
