from django.test import TestCase
from cryptography.fernet import Fernet

# Create your tests here.
encMessage="b'gAAAAABjA9VKmwYqaj_tPfLboD-ER7RUrbGi3eHghMLWoGOfw7HZy-nq_garFyCH0w3vkukruJiSJSqqdr-oW2DZHVBl3uBgVQ=='"
# key='h61CM9wQHMIAgy6uuiZ26y5TrKJGsUwVW-2RGPm944Q='
# fernet = Fernet(key)
# decMessage = fernet.decrypt(encMessage
# ).decode()
# print(decMessage)

# arr = bytes(encMessage, 'utf-8')
# print(type(arr))

stroke=encMessage[1:len(encMessage)].replace("'", "")
print(stroke)
 