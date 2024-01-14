import nltk
import string

class TextProcessing:
    __porter = nltk.PorterStemmer()
    __wnl = nltk.WordNetLemmatizer()

    @staticmethod
    def download_dependencies():
        nltk.download('punkt') # used by tokenize()
        nltk.download('wordnet') # used by lemmatize()
        nltk.download('stopwords') # used by is_stopword()

    @staticmethod
    def tokenize(input: str) -> list[str]:
        return nltk.tokenize.word_tokenize(input)

    @staticmethod
    def stem(input: str) -> str:
        return TextProcessing.__porter.stem(input)

    @staticmethod
    def lemmatize(input: str) -> str:
        return TextProcessing.__wnl.lemmatize(input)

    @staticmethod
    def is_special(input: str) -> bool:
        return True if input in string.punctuation else False
    
    @staticmethod
    def is_stopword(input: str) -> bool:
        stopwords = nltk.corpus.stopwords.words('english')
        return True if input in stopwords else False