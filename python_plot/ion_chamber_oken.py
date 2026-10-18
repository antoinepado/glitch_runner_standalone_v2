import math as m
import numpy as np
import matplotlib.pyplot as plt

#mass absorption coefficient (cm^2/g), N2
#https://physics.nist.gov/PhysRefData/FFast/form.html
def N2(energy):
    #these values are in cm^2/g
    t = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    t[0]  =  2649.6
    t[1]  =  2204.7
    t[2]  =  1832.3
    t[3]  =  1521.2
    t[4]  =  1261.9
    t[5]  =  1046.1
    t[6]  =  866.68
    t[7]  =  714.38
    t[8]  =  588.46
    t[9]  =  484.73
    t[10] =  399.29
    t[11] =  328.92
    t[12] =  270.95
    t[13] =  223.20
    t[14] =  183.87
    t[15] =  151.47
    t[16] =  124.13
    t[17] =  101.23
    t[18] =  82.553
    t[19] =  67.324
    t[20] =  54.905
    t[21] =  44.776
    t[22] =  36.516
    t[23] =  29.780
    t[24] =  24.287
    t[25] =  19.807
    t[26] =  16.153
    t[27] =  13.174
    t[28] =  10.744
    t[29] =  8.7620
    t[30] =  7.1183
    t[31] =  5.7735
    t[32] =  4.6775
    t[33] =  3.7741
    t[34] =  3.0452
    t[35] =  2.4571
    t[36] =  1.9825
    t[37] =  1.5995
    t[38] =  1.2905
    t[39] =  1.0411
    t[40] =  0.83998
    t[41] =  0.67769
    t[42] =  0.54676
    t[43] =  0.44112
    t[44] =  0.35589
    t[45] =  0.28713
    t[46] =  0.23166
    t[47] =  0.18690
    t[48] =  0.15079
    t[49] =  0.12120
    t[50] =  9.7291e-2
    t[51] =  7.8100e-2
    t[52] =  6.2695e-2
    t[53] =  5.0328e-2
    t[54] =  4.0401e-2
    t[55] =  3.2432e-2
    t[56] =  2.6035e-2 
    
    e = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    e[0]  =  1.0677
    e[1]  =  1.1413
    e[2]  =  1.2201
    e[3]  =  1.3043
    e[4]  =  1.3943
    e[5]  =  1.4905
    e[6]  =  1.5933
    e[7]  =  1.7033
    e[8]  =  1.8208
    e[9]  =  1.9464
    e[10] =  2.0807
    e[11] =  2.2243
    e[12] =  2.3778
    e[13] =  2.5418
    e[14] =  2.7172
    e[15] =  2.9047
    e[16] =  3.1052
    e[17] =  3.3194
    e[18] =  3.5484
    e[19] =  3.7933
    e[20] =  4.0550
    e[21] =  4.3348
    e[22] =  4.6339
    e[23] =  4.9537
    e[24] =  5.2955
    e[25] =  5.6609
    e[26] =  6.0515
    e[27] =  6.4690
    e[28] =  6.9154
    e[29] =  7.3925
    e[30] =  7.9026
    e[31] =  8.4479
    e[32] =  9.0308
    e[33] =  9.6539
    e[34] =  10.320
    e[35] =  11.032
    e[36] =  11.793
    e[37] =  12.607
    e[38] =  13.477
    e[39] =  14.407
    e[40] =  15.401
    e[41] =  16.464
    e[42] =  17.600
    e[43] =  18.814
    e[44] =  20.112
    e[45] =  21.500
    e[46] =  22.983
    e[47] =  24.569
    e[48] =  26.265
    e[49] =  28.077
    e[50] =  30.014
    e[51] =  32.085
    e[52] =  34.299
    e[53] =  36.666
    e[54] =  39.195
    e[55] =  41.900
    e[56] =  44.791
    
    counter = 0
    for i,elt in enumerate(e):
        if(energy>=e[i] and energy<=e[i+1]):
            counter=i
            break
            
    v = ((energy-e[counter])*t[counter+1]+(e[counter+1]-energy)*t[counter])/(e[counter+1]-e[counter])

    return v

def He(energy):
    #these values are in cm^2/g
    t = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    t[0]  =  52.183
    t[1]  =  41.838
    t[2]  =  33.514
    t[3]  =  26.823
    t[4]  =  21.449
    t[5]  =  17.137
    t[6]  =  13.682
    t[7]  =  10.914
    t[8]  =  8.7002
    t[9]  =  6.9302
    t[10] =  5.5165
    t[11] =  4.3882
    t[12] =  3.4884
    t[13] =  2.7714
    t[14] =  2.2005
    t[15] =  1.7461
    t[16] =  1.3849
    t[17] =  1.0978
    t[18] =  0.86978
    t[19] =  0.68881
    t[20] =  0.54525
    t[21] =  0.43144
    t[22] =  0.34124
    t[23] =  0.26981
    t[24] =  0.21326
    t[25] =  0.16850
    t[26] =  0.13311
    t[27] =  0.10512
    t[28] =  8.2993e-2
    t[29] =  6.5512e-2
    t[30] =  5.1704e-2
    t[31] =  4.0799e-2
    t[32] =  3.2190e-2
    t[33] =  2.5395e-2
    t[34] =  2.0033e-2
    t[35] =  1.5802e-2
    t[36] =  1.2465e-2
    t[37] =  9.8319e-3
    t[38] =  7.7554e-3
    t[39] =  6.1177e-3
    t[40] =  4.8263e-3
    t[41] =  3.8078e-3
    t[42] =  3.0047e-3
    t[43] =  2.3713e-3
    t[44] =  1.8717e-3
    t[45] =  1.4777e-3
    t[46] =  1.1669e-3
    t[47] =  9.2172e-4
    t[48] =  7.2825e-4
    t[49] =  5.7557e-4
    t[50] =  4.5505e-4
    t[51] =  3.5989e-4
    t[52] =  2.8474e-4
    t[53] =  2.2538e-4
    t[54] =  1.7847e-4
    t[55] =  1.4138e-4
    
    e = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    e[0]  =  1.0677
    e[1]  =  1.1413
    e[2]  =  1.2201
    e[3]  =  1.3043
    e[4]  =  1.3943
    e[5]  =  1.4905
    e[6]  =  1.5933
    e[7]  =  1.7033
    e[8]  =  1.8208
    e[9]  =  1.9464
    e[10] =  2.0807
    e[11] =  2.2243
    e[12] =  2.3778
    e[13] =  2.5418
    e[14] =  2.7172
    e[15] =  2.9047
    e[16] =  3.1052
    e[17] =  3.3194
    e[18] =  3.5484
    e[19] =  3.7933
    e[20] =  4.0550
    e[21] =  4.3348
    e[22] =  4.6339
    e[23] =  4.9537
    e[24] =  5.2955
    e[25] =  5.6609
    e[26] =  6.0515
    e[27] =  6.4690
    e[28] =  6.9154
    e[29] =  7.3925
    e[30] =  7.9026
    e[31] =  8.4479
    e[32] =  9.0308
    e[33] =  9.6539
    e[34] =  10.320
    e[35] =  11.032
    e[36] =  11.793
    e[37] =  12.607
    e[38] =  13.477
    e[39] =  14.407
    e[40] =  15.401
    e[41] =  16.464
    e[42] =  17.600
    e[43] =  18.814
    e[44] =  20.112
    e[45] =  21.500
    e[46] =  22.983
    e[47] =  24.569
    e[48] =  26.265
    e[49] =  28.077
    e[50] =  30.014
    e[51] =  32.085
    e[52] =  34.299
    e[53] =  36.666
    e[54] =  39.195
    e[55] =  41.900
    
    counter = 0
    for i,elt in enumerate(e):
        if(energy>=e[i] and energy<=e[i+1]):
            counter=i
            break
            
    v = ((energy-e[counter])*t[counter+1]+(e[counter+1]-energy)*t[counter])/(e[counter+1]-e[counter])

    return v

###INPUT
rock_data_input = input("Enter the name of the ROCK data (1_Fe, 2_Fe, 3_Fe, CoNi, Cu, FeNi, Ni, NiCu, Ti): ")

compound_gaz = 0
if(rock_data_input=="1_Fe" or rock_data_input=="Ni" or rock_data_input=="Ti"): #He/N2 (0.9/0.1) compound
    compound_gaz=1

print(compound_gaz)

data_rock_filename = "rock_data_si_111_short" + "/" + rock_data_input + ".txt"

#experimental data
def ParseCounts(energy):
    ########### Get data from digitalized ROCK data.
    data_rock = np.loadtxt(data_rock_filename, encoding='utf-8-sig',delimiter="\t")        
    tm = []
    em = []
    
    for elt in data_rock:
        tm.append(elt[1])
        em.append(elt[0]/1000.0)
    
    counter = 0
    for i,elt in enumerate(em):
        if(energy>=em[i] and energy<=em[i+1]):
            counter=i
            break
            
    v = ((energy-em[counter])*tm[counter+1]+(em[counter+1]-energy)*tm[counter])/(em[counter+1]-em[counter])

    return v


gain=1E+6

########### Ask what to plot
print("Give the atom(s) name you want to plot. Here is the list:")
print("For Si 111 short crystals:")
print("Ti, NiCu, Ni, FeNi, Cu, CoNi, 1_Fe, 2_Fe, 3_Fe.")

########### Get data from digitalized ROCK data.
data_rock = np.loadtxt(data_rock_filename, encoding='utf-8-sig',delimiter="\t")
size_data_rock = len(data_rock)
X_rock = np.zeros(size_data_rock)
Y_rock = np.zeros(size_data_rock)


i=0
for elt in data_rock:    
    X_rock[i] = elt[0]
    Y_rock[i] = elt[1]
    i+=1

Y_flux_abs = []

#density calculated at 1 atm(101325 Pa) and 295 kelvin
for elt in data_rock:
    if (compound_gaz==0):
        energy_kev = elt[0]/1000.0
        muen = N2(energy_kev)
        counts_data = ParseCounts(energy_kev)
        a = 10*100*counts_data/(1.0E6)/gain
        length_chamber = 14.0#cm
        flux = a*35/(1.6E-19)/(energy_kev*1.0E3)
        flux = flux/(1-m.exp(-(muen*1.1573E-3*length_chamber)))
    elif (compound_gaz==1): 
        energy_kev = elt[0]/1000.0
        #values for He/N2 (90,10) compound now
        #He 0.9, N2 0.1 from the excel
        #molar mass g/mol M
        #0.9 * MHe / (0.9 * MHe + 0.1 * MN2)
        muen = 0.56254*He(energy_kev) + 0.43746*N2(energy_kev)
        counts_data = ParseCounts(energy_kev)
        a = 10*100*counts_data/(1.0E6)/gain
        length_chamber = 14.0#cm
        #leave a as 35 just a scalar ok
        flux = a*35/(1.6E-19)/(energy_kev*1.0E3)
        flux = flux/(1-m.exp(-(muen*0.2645E-3*length_chamber)))
        
    Y_flux_abs.append(flux)
    
norm = Y_flux_abs[0]    


########### For now only the data for the short cc has been done, we plot both McXtrace data and ROCK's data
###INPUT

mcxtrace_data_input = rock_data_input

data_mcxtrace_filename = "mcxtrace_data_si_111_short/mccode_" + rock_data_input + ".dat"

data_mcxtrace = np.loadtxt(data_mcxtrace_filename)

size_data_mcxtrace = len(data_mcxtrace)
X_mcxtrace = np.zeros(size_data_mcxtrace)
Y_mcxtrace = np.zeros(size_data_mcxtrace)
i=0
for elt in data_mcxtrace:
    X_mcxtrace[i] = elt[0]
    Y_mcxtrace[i] = elt[5] #I0
    i+=1


scl = Y_mcxtrace[0]
for i,elt in enumerate(Y_flux_abs):
    Y_flux_abs[i]=(Y_flux_abs[i]/norm)*scl
    print(i,elt)


#same start(xmin) and end(xmax) for both plots so the x axis aligns
x_min_rock = float(m.floor(X_rock[0]))
x_max_rock = float(m.floor(X_rock[-1]))
pos_x_min_rock, =  np.where(np.isclose(X_mcxtrace, x_min_rock)) 
pos_x_max_rock, = np.where(np.isclose(X_mcxtrace, x_max_rock)) 

plt.plot(X_mcxtrace[pos_x_min_rock[0]:pos_x_max_rock[0]+1], Y_mcxtrace[pos_x_min_rock[0]:pos_x_max_rock[0]+1], marker='.', markersize=4, color="b", label='McXtrace')
plt.legend(fontsize=10)

plot_title = "I0 McXtrace and ROCK data " + rock_data_input

plt.title(plot_title)


plt.xlabel("E")
plt.ylabel("I0")

print("McXtrace and ROCK data plotted.")

plt.plot(X_rock, Y_flux_abs, marker='.', markersize=4, color="r", label='Rock exp (flux)')
plt.legend(fontsize=10)

plt.show()