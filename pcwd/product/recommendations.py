from django.core.cache import cache
from django.shortcuts import get_object_or_404
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_recommendations(product_id, unique_products):
    # create a unique cache key for this product's recommendations
    cache_key = f'product_recommendations_{product_id}'

    # Check if recommendations are already cached
    cached_recommendations = cache.get(cache_key)

    if cached_recommendations:
        return cached_recommendations

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

    # cache the recommendations indefinitely
    cache.set(cache_key, recommended_products, timeout=None)

    return recommended_products
