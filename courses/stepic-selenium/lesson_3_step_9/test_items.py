def test_add_to_basket_button_is_present(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_to_basket_button = browser.find_element_by_css_selector("#add_to_basket_form > button") 
    assert add_to_basket_button is not None, 'Add to basket button not found'
