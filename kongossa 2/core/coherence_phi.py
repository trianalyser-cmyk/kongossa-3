class CoherenceMeter:

    def __init__(self):

        self.total = 0
        self.useful = 0

    def record(self, useful=True):

        self.total += 1

        if useful:
            self.useful += 1

    def phi(self):

        if self.total == 0:
            return 1

        return self.useful / self.total


coherence = CoherenceMeter()
