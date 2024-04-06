# Select the name of the workspace
while true; do
    echo "Hello, please select the workspace first:"
    read -p "Name of the workspace: " ws_name

    # Check if the workspace exists.
    if [ -d "$ws_name" ]; then
        echo "Workspace '$ws_name' selected."
        break  # if exist, break loop.
    else
        echo -e "\e[1;31m Workspace directory '$ws_name' does not exist. Please provide a valid directory name.  \e[0m"
    fi
done

