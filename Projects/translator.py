# pip install googletrans==3.1.0a0

from googletrans import Translator
translator = Translator()

out = translator.translate("Hola amigo", dest='en')
print(out)

out = translator.translate("I am learning python", dest='es')
print(out)
