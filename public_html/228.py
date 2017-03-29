# -*- coding: utf-8 -*-
#print ("Ievadi trīsstūra leņķi alfa!\n")
#a=input("Ievadi trīsstūra leņķi alfa!\n")
from math import sin, pi, sqrt
while True:
     result = input("Ievadi trīsstūra leņķi alfa robežās no 1-89:\n")
     if 1 <= int(result) <= 89:
         print "Leņķis ir %d grādi" %result
         d= int(result)*pi/180
         print "Leņķis ir %f radiāni" %d
         break;
     print "Netrāpīji robežās, mēģini vēlreiz!"
#print "Leņķis ir %d grādi" %a
# kat=pretkatete
kat=(sin(d))*400
#b=sin(d)
print 'Pretkatete ir %.f vienības gara' %kat
#pitagora      piekat= piekatete 
piekat=sqrt(400*400-kat*kat)
print "Piekatete ir %.f vienības gara" %piekat
print "Hipotenūza ir 400 vienības gara"

#print ('<svg width="150%" height="150%" version="1.1" xmlns="http://www.w3.org/2000/svg"><svg height="700" width="700"><polygon points="0,%f %f,%f %f,0"  style="fill:lime;stroke:purple;stroke-width:1" /></svg>') %(kat,piekat,kat,piekat)
#f=open(228.svg,'w')
#print >> f, '228.svg'
import sys
sys.stdout=open("228.svg","w")
print ('<svg width="500" height="500" version="1.1" xmlns="http://www.w3.org/2000/svg"><polygon points="0,%f %f,%f %f,0"  style="fill:lime;stroke:purple;stroke-width:1" /><text x="20" y="50" fill="#000000">%.f grādi</text></svg>') %(kat,piekat,kat,piekat,result)
sys.stdout.close()

#<svg width="150%" height="150%" version="1.1"
#xmlns="http://www.w3.org/2000/svg">



#<text x="20" y="50" fill="#FFF000">
#Taisnsturis Rolands</text>
#</svg>
