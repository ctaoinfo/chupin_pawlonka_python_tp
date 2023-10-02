from verbecc import Conjugator
from verbecc.exceptions import ConjugatorError

class ConjugationOfVerbs:
	def __init__(self):
		self.cg = Conjugator(lang='fr')

	def conjugate(self, verb):
		try:
			conjugation = self.cg.conjugate(verb)
			for category, sub_dict in conjugation['moods'].items():
				print(category)
				for tense, conjs in sub_dict.items():
					print(tense, ":", conjs)
		except ConjugatorError:
			print("Invalid infinitive verb")



