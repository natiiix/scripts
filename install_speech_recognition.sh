set -e

sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip3 install --upgrade pip
sudo pip3 install SpeechRecognition
sudo apt install portaudio19-dev python-all-dev python3-all-dev
sudo pip3 install pyaudio
sudo pip3 install --upgrade pyaudio
