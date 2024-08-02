import pytest
from django.test import Client
from .models import ScrapedProduct, Website


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def website():
    return Website.objects.create(name='AM')


@pytest.fixture
def scraped_product(website):
    scraped_product = ScrapedProduct.objects.create(
        website=website,
        product_url="https://www.amazon.eg/Xiaomi-Display-Resistant-Battery-Tracking/dp/B0C7R1RN2D"
                    "/ref=mp_s_a_1_4?crid=3L75S7JNV9KZD&dib=eyJ2IjoiMSJ9.eUPxj3SOeVi8nifQdNTFBthj"
                    "71E0EkWGzaJ0TXsnOJ3WY26F-mXV12xKLRDlgiu_sJ6dTe5KmrWIrZJe8KGyD47vaW5_T-9D1d-"
                    "vevwtaGvMZDCs5VFA9IFIH98-UgZrg2bDhyxzlHNdxqBuf48nCz9gya6cBekCMu8stNY_vN-"
                    "T1Uof4Mghv4XG2P5Dmdw8SPsYRRAdaLvo4R3Tdb0Aaw.27WRZzP9eK7D0aNiT5PLaVKlu5pKYK2_"
                    "IxEnGeuct_k&dib_tag=se&keywords=smart%2Bwatches&qid=1721756059&sprefix=smart"
                    "%2Bwa%2Caps%2C599&sr=8-4&th=1",
        image_url="https://m.media-amazon.com/images/I/615LVMteaYL._AC_SL1500_.jpg",
    )

    # set English translations
    scraped_product.translations.create(
        language_code='en',
        description='English description',
        brand='Brand A',
        color='Red',
        currency='EGP'
    )

    scraped_product.translation.create(
        language_code='en',
        product_url="https://www.amazon.eg/Xiaomi-Display-Resistant-Battery-Tracking/dp/B0C7R1RN2D"
                    "/ref=mp_s_a_1_4?crid=3L75S7JNV9KZD&dib=eyJ2IjoiMSJ9.eUPxj3SOeVi8nifQdNTFBthj"
                    "71E0EkWGzaJ0TXsnOJ3WY26F-mXV12xKLRDlgiu_sJ6dTe5KmrWIrZJe8KGyD47vaW5_T-9D1d-"
                    "vevwtaGvMZDCs5VFA9IFIH98-UgZrg2bDhyxzlHNdxqBuf48nCz9gya6cBekCMu8stNY_vN-"
                    "T1Uof4Mghv4XG2P5Dmdw8SPsYRRAdaLvo4R3Tdb0Aaw.27WRZzP9eK7D0aNiT5PLaVKlu5pKYK2_"
                    "IxEnGeuct_k&dib_tag=se&keywords=smart%2Bwatches&qid=1721756059&sprefix=smart"
                    "%2Bwa%2Caps%2C599&sr=8-4&th=1"
    )

    # set Arabic translations
    scraped_product.translations.create(
        language_code='ar',
        description='وصف عربي',
        brand='العلامة التجارية أ',
        color='أحمر',
        currency='جنيه'
    )

    scraped_product.translation.create(
        language_code='ar',
        product_url="https://www.amazon.eg/%D8%B4%D8%A7%D9%88%D9%85%D9%8A-%D8%A7%D9%84%D9%85%D9%88"
                    "%D8%A7%D9%82%D8%B9-%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85%D9%8A-%D8%A7%D9%84%D9"
                    "%84%D9%8A%D8%A7%D9%82%D8%A9-%D8%A7%D9%84%D8%A8%D8%AF%D9%86%D9%8A%D8%A9/dp/"
                    "B0C7R1RN2D/ref=sr_1_6?crid=3LI1Y8NP6ZWR9&dib=eyJ2IjoiMSJ9.eUPxj3SOeVi8nifQdNT"
                    "FBpU729InDij1qnWUROwBhLw3z2Wf2E0YfCQHGUVxZ_OUsqvymnhuHNazS6OqmMvsE89VzwHdsjU2"
                    "xwu9nf5O-gS9YXIJ-DEKyWWMKcoM-vs8aK9aLWj25KPLQqfzkhoox-lN6gC4R67PnQRkyqSHYDVYU"
                    "zFxUnLG-UFRn5rqcFsVGEm-KIcpz_f8j33yBugpGXUmgv0XVXWe-T6IynR1IExGoS2Kw_7ZCVERs"
                    "TEqeQesQpGmGgEN3DBTB_DAoNSFziexFfnEpPdPZ6dDJn__FWc.0jE8XfZWep94jg7pj0mQtHzq0"
                    "eSud7NNOcZU3oiqUj4&dib_tag=se&keywords=smart%2Bwatch&qid=1721930997&sprefix="
                    "smart%2Caps%2C579&sr=8-6&th=1"
    )

    return scraped_product
