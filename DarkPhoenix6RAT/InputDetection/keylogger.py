from pynput import keyboard
import json


class MyException(Exception): pass


class KeyLogger(object):
    def __init__(self):
        self.nice_output = []
        self.simple_output = []

    @staticmethod
    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    @staticmethod
    def on_press_exc(key):
        if key == keyboard.Key.esc:
            raise MyException(key)
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_press_silent(self, key):
        try:
            self.nice_output.append('alphanumeric key {0} pressed'.format(
                key.char))
            self.simple_output.append()
        except AttributeError:
            self.nice_output.append('special key {0} pressed'.format(
                key))


    @staticmethod
    def on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    @staticmethod
    def monitor_keys():
        with keyboard.Listener(
                on_press=KeyLogger.on_press,
                on_release=KeyLogger.on_release) as listener:
            listener.join()

    @staticmethod
    def monitor_keys_esc():
        with keyboard.Listener(
                on_press=KeyLogger.on_press_exc,
                on_release=KeyLogger.on_release) as listener:
            try:
                listener.join()
            except MyException as e:
                print('{0} was pressed'.format(e.args[0]))

    def to_json(self):
        """ Converts all member data into a JSON string
        :return: JSON string
        """
        data = {
            "nice_output": self.nice_output,
            "simple_output": self.simple_output
        }
        return json.dumps(data)
