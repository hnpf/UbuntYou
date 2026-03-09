#!/bin/bash

set -e
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' 

echo -e "${BLUE}Starting ubuntyou installation...${NC}"
# 1. check for Python 3
if ! command -v python3 &> /dev/null; then
    echo -e "${BLUE}Python 3 not found. Installing...${NC}"
    sudo apt update
    sudo apt install -y python3
else
    echo -e "${GREEN}✓ Python 3 is already installed!${NC}"
fi

# 2. check for pip3
if ! command -v pip3 &> /dev/null; then
    echo -e "${BLUE}pip3 not found. Installing...${NC}"
    sudo apt update
    sudo apt install -y python3-pip
else
    echo -e "${GREEN}✓ pip3 is already installed!${NC}"
fi

# 3. install Python deps
echo -e "${BLUE}Installing Python dependencies...${NC}"
sudo pip3 install -r requirements.txt --break-system-packages || sudo pip3 install -r requirements.txt

# 4. make a symlink for easy access
echo -e "${BLUE}Creating symlink to /usr/local/bin/ubuntyou...${NC}"
cat <<EOF | sudo tee /usr/local/bin/ubuntyou > /dev/null
#!/bin/bash
sudo python3 -m ubuntyou.cli "\$@"
EOF
sudo chmod +x /usr/local/bin/ubuntyou

# 5. make the project directory accessible for the module imports
# well use the current directory as the source for the python module
INSTALL_DIR=$(pwd)
export PYTHONPATH=\$PYTHONPATH:\$INSTALL_DIR
echo -e "${GREEN}Successfully installed ubuntyou!${NC}"
echo -e "You can now run it using: ${BLUE}sudo ubuntyou list${NC}"
echo -e "Or to apply everything: ${BLUE}sudo ubuntyou apply --all${NC}"
