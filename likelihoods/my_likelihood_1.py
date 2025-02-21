import numpy as np
from cobaya import Likelihood

class MyLikelihood(Likelihood):
    params = {
        "sigma": 0.1,  # Nuisance parameter
    }

    def initialize(self):
        # Load your data here
        self.data = ...

    def get_requirements(self):
        # Request quantities computed by theories (e.g., "H_z")
        return {"H_z": {"z": [0, 1, 2]}}  # Request H(z) at specific redshifts

    def logp(self, **params_values):
        H_z = self.provider.get_H_z()
        # Compare to data and compute log-likelihood
        return -0.5 * np.sum((H_z - self.data)**2 / self.sigma**2)