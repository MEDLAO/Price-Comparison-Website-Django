import pytest
from .models import ScrapedProduct, Website


@pytest.fixture
def website():
    return Website.objects.create(name='AM')


@pytest.fixture
def scraped_product(website):
    return ScrapedProduct.objects.create(
        website=website,
        product_url="https://www.amazon.eg/Xiaomi-Display-Resistant-Battery-Tracking/dp/B0C7R1RN2D"
                    "/ref=mp_s_a_1_4?crid=3L75S7JNV9KZD&dib=eyJ2IjoiMSJ9.eUPxj3SOeVi8nifQdNTFBthj"
                    "71E0EkWGzaJ0TXsnOJ3WY26F-mXV12xKLRDlgiu_sJ6dTe5KmrWIrZJe8KGyD47vaW5_T-9D1d-"
                    "vevwtaGvMZDCs5VFA9IFIH98-UgZrg2bDhyxzlHNdxqBuf48nCz9gya6cBekCMu8stNY_vN-"
                    "T1Uof4Mghv4XG2P5Dmdw8SPsYRRAdaLvo4R3Tdb0Aaw.27WRZzP9eK7D0aNiT5PLaVKlu5pKYK2_"
                    "IxEnGeuct_k&dib_tag=se&keywords=smart%2Bwatches&qid=1721756059&sprefix=smart"
                    "%2Bwa%2Caps%2C599&sr=8-4&th=1",
        image_url="https://m.media-amazon.com/images/I/615LVMteaYL._AC_SL1500_.jpg"
    )
