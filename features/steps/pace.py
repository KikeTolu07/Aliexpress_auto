from behave import *
from pages.page_object import GuestShopper
from values import source

use_step_matcher("parse")

test = GuestShopper()



@given('I am on "{text}" site')
def step_impl(context, text):
    if text == "Aliexpress":
        test.setup(source.ali_url)
    elif text == "ebay":
        test.setup(source.ebay_url)



@step('I search and click on an item on "{text}"')
def step_impl(context, text):
    if text == "Aliexpress":
        test.search_and_click(source.ali_box, source.ali_item, source.ali_button)
    elif text == "ebay":
        test.search_and_click(source.ebay_box, source.ebay_item, source.ebay_button)



@step('I select an item on "{text}"')
def step_impl(context, text):
    if text == "Aliexpress":
        try:
            test.close_popup()
        except:
            test.scroll_page()
        test.select_item(source.ali_select_item)
    elif text == "ebay":
        test.select_item(source.ebay_select_item)



# @step('I added the "{text}" to cart')
# def step_impl(context, text):
#     if text == "Aliexpress":
#         test.scroll()

@step('I added the "{text}" item to cart')
def step_impl(context, text):
    if text == "Aliexpress":
        test.scroll()
        # test.select_country()
        test.add_to_cart(source.ali_add_to_cart, source.cont_book)
        test.view_item()
    elif text == "ebay":
        test.add_to_cart(source.ebay_add_to_cart, source.ebay_new)



@when('I proceed to check out on "{text}"')
def step_impl(context, text):
    if text == "Aliexpress":
        test.check_out(source.ali_checkout_button, source.ali_new_page)
    elif text == "ebay":
        test.check_out(source.ebay_checkout, source.ebay_new)



@then('I should be redirected to "{text}" sign in page')
def step_impl(context, text):
    if text == "Aliexpress":
        test.verify_page(source.ali_sign_in)
    elif text == "ebay":
        test.verify_page(source.ebay_sign_in)



