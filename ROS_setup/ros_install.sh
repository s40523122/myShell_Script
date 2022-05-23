# Read the distro of ROS
echo " ======================"
echo " = System requirement ="
echo " ======================"
echo -e " ROS_distro" "\t" ubuntu_release
echo -e " kinetic" "\t" 16.04
echo -e " melodic" "\t" 18.04
echo -e " noetic" "\t" 20.04
echo ""

until [[ ${distro} =~ ^(kinetic|melodic|noetic)$ ]]
do
   if [[ -n ${distro} ]]
   then
      echo ""
      echo -e "\e[1;31m Can't find the distro ! \e[0m"
   fi
   read -p " Please input the ROS distro : " distro
done

# Setup sources.list
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

# Set up keys
sudo apt install -y curl
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# Installation
sudo apt update
sudo apt install -y ros-${distro}-desktop-full

# Environment setup
echo "source /opt/ros/${distro}/setup.bash" >> ~/.bashrc
echo "export ROS_MASTER_URI=http://localhost:11311" >> ~/.bashrc
echo "export ROS_IP=localhost" >> ~/.bashrc
source ~/.bashrc

# Dependencies for building packages
if [ "${distro}" = "noetic" ]
then
    sudo apt install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential python3-rosdep

else
    sudo apt install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential python-rosdep

fi

sudo rosdep init
rosdep update
