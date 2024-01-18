import gettext


def set_language(language_code="es", localedir: str = None, domain="messages"):
    translation = gettext.translation(domain, localedir, languages=[language_code])
    translation.install()
    global _
    _ = translation.gettext
    return _
