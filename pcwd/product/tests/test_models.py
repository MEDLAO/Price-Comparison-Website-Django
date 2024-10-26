import pytest
from product.models import ScrapedProduct, Website


@pytest.mark.django_db
def test_website_str_method(website):
    """
    Tests the __str__ method of the Website model.
    """
    assert str(website) == 'AM EG'


@pytest.mark.django_db
def test_scraped_product_str_method(scraped_product):
    """
    Tests the __str__ method of the ScrapedProduct model.
    """
    assert str(scraped_product) == f'{scraped_product.brand} {scraped_product.product_type} ' \
                                   f'- Scraped from {scraped_product.website.name}'


@pytest.mark.django_db
def test_translations_in_database(scraped_product):
    """
    Tests that English and Arabic translations are correctly stored in the database.
    """
    # verify English translations
    scraped_product.set_current_language('en')
    assert scraped_product.description == 'English description'
    assert scraped_product.brand == 'Brand A'
    assert scraped_product.color == 'Red'
    assert scraped_product.currency == 'EGP'
    assert scraped_product.product_url == 'https://www.amazon.eg/Xiaomi-Display-Resistant-' \
                                          'Battery-Tracking/dp/B0C7R1RN2D/ref=mp_s_a_1_4?crid' \
                                          '=3L75S7JNV9KZD&dib=eyJ2IjoiMSJ9.eUPxj3SOeVi8nifQdN' \
                                          'TFBthj71E0EkWGzaJ0TXsnOJ3WY26F-mXV12xKLRDlgiu_sJ6dTe' \
                                          '5KmrWIrZJe8KGyD47vaW5_T-9D1d-vevwtaGvMZDCs5VFA9IFIH98' \
                                          '-UgZrg2bDhyxzlHNdxqBuf48nCz9gya6cBekCMu8stNY_vN-T1Uo' \
                                          'f4Mghv4XG2P5Dmdw8SPsYRRAdaLvo4R3Tdb0Aaw.27WRZzP9eK7D0' \
                                          'aNiT5PLaVKlu5pKYK2_IxEnGeuct_k&dib_tag=se&keywords=' \
                                          'smart%2Bwatches&qid=1721756059&sprefix=smart%2Bwa%2' \
                                          'Caps%2C599&sr=8-4&th=1'

    # verify Arabic translations
    scraped_product.set_current_language('ar')
    assert scraped_product.description == 'وصف عربي'
    assert scraped_product.brand == 'العلامة التجارية أ'
    assert scraped_product.color == 'أحمر'
    assert scraped_product.currency == 'جنيه'
    assert scraped_product.product_url == "https://www.amazon.eg/%D8%B4%D8%A7%D9%88%D9%85%D9%8A" \
                                          "-%D8%A7%D9%84%D9%85%D9%88%D8%A7%D9%82%D8%B9-%D8%A7" \
                                          "%D9%84%D8%B9%D8%A7%D9%84%D9%85%D9%8A-%D8%A7%D9%84%D9%" \
                                          "84%D9%8A%D8%A7%D9%82%D8%A9-%D8%A7%D9%84%D8%A8%D8%AF%" \
                                          "D9%86%D9%8A%D8%A9/dp/B0C7R1RN2D/ref=sr_1_6?crid=" \
                                          "3LI1Y8NP6ZWR9&dib=eyJ2IjoiMSJ9.eUPxj3SOeVi8nifQdNTFB" \
                                          "pU729InDij1qnWUROwBhLw3z2Wf2E0YfCQHGUVxZ_OUsqvymnhuHN" \
                                          "azS6OqmMvsE89VzwHdsjU2xwu9nf5O-gS9YXIJ-DEKyWWMKcoM-" \
                                          "vs8aK9aLWj25KPLQqfzkhoox-lN6gC4R67PnQRkyqSHYDVYUz" \
                                          "FxUnLG-UFRn5rqcFsVGEm-KIcpz_f8j33yBugpGXUmgv0XVXWe-" \
                                          "T6IynR1IExGoS2Kw_7ZCVERsTEqeQesQpGmGgEN3DBTB_DAoNSF" \
                                          "ziexFfnEpPdPZ6dDJn__FWc.0jE8XfZWep94jg7pj0mQtHzq0eSud" \
                                          "7NNOcZU3oiqUj4&dib_tag=se&keywords=smart%2Bwatch&qid=" \
                                          "1721930997&sprefix=smart%2Caps%2C579&sr=8-6&th=1"
