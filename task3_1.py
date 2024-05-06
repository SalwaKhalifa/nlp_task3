import spacy
def tokenize_sentences(text, language='en'):
    if language == 'en':
        model_name = 'en_core_web_sm'
    elif language == 'fr':
        model_name = 'fr_core_news_sm'
    elif language == 'de':
        model_name = 'de_core_news_sm'
    else:
        raise ValueError("Unsupported language. Please provide a valid language code.")
    
    nlp = spacy.load(model_name)
    
    # Process the text using the loaded model
    doc = nlp(text)
    
    # Tokenize the text into sentences
    sentences = [sent.text for sent in doc.sents]
    
    return sentences

def main():
    text = input("Enter the text: ")
    language = input("Enter the language ('en' for English, 'fr' for French, 'de' for German): ")
    sentences = tokenize_sentences(text, language=language)
    print("\nTokenized Sentences:")
    for i, sentence in enumerate(sentences, start=1):
        print(f"Sentence {i}: {sentence}")

if __name__ == "__main__":
    main()
