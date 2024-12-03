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
```
git clone https://gitlab.onelab.info/gmsh/gmsh.git
cd gmsh
```

### 3. Build the Source Code
```
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)  # Replace $(nproc) with the number of CPU cores if needed
```

### 4. Find the gmsh binary file
```
ls gmsh
```

### 5. Verify Installation
./gmsh -version

### 6. Copy the binary file to `/usr/local/bin`
```
sudo cp gmsh /usr/local/bin/
```

## Install Neper
### 1. Install Prerequisites
```
sudo apt update
sudo apt install -y git cmake g++ make libgsl-dev libboost-all-dev libopenmpi-dev libfftw3-dev libhdf5-dev \
libx11-dev libpng-dev libfreetype6-dev libgl1-mesa-dev libglu1-mesa-dev povray asymptote
```

### 2. Download the Neper Source Code
```
git clone https://github.com/neperfepx/neper.git
cd neper
```

### 3. Configure the Build
```
cd src
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
```

### 4. Build Neper
```
make -j$(nproc)  # Replace $(nproc) with the number of CPU cores if needed
```

### 4. Find the gmsh binary file
```
ls neper
```

### 5. Verify Installation
./neper -V

### 6. Copy the binary file to `/usr/local/bin`
```
sudo cp neper /usr/local/bin/
```

## Test Neper
```
cd ~
mkdir testNeper
cd testNeper
```
use the command on Neper offical website
```
neper -T -n 100
neper -V n100-id1.tess -print img1
neper -T -n 100 -id 2
neper -V n100-id2.tess -print img1b
neper -M n100-id1.tess
neper -V n100-id1.tess,n100-id1.msh -print img2
neper -V n100-id1.tess,n100-id1.msh -showelt1d all -dataelt1drad 0.005 -print img3
```
If all success, you finished.



