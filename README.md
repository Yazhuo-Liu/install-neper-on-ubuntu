# Installing Gmsh and Neper on Ubuntu (Build from Source)

## Install Gmsh

### 1. Install Prerequisites
```bash
sudo apt update
sudo apt install -y git cmake g++ make libglu1-mesa-dev libxmu-dev libxi-dev \
libfreetype6-dev libpng-dev zlib1g-dev libtiff5-dev libjpeg-dev \
libjsoncpp-dev libxml2-dev
```

### 2. Download the Source Code
```bash
git clone https://gitlab.onelab.info/gmsh/gmsh.git
cd gmsh
```

### 3. Build the Source Code
```bash
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)  # Replace $(nproc) with the number of CPU cores if needed
```

### 4. Find the gmsh binary file
```bash
ls gmsh
```

### 5. Verify Installation
```bash
./gmsh -version
```

### 6. Copy the binary file to `/usr/local/bin`
```bash
sudo cp gmsh /usr/local/bin/
```

## Install Neper
### 1. Install Prerequisites
```bash
sudo apt update
sudo apt install -y git cmake g++ make libgsl-dev libboost-all-dev libopenmpi-dev libfftw3-dev libhdf5-dev \
libx11-dev libpng-dev libfreetype6-dev libgl1-mesa-dev libglu1-mesa-dev povray asymptote
```

### 2. Download the Neper Source Code
```bash
git clone https://github.com/neperfepx/neper.git
cd neper
```

### 3. Configure the Build
```bash
cd src
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
```

### 4. Build Neper
```bash
make -j$(nproc)  # Replace $(nproc) with the number of CPU cores if needed
```

### 4. Find the gmsh binary file
```bash
ls neper
```

### 5. Verify Installation
```bash
./neper -V
```

### 6. Copy the binary file to `/usr/local/bin`
```bash
sudo cp neper /usr/local/bin/
```

## Test Neper
```bash
cd ~
mkdir testNeper
cd testNeper
```
use the command on Neper offical website
```bash
neper -T -n 100
neper -V n100-id1.tess -print img1
neper -T -n 100 -id 2
neper -V n100-id2.tess -print img1b
neper -M n100-id1.tess
neper -V n100-id1.tess,n100-id1.msh -print img2
neper -V n100-id1.tess,n100-id1.msh -showelt1d all -dataelt1drad 0.005 -print img3
```
If all success, you finished.

## Example of using Neper in python
Create a new python file named `generateMesh.py`, write down the following code:
```python
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
```
To run this file, using 
```
python3 generateMesh.py
```

## Code for assigning materials for neper mesh in abaqus
The code is upload [here](/assignMaterials.py)



