import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

Authenticator = IAMAuthenticator(APIKEY)
Language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=Authenticator
)

Language_translator.set_service_url(URL)

def englishToFrench(englishText):
    if englishText is '':
        frenchText = ''
    else:
        translation = Language_translator.translate(
            text=englishText,
            model_id='en-fr').get_result()
        frenchText = translation['translations'][0]['translation']   
    
    return frenchText

def frenchToEnglish(frenchText):
    if frenchText is '':
        englishText = ''
    else:
        translation = Language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()
        englishText = translation['translations'][0]['translation']   
    
    return englishText