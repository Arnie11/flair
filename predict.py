from flair.data import Sentence
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger.load("ner")

sentence: Sentence = Sentence("George Washington went to Washington .")
tagger.predict(sentence)

Konfliktlösung:
Vom Master war(HEAD)
print("Analysing sentence %s“ % sentence)

Vom feature branch war:
print("Analysing the sentence %s" % sentence)


unverändert war:
print("\nThe following NER tags are found: \n")
print(sentence.to_tagged_string())
