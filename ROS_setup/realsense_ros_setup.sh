# Select the name of the workspace
while true; do
    echo "Hello, please select the workspace first:"
    read -p "Name of the workspace: " ws_name

    # Check if the workspace exists.
    if [ -d "$ws_name" ]; then
        echo "Workspace '$ws_name' selected !"
        break  # if exist, break loop.
    else
        echo -e "\e[1;31m Workspace directory '$ws_name' does not exist. Please provide a valid directory name.  \e[0m"
    fi
done

cd $ws_name/src

# Setup RealSense™ SDK 2.0
sudo apt-get update
git clone https://github.com/IntelRealSense/librealsense.git
sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev at
cd librealsense/
touch CATKIN_IGNORE
./scripts/setup_udev_rules.sh
./scripts/patch-realsense-ubuntu-lts-hwe.sh -n
echo 'hid_sensor_custom' | sudo tee -a /etc/modules
mkdir build && cd build
cmake ../ -DBUILD_EXAMPLES=true
sudo make uninstall && make clean && make && sudo make install

# Setup RealSense ros
cd ../..
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/
git checkout `git tag | sort -V | grep -P "^2.\d+\.\d+" | tail -1`
cd ..
git clone https://github.com/pal-robotics/ddynamic_reconfigure.git
catkin_init_workspace
cd ..
catkin_make clean
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
catkin_make install
source ~/.bashrc

