sudo apt upgrade -y

# Setup Sources
sudo apt update 
sudo apt install -y curl gnupg2 lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Installation
sudo apt update
sudo apt install -y ros-foxy-ros-base

# Environment setup
echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
source ~/.bashrc

# Dependencies for building packages
