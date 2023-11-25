#!/bin/sh
sudo apt update
sudo apt install foremost steghide stegseek imagemagick gedit -y
mkdir -p /home/kali/bin
cd /home/kali/bin
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
echo '#!/bin/zsh
java -jar /home/kali/bin/stegsolve.jar' | sudo tee /bin/stegsolve
sudo chmod +x /bin/stegsolve
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
wget http://downloads.volatilityfoundation.org/releases/2.6/volatility_2.6_lin64_standalone.zip -O volatility.zip
unzip volatility.zip
sudo ln -s /home/kali/bin/volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone /bin/volatility
