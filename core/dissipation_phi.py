import psutil

def measure_phi_d():

    cpu = psutil.cpu_percent()

    return cpu / 100


class DissipationRegulator:

    def __init__(self):

        self.low_power = False

    def update(self, phi_m, phi_c):

        phi_d = measure_phi_d()

        if phi_d + phi_m > phi_c:

            self.low_power = True

        else:

            self.low_power = False

        return self.low_power


regulator = DissipationRegulator()
