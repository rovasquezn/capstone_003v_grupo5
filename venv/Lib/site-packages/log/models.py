from django.db import models

'''
	Model containing the records
	with errors captured
'''
class DjLogAdmin(models.Model):

	date = models.DateField(null=False)
	username = models.CharField(null=True, blank=True, max_length=50)
	content = models.TextField(null=False, blank=False)

	def __unicode__(self):
		return '%s error: %s' % (self.username, self.content)