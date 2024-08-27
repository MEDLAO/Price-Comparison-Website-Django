from django.shortcuts import get_object_or_404
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_recommendations(product_id, unique_products):
    product = get_object_or_404(unique_products, product_id)
    # exclude the product itself from the recommendations
    all_products = unique_products.exclude(id=product_id)


