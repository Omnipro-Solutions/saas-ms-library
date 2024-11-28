import gettext
import threading


def set_language(language_code: str = "es", localedir: str = None, domain="messages"):
    translation = gettext.translation(domain, localedir, languages=[language_code])
    translation.install()
    global _
    _ = translation.gettext
    return _


class GlobalTranslator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(GlobalTranslator, cls).__new__(cls)
                    cls._instance.current_language = None
                    cls._instance.translator = lambda x: x
        return cls._instance

    def set_language(self, language_code, localedir):
        self.translator = set_language(language_code, localedir)
        self.current_language = language_code

    def gettext(self, message):
        return self.translator(message)


# Instantiate a global translator object
translator = GlobalTranslator()
