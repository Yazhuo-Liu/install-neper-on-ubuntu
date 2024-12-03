#!/usr/bin/env python3

import os
import glob

domain_x = 1.0
domain_y = 1.0
domain_z = 0.2

num_grains = 100
mesh_size = 0.5
mesh_type = 'hex'
mesh_order = 1
id = 0
neper_dir = os.path.join(os.path.dirname(__file__),'data')

files = glob.glob(os.path.join(neper_dir, f'*'))
for f in files:
    os.remove(f)


os.system(f'''neper -T -n {num_grains} -id {id} -regularization 0 -domain "cube({domain_x},\
                {domain_y},{domain_z})" \
                -o {neper_dir}/domain -format tess,obj,ori''')
os.system(f"neper -T -loadtess {neper_dir}/domain.tess -statcell x,y,z,vol,facelist -statface x,y,z,area")

## hax mesh
os.system(f"neper -M -rcl {mesh_size} -elttype {mesh_type} -order {mesh_order} -faset faces {neper_dir}/domain.tess -o {neper_dir}/domain.msh")
os.system(f"neper -M -rcl {mesh_size} -elttype {mesh_type} -order {mesh_order} -faset faces {neper_dir}/domain.tess -format inp -o {neper_dir}/domain")
# os.system(f'neper -M {neper_dir}/domain.msh -format inp -o {neper_dir}/domain.inp')
os.system(f"neper -V {neper_dir}/domain.tess,{neper_dir}/domain.msh -print {neper_dir}/domain")


# tet mesh
os.system(f"neper -M -rcl {mesh_size} -order {mesh_order} -faset faces {neper_dir}/domain.tess -o {neper_dir}/domain2.msh")
os.system(f"neper -M -rcl {mesh_size} -order {mesh_order} -faset faces {neper_dir}/domain.tess -format inp -o {neper_dir}/domain2")
# os.system(f'neper -M {neper_dir}/domain.msh -format inp -o {neper_dir}/domain.inp')
os.system(f"neper -V {neper_dir}/domain.tess,{neper_dir}/domain2.msh -print {neper_dir}/domain2")

os.system(f"mv data/domain.inp g{num_grains}hax0.inp")
os.system(f"mv data/domain2.inp g{num_grains}tet1.inp")
os.system(f"mv data/domain2.png g{num_grains}hax1.png")
os.system(f"mv data/domain.png g{num_grains}tet0.png")
