#!/usr/bin python3
import os
import sys
import time

time_exec = int(sys.argv[1])

my_dir = os.path.dirname(sys.argv[0])
os.system('%s %s' % (sys.executable, 
                        os.path.join(my_dir, f'packets_analyze.py {time_exec} > rapport.txt')))

os.system('mail -s "Rapport d analyse des paquets" -A rapport.txt postmaster@projet-reseau.sn < rapport.txt' )



