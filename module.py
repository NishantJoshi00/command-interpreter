import speech_recognition as sr
import sys
from datetime import datetime
import os
class Module:
    def __init__(self, sf=sr.Recognizer.recognize_google, **kwargs):
        self._recognizer = sr.Recognizer()
        self._logging("Recognizer module started", 1)
        self._microphone = sr.Microphone()
        self._logging("Microphone module detected/started", 1)
        self._tokens = kwargs
        self._engine = sf
        self._command_set = None
        self._cpfilename = 'model.yml'
    @property
    def filename(self):
        return self._cpfilename
    
    @filename.setter
    def filename(self, value):
        self._cpfilename = self._secure_filename(value)
    def _speech_to_text(self):
        with self._microphone as src:
            self._recognizer.adjust_for_ambient_noise(src)
            _audio = self._recognizer.listen(src)
        data = {
            "status_code": 0,
            "error": None,
            "text": None
        }
        try:
            data['text'] = self._engine(self._recognizer, _audio)
        except sr.RequestError:
            data['status_code'] = -1
            data['error'] = "API unavailable"
        except sr.UnknownValueError:
            data['status_code'] = 1
            data['error'] = "Unable to recognize speech"
        return data
    
    def _secure_filename(self, filename):
        if filename.startswith("/") or filename.startswith("~"):
            return filename
        else:
            return '/'.join(sys.argv[0].split("/")[:-1]) + '/' + filename
    def _yaml_interpreter(self, filename):
        with open(filename, "r") as f:
            from yaml import load, SafeLoader
            self._command_set = load(f, Loader=SafeLoader)
        return 0
    def _interpreter(self, command):
        if self._command_set == None:
            self._yaml_interpreter(self._cpfilename)
        command = command.split()
        action = self._command_set
        for i in command:
            if type(action) != dict:
                break
            if i not in action:
                raise NotImplementedError("The command not implemented")
            action = action[i]
        eval(action)

    def exec(self):
        data = self._speech_to_text()
        self._logging("Executing {} as {}".format(data['text'], data['status_code']), 1)
        if data['status_code'] != 0:
            raise EOFError("No text supplied")
        self._interpreter(data['text'])
    def _logging(self, msg, level):
        if level == 0:
            sys.stdout.write('{}\n'.format(msg))
        if level == 1:
            sys.stderr.write("[{}]: {}\n".format(datetime.now().isoformat(), msg))

if __name__ == "__main__":
    model = Module()
    model.exec()
