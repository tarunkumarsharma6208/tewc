from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.contrib.humanize.templatetags.humanize import naturaltime as django_naturaltime
from django.conf import settings
from django.apps import apps
from django_middleware_global_request.middleware import get_request
from django.utils import timezone
from store.models import *


def naturaltime(value):
	return django_naturaltime(value)

def convert_to_list(value):
	if value:
		return list(map(int, value.split(',')))
	else:
		return []

def naturaldateyear(value):
	try:
		return value.strftime("%d %b %Y")
	except:
		return "_"

def datetimelist(value):
	print(value.time().strftime("%H:%M"))
	data = [value.strftime("%d %b %Y"),value.time().strftime("%I:%M:%p")]
	return data

def htmldate(value):
	try:
		return value.strftime("%Y-%m-%d")
	except:
		return value

def time_m(value):
	time = timezone.localtime(value)
	data = time.time().strftime("%I:%M:%p")
	return data

def get_base_url():
	try:
		request = get_request()
		return request.META['HTTP_HOST']
	except Exception as e:
		print(e)
		return settings.BASE_URL
	
def global_context():
	d = {}
	d['category_all'] = Category.objects.all()
	print(Category.objects.all())
	return d


def environment(**options):
	env = Environment(**options)
	env.globals.update({
		'static': staticfiles_storage.url,
		'url'	: reverse,
		'get_base_url': get_base_url,
		'filter': getter_multiple_obj,
		'global_context': global_context
	})
	
	env.filters['naturaltime'] = naturaltime	
	env.filters['convert_to_list'] = convert_to_list	
	env.filters['naturaldateyear'] = naturaldateyear	
	env.filters['datetimelist'] = datetimelist	
	env.filters['time_m'] = time_m	
	env.filters['htmldate'] = htmldate
	return env	

def getter_multiple_obj(app_name, model_name, **kwargs):
	__class = apps.get_model(app_label=app_name, model_name=model_name)
	return __class.objects.filter(**kwargs)

