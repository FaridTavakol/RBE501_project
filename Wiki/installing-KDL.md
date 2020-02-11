```
git clone https://github.com/orocos/orocos_kinematics_dynamics.git
cd orocos_kinematics_dynamics/orocos_kdl; mkdir build; cd build
cmake ..
make -j$(nproc)  # compile
sudo make install; sudo ldconfig; cd  # install and go home
```