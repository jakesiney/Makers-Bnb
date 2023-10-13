from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/")

    # We look at the <h1> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(h1_tag).to_have_text("Feel at home, anywhere")


"""
We can view a list of spaces
"""
def test_view_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Book a Space")

def test_get_login(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/login")

    # We look at the <h1> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(h1_tag).to_have_text("Log in to Makers BnB")

def test_get_space(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/space")

    # We look at the <h1> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(h1_tag).to_have_text("List a Space")

