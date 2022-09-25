from django import template
from cryptography.fernet import Fernet

register = template.Library()
import pytz
from django.utils import timezone

@register.filter(name='utc_to_local')
def convert_to_localtime(utctime):
  fmt = '%d/%m/%Y %H:%M'
  utc = utctime.replace(tzinfo=pytz.UTC)
  localtz = utc.astimezone(timezone.get_current_timezone())
  return localtz.strftime(fmt)

@register.filter(name='utc_to_local_new')
def date_change(datetime):
    local_dt = timezone.localtime(datetime) if datetime is not None else None
    
    return local_dt
@register.filter(name='upper')
def upper(value):
  return value.upper()

@register.filter(name='passwordcopy')
def copypass(hash,key):
  encmessage=hash
  decryptkey=key
  fernet = Fernet(decryptkey)
  decMessage = fernet.decrypt(encmessage
  ).decode()
  return decMessage

@register.filter(name='removebyte')
def revbyte(encrypted_pas):
  stroke=encrypted_pas[1:len(encrypted_pas)].replace("'","")
  return stroke
  
  



# use it by addit 
# 1.>  {% load custom_tags %} in html 
# 2.> {{contact.name|upper}}