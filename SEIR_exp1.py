# Outbreak Model
# dS(t)/dt=-β S(t)/N I(t)-αS(t)
# dL(t)/dt=β S(t)/N I(t)-γL(t)  +k(t)
# dI(t)/dt=γL(t)-δI(t)-k(t)
# dQ(t)/dt=δI(t)λ(t)Q(t)-η(t)Q(t)
# dR(t)/dt=λ(t)Q(t)
# dD(t)/dt=η(t)Q(t)

#initial value of susceptible people
S=190000000
#initial value of latent people
L=0
#initial value of infected people
I=2
#initial value of quarantined people
Q=0
#initial value of removed people
R=0
#initial value of dead people
D=0
#total population
N= S+L+I+Q+R+D
#parameters
#infection rate
β=1
#restriction rate (assumed 50%)
α=50/100
#latent rate
γ =1/3
#average quarantine rate
δ=1/14
#temperature
k =72
#recovery rate
λ=1/5
#mortality rate
η=.037

#initial time in days
t=0

FINAL_SLIQRD = open("SLIQRD.csv","w") # open file for writing
FINAL_SLIQRD.write("time, S,L, I, Q, R, D\n") # write headers to file

for i in range(0,100):
    FINAL_SLIQRD.write(str(t) + "," + str(S) + "," + str(L) + "," + str(I)  + "," + str(Q) + "," + str(R) + "," + str(D) + "\n")
    print(str(t) + "," + str(S) + "," + str(L) + "," + str(I) + "," + str(Q) + "," + str(R) +"," + str(D) + "\n")
    t = t + 1
    dS_dt= -β*(S/N)*I-(α*S)
    dL_dt= β*(S/N)*I-(γ*L) + k
    dI_dt=(γ*L)-(δ*I)-k
    dQ_dt=(δ*I*λ*Q)-(η*Q)
    dR_dt=λ*Q
    dD_dt=η*Q
    
    S=S+dS_dt
    L=L+dL_dt
    I=I+dI_dt
    Q=Q+dQ_dt
    R=R+dR_dt
    D=D+dD_dt
FINAL_SLIQRD.write(str(t) + "," + str(S) + "," + str(L) + "," + str(I) + "," + str(Q) + "," + str(R) + "," + str(D) + "\n")



FINAL_SLIQRD.close()