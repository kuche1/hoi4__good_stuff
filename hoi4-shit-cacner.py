#! /usr/bin/env python3

import os
import sys

dir_source = os.path.expanduser('~') + '/.steam/steam/steamapps/common/Hearts of Iron IV/history/states/'
dir_dest = os.path.expanduser('~') + '/.local/share/Paradox Interactive/Hearts of Iron IV/mod/disable_oceania/history/states/'
owner_old = 'owner = ' + sys.argv[1]
owner_new = 'owner ='

for dir_, fols, fils in os.walk(dir_source):
    for fil in fils:
        with open(dir_source+fil) as f:
            cont = f.read()
            if owner_old in cont:
                print('yes')
                cont = cont.replace(owner_old, owner_new)
                with open(dir_dest+fil, 'w') as f:
                    f.write(cont)
    break
