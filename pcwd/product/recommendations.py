from django.shortcuts import get_object_or_404
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_recommendations(product_id, unique_products):
    product = get_object_or_404(unique_products, product_id)
    # exclude the product itself from the recommendations
    all_products = unique_products.exclude(id=product_id)

    # prepare descriptions for similarity computation
    descriptions = [product.description for product in all_products]
    descriptions.insert(0, product.description)

    # using TF-IDF Vectorizer to calculate similarity based on description
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(descriptions)
    cosine_similarities = cosine_similarity(vectors[0:1], vectors).flatten()

    # get the top 5 similar products (excluding the product itself)
    similar_indices = cosine_similarities.argsort()[-6:][::-1][1:]
    recommended_products = [all_products[i] for i in similar_indices]

    return recommended_products



