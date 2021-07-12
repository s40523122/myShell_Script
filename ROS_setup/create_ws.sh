# Read the input name
echo Hello, please name the workspace first:
read -p 'Name of the workspace : ' ws_name

# Make workspace folder
mkdir -p ~/$ws_name/src
cd ~/$ws_name && catkin_make

# Environment setup
echo "source ~/$ws_name/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc