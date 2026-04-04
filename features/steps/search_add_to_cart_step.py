from behave import given, when, then
from features.pages.search_add_to_cart_page import search_add_to_cart_page

@given(u'User navigates to adnabu store')
def step_impl(context):
    context.pages = search_add_to_cart_page(context)
    context.pages.navigate_to_adnabu_store()

@given(u'User enters store password "{password}"')
def step_impl(context, password):
    context.pages = search_add_to_cart_page(context)
    context.pages.enter_store_password(password)

@when(u'User is on adnabu store homepage')
def step_impl(context):
    context.pages = search_add_to_cart_page(context)
    context.pages.validate_homepage()

@then(u'User clicks on enter button')
def step_impl(context):
    context.pages = search_add_to_cart_page(context)
    context.pages.click_on_enter_button()

@then(u'User clicks on shop products button')
def step_impl(context):
    context.pages = search_add_to_cart_page(context)
    context.pages.click_on_shop_products_button()

@then(u'User clicks on add to cart button')
def step_impl(context):
    context.pages = search_add_to_cart_page(context)
    context.pages.click_on_add_to_cart_button()

@then(u'User clicks on search icon')
def step_impl(context):
    context.pages = search_add_to_cart_page(context)
    context.pages.click_on_search_icon()

@then(u'User searches for "{product_name}"')
def step_impl(context, product_name):
    context.pages = search_add_to_cart_page(context)
    context.pages.search_for_product(product_name)

@then(u'User validates the search result')
def step_impl(context):
    context.pages = search_add_to_cart_page(context)
    context.pages.validate_search_result()

@when(u'User clicks on the search result')
def step_impl(context):
    context.pages = search_add_to_cart_page(context)
    context.pages.click_on_search_result()

@then(u'User verifies the product is successfully added to cart')
def step_impl(context):
    context.pages = search_add_to_cart_page(context)
    context.pages.verify_product_in_cart()