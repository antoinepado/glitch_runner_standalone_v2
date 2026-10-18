# Changes

#### 1
op index bug in toroidal mirror is now fixed, no apparent change

#### 2
double crystal monochromator geometric change, respects the short channel cut now, this significantly improves the Ti simulation's curve trend

#### 3
filter_rock component in instrument file now has a larger height and width (0.5m), this significantly improves the Cu simulation's curve trend

#### 4
Mistake corrected in the single crystal component. 10E was written instead of 1E in abs_xsect. No change expected as this error cancelled out before, therefore no changes.

#### 5
Si.lau units fixed converted to barns now.

#### 6
Fixed weights of photons in the bending magnet. weight_i = Q(E_i, theta_i, psi_i)/(N\*E_i\*q_E(Ei)\*q_theta_psi(theta_i,psi_i))
where  
N is the number of photons  
q_E is the energy sampling compensation (or probability density)  
q_theta_psi is the angles sampling compensation  
E_i the energy of the photon  
Q is simply the Schwinger's equation without the relative bandwidth factor delta_E/E  

#### 7

New reflectivities created with the xraydb library. Takes into account the thickness of the coatings (Ir for M1 mirror or B4C,Pt,Pd for M2a and M2b mirrors) and the substrate (Si).

#### 8
New beamline alignment.
