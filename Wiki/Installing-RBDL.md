### Downloads, build and install
```
cd ~/Downloads
sudo rm -r rbdl
mkdir rbdl
cd rbdl
wget https://bitbucket.org/rbdl/rbdl/get/default.zip
unzip default.zip
cd rbdl-rbdl-*
mkdir build
cd build/
cmake -D CMAKE_BUILD_TYPE=Release -D RBDL_BUILD_ADDON_URDFREADER=ON -D RBDL_BUILD_PYTHON_WRAPPER=ON ../
make -j4
sudo make install
cd python/
sudo cp rbdl.so /usr/local/lib/python2.7/dist-packages
```

By default the python wrapper is installed in /usr/local/lib/python2.7/site-packages, you could add this path to envirments PYTHONPATH in .bashrc or add:
```
cd ~/Downloads/rbdl/rbdl-rbdl-*/build/python
sudo cp rbdl.so /usr/local/lib/python2.7/dist-packages
```
