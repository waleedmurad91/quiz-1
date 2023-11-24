# Import necessary libraries
import streamlit as st
from nltk import ngrams
from nltk.tokenize import word_tokenize

# Function to generate n-grams
def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return n_grams

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

if __name__ == "__main__":
    main()
