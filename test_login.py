import pytest
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    # 1. Navigate to the demo login page
    page.goto("https://www.saucedemo.com/")
    
    # 2. Fill in standard user credentials
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    
    # 3. Click the login button
    page.click("#login-button")
    
    # 4. Verify successful redirection to the inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("\n[Test Passed]: Successfully logged into Saucedemo!")

def test_failed_login_error_message(page: Page):
    # Test negative path: invalid password
    page.goto("https://www.saucedemo.com/")
    
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password_123")
    page.click("#login-button")
    
    # Verify error message appears
    error_banner = page.locator("[data-test='error']")
    expect(error_banner).to_be_visible()
    print(f"\n[Test Passed]: Caught expected error: {error_banner.inner_text()}")

def test_valid_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # Intentionally wrong URL to force a test failure
    expect(page).to_have_url("https://www.saucedemo.com/wrong-page.html")