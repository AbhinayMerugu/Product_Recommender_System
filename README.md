# Content-Based Recommendation System

## [Live Application](https://smart-pick-recommender-system.streamlit.app/)

## Overview

This project involves building a content-based recommendation system to suggest similar products to users. The system uses a dataset created by combining multiple product categories, helping users discover items similar to those they are interested in, with direct purchase links. An interactive **Streamlit application** was developed and deployed for ease of use.

## Project Highlights

1. **Dataset Creation**:  
   - Combined multiple datasets from the following categories:  
     **Electronics** | **Headphones** | **Watches** | **Sportswear** | **Televisions**  
   - Created a final dataset of **5,300 products**.

2. **Feature Extraction**:  
   - Extracted relevant features and tags for each product.  
   - **Stemming** of product features using **NLTK** to reduce words to their root forms ensuring consistency in text data.

3. **Vectorization**:  
   - Converted product features and tags into vectors using **CountVectorizer**, transforming text data into numerical format suitable for similarity calculations.

4. **Recommendation System**:  
   - Applied **cosine similarity** to measure the similarity between product vectors.  
   - Generated recommendations for similar products along with purchase links.

5. **Deployment**:  
   - Developed an interactive **Streamlit application** to allow users to input a product and receive recommendations.  
   - Deployed the application on **Streamlit Community Cloud**.

## Technologies Used

- **Libraries**:  
  Python | Streamlit | scikit-learn (CountVectorizer, Cosine Similarity) | Pandas | NumPy | NLTK (Stemming)  

- **Tools**:  
  Streamlit Community Cloud  

## How to Use the Application

1. Visit the deployed [Application](https://smart-pick-recommender-system.streamlit.app/)  
2. Select or enter a product to receive recommendations of similar products.  
3. Click the provided purchase links to explore or buy the recommended products.
