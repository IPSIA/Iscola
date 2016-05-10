sudo apt-get update
sudo apt-get install python-matplotlib

mkdir git_repo
cd git_repo/

git config --global user.email "pi@raspberry.com"
git config --global user.name "Raspberry PI"

git clone https://github.com/theiera/Iscola_IPSIA_Connect-IT.git
cd Iscola_IPSIA_Connect-IT/

mkdir basics
cd basics
