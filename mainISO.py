from thermopack.cubic import cubic
#eos = pcsaft('NC6,NC12') 
eos = cubic('CO2,C1', 'vdW') #c1 antes pr vdw ou srk


x = [0.2, 0.8]

# Calculate pressure, specific volume, specific entropy and specific enthalpy along the isotherm at 300 K
# from p = minimum_pressure to p = maximum_pressure. Compute at most nmax points.

p_iso_T, v_iso_T, s_iso_T, h_iso_T = eos.get_isotherm(350., x, minimum_pressure=1e5, maximum_pressure=1.5e7, nmax=100)


                                                   
print(p_iso_T, v_iso_T);

   
#for (int i=0; i<100; i++){
#print(p_iso_T[i] \n );}
#for ( int j=0; j<100; j++){
#print(v_iso_T[j]\n); }



#print(eos.nc);


