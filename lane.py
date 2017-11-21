class lane:

    # Initialize lane.
    #
    # scp - starting car position
    # scv - starting car velocity
    # sip - starting intersection position
    # eip - ending intersection position
    # ecp - ending car position
    def __init__(self, scp, scv, sip, eip, ecp):
        self.scp = scp
        self.scv = scv
        self.sip = sip
        self.eip = eip
        self.ecp = ecp
