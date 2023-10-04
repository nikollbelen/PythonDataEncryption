from googletrans import Translator

translator = Translator()
translated = translator.translate(
    "El misterio de la vida no es un problema a resolver, sino una realidad a experimentar",
    src = "es",
    dest = "en",
)
print(translated.text)