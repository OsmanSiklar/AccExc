def get_rigidity(momentum, charge):
   
    e_charge = 1.602176634e-19

    momentum_kgms = momentum * 1e6 * 1.602176634e-19 / 299792458

    rigidity = momentum_kgms / charge

    return rigidity

momentum = 3.5 
charge = 1.6e-19  

rigidity = get_rigidity(momentum, charge)
print(f"Magnetic Rigidity (Bρ): {rigidity} T·m")
