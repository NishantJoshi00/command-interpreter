# Command Recognition with Python

This is an API built using python to recognize speech commands. It uses SpeechRecognition to convert speech to text, and then interprets the command according to the model.yml file that is provided.
## Building

To build this application you, require make to be installed in your system.
Start building the software using the command `make build`
This command will ask for superuser privilages, they are strictly for using the package manager.

## Issues

- This would only work on debian based system as the package manager specified if only for debian/ubuntu
- The Speech recoginzer model that is used is from google and thus the privilages for using it can be revoked anytime.

## Scaling

- Any different engine for recoginzation can be used, but must be specified while initialising the model, the \*\*kwargs that are passed to the function.
- You can specifiy a custom model for the command interpretation.
- Sample model is present in **model.yml**

