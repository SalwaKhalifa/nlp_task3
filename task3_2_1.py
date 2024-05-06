import spacy

def pos_tagging(text):
    # Load the English language model in SpaCy
    nlp = spacy.load("en_core_web_sm")
    
    # Process the input text
    doc = nlp(text)
    
    # Extract part-of-speech tags for each word with Universal Dependencies tagset
    tagged_words_universal = [(token.text, token.pos_) for token in doc]
    
    # Extract part-of-speech tags for each word with Penn Treebank tagset
    tagged_words_penn = [(token.text, token.tag_) for token in doc]
    
    return tagged_words_universal, tagged_words_penn

def main():
    # Input text from the user
    text = input("Enter the text: ")
    
    # Apply part-of-speech tagging using SpaCy
    tagged_words_universal, tagged_words_penn = pos_tagging(text)
    
    # Print the results with Universal Dependencies tagset
    print("\nPOS tags with Universal Dependencies tagset:")
    for word, tag in tagged_words_universal:
        print(f"{word}: {tag}")
    
    # Print the results with Penn Treebank tagset
    print("\nPOS tags with Penn Treebank tagset:")
    for word, tag in tagged_words_penn:
        print(f"{word}: {tag}")

if __name__ == "__main__":
    main()
