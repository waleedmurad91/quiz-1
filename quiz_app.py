import streamlit as st
import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download NLTK data
nltk.download('punkt')

# Function to generate n-grams
def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return n_grams

# Function to generate and display word cloud
def display_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()

# Streamlit web application
def main():
    st.title("N-gram")

    # Input text area
    text_input = st.text_area("Enter your text here:")

    # Select n for n-grams
    n = st.slider("Select the 'n' value for n-grams:", min_value=1, max_value=5, value=2)

    # Button to generate n-grams
    if st.button("Generate N-grams"):
        # Generate and display n-grams
        n_grams = generate_ngrams(text_input, n)
        st.write(f"{n}-grams:")
        st.write(n_grams)

        # Display word cloud
        text_for_wordcloud = ' '.join([' '.join(gram) for gram in n_grams])
        display_word_cloud(text_for_wordcloud)

if __name__ == "__main__":
    main()
