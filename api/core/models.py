from django.db import models

class Talk(models.Model):
	THEMES = [
		('Vue', 'Vue'),
		('Test', 'Test'),
		('A11y', 'A11y'),
		('Serverless', 'Serverless'),
		('How we work', 'How we work'),
		('Webpack', 'Webpack'),
		('Svelte', 'Svelte'),
		('Design', 'Design'),
		('Nuxt', 'Nuxt'),
		('WebAssembly', 'WebAssembly'),
		('Audio', 'Audio'),
		('Vue3', 'Vue3'),
		('Climate', 'Climate'),
		('Vuex', 'Vuex'),
		('Architecture', 'Architecture'),
		('GraphQL', 'GraphQL'),
	]

	theme = models.CharField(choices=THEMES, max_length=25)
	name  = models.CharField(max_length=75, default='a title of the talk')
	speaker  = models.CharField(max_length=50)
	summary = models.CharField(max_length=500, default='a summary of the talk')
	image = models.FileField()
	slides = models.URLField(null=True, blank=True)

	def __str__(self):
	 return "Talk for {}".format(self.name)
