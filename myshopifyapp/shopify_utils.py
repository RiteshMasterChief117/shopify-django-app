from django.conf import settings
import shopify

# def get_shopify_session():
#     session = shopify.Session(
#         f"https://{settings.SHOPIFY_STORE_DOMAIN}",
#         settings.SHOPIFY_API_VERSION,
#         settings.SHOPIFY_ACCESS_TOKEN
#     )
#     shopify.ShopifyResource.activate_session(session)
#     return session


def get_shopify_session():
    if not settings.SHOPIFY_STORE_DOMAIN or not settings.SHOPIFY_ACCESS_TOKEN:
        raise ValueError("SHOPIFY_STORE_DOMAIN or SHOPIFY_ACCESS_TOKEN is not set")

    session = shopify.Session(
        f"https://{settings.SHOPIFY_STORE_DOMAIN}",
        settings.SHOPIFY_API_VERSION,
        settings.SHOPIFY_ACCESS_TOKEN
    )
    shopify.ShopifyResource.activate_session(session)
    return session