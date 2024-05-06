import spacy

def pos_tagging(text):
    # Load the English language model in SpaCy
    nlp = spacy.load("en_core_web_sm")
    
    # Process the input text
    doc = nlp(text)
    
    # Extract part-of-speech tags for each word with Universal Dependencies tagset
    tagged_words_ud = [(token.text, token.tag_) for token in doc]
    
    return tagged_words_ud

def main():
    # Input text from the user
    text = input("Enter the text: ")
    
    # Apply part-of-speech tagging using SpaCy
    tagged_words_ud = pos_tagging(text)
    
    # Print the results with Universal Dependencies tagset
    print("\nPOS tags with Universal Dependencies tagset:")
    for word, tag in tagged_words_ud:
        if word.islower():
            print(f"{word}: Small")
        elif word.isupper():
            print(f"{word}: Capital")
        else:
            print(f"{word}: Mixed")

if __name__ == "__main__":
    main()
