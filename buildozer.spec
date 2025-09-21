[app]
# Título do app
title = PokerBot

# Nome do pacote
package.name = pokerbot
package.domain = org.sady

# Pasta de origem e tipos de arquivo
source.dir = .
source.include_exts = py,png,jpg

# Versão do app
version = 0.1

# Bibliotecas e dependências
requirements = python3,kivy,pytesseract,pillow,treys

# Orientação da tela
orientation = portrait

# Configurações Android
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = armeabi-v7a, arm64-v8a

# Permissões do Android
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, WRITE_EXTERNAL_STORAGE

# Outras configurações padrão
fullscreen = 0
presplash.filename = 
icon.filename = 
title_fontname = 
version.code = 1
version.regex = 
