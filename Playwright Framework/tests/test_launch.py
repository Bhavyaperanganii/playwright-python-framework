def test_launch(page):
    page.goto("https://www.saucedemo.com")
    page.wait_for_timeout(3000)

    assert page.title() == "Swag Labs"