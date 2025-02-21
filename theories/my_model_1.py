from cobaya import Theory

class MyModel(Theory):
    # Define parameters your model accepts (e.g., Hubble constant, dark energy parameters)
    params = {
        "H0": 70,       # Default value
        "Omega_m": 0.3,
    }

    def initialize(self):
        # Initialize your model (e.g., load external code, set up arrays)
        pass

    def get_requirements(self):
        # Specify what other quantities your model needs (e.g., primordial power spectrum)
        return []

    def calculate(self, state, want_derived=True, **params_values):
        # Compute your model's predictions here
        # Example: Calculate H(z) or other observables
        state["H_z"] = ...  # Store results in `state`
        state["derived"] = {"Omega_lambda": 1 - self.Omega_m}  # Derived parameters

    def get_H_z(self, z):
        # Optional: Return Hubble parameter at redshift z
        return ...