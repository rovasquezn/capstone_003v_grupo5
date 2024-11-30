#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
from .models import DjLogAdmin

'''	
	Set error in the model log
'''
def set_error_to_log(request, content):

	try:
		now = datetime.datetime.now()
		username = request.user.username

		log = DjLogAdmin(date=now, username=username,
						content=content)

	except Exception:
		log = DjLogAdmin(date=now, content=content)

	log.save()

'''
	Return error based on a filter
'''

def get_data_log(filter, value):

	try:
		if isinstance(filter, basestring):
			if filter.lower().strip() == "date":
				log = DjLogAdmin.objects.filter(date=value)
			elif filter.lower().strip() == 'username':
				log = DjLogAdmin.objects.filter(username=value)
			else:
				return None
		else:
			return None

		return log
	except Exception:
		return None






	

