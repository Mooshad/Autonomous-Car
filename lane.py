class lane:

    # Initialize lane.
    #
    # scp - starting car position
    # sip - starting intersection position
    # eip - ending intersection position
    # ecp - ending car position
    # sd - direction object is heading before entering the intersection
    # ed - direction object is heading after leaving the intersection
    def __init__(self, scp, sip, eip, ecp, index):
        self.scp = scp
        self.sip = sip
        self.eip = eip
        self.ecp = ecp
        self.index = index
