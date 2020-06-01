

build:
	sudo apt install python3-pyaudio portaudio19-dev libportaudio2 libportaudiocpp0
	pip3 install virtualenv
	virtualenv venv
	venv/bin/pip3 install -r requirements.txt
	
