from nltk.corpus import wordnet
from nltk.metrics import edit_distance


class AntonymReplacer(object):
    def replace(self, word, pos=None):
        antonyms = set()

        for syn in wordnet.synsets(word, pos=pos):
            for lemma in syn.lemmas():
                for antonym in lemma.antonyms():
                    antonyms.add(antonym.name())

        if len(antonyms) == 1:
            return antonyms.pop()
        elif len(antonyms) > 1:
            for ant in antonyms:
                return ant
        else:
            return None

    def replace_negations(self, sent):
        i, l = 0, len(sent)
        words = []

        while i < l:
            word = sent[i]

            if word == 'not' and i + 1 < l:
                ant = self.replace(sent[i + 1])

                if ant:
                    if sent[i + 2] == 'and' and sent[i + 3] == 'will' and sent[i + 4] == 'never':
                        words.append('very')
                        words.append(ant)
                        i += 6
                        continue
                    else:
                        words.append(ant)
                        i += 2
                        continue

            words.append(word)
            i += 1

        return words


if __name__ == '__main__':
    a = AntonymReplacer()
    print(a.replace('good'))
    print(a.replace('agree'))
    sent = ["Let's", 'not', 'disagree', 'on', 'this']
    words = a.replace_negations(sent)
    print(words)
