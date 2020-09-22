#!/usr/local/bin/python3
import math

xA=8
xB=10
xC=12
yA=9
yB=6
yC=10

dxAB=xA-xB
dyAB=yA-yB
dxAC=xA-xC
dyAC=yA-yC
dxBC=xB-xC
dyBC=yB-yC

dAB=math.sqrt(dxAB**2+dyAB**2)
dAC=math.sqrt(dxAC**2+dyAC**2)
dBC=math.sqrt(dxBC**2+dyBC**2)

d2AB=dAB**2
d2AC=dAC**2
d2BC=dBC**2

Alpha= math.acos((d2AC+d2BC-d2AB)/(2*dAC*dBC));
Beta= math.acos((d2AB+d2BC-d2AC)/(2*dAB*dBC));
Gamma= math.acos((d2AB+d2AC-d2BC)/(2*dAB*dAC));

Alpha= Alpha*180/math.pi;
Beta= Beta*180/math.pi;
Gamma= Gamma*180/math.pi;

print(Alpha)
print(Beta)
print(Gamma)






