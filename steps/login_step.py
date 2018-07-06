
from behave import given, when, then
import allure


@given ('user is on Poczta Onet website')
def step_start_page (context):
    context.driver.get('http://poczta.onet.pl/')
    rodo = context.driver.find_element_by_css_selector("button.cmp-button_button.cmp-intro_acceptAll")

    if rodo.is_displayed():
        rodo.click()

@when('user fills valid username {username} and valid password {password} and submits it')
def step_set_login_in(context, username, password):
    context.driver.find_element_by_id('f_login').send_keys(username)
    context.driver.find_element_by_id('f_password').send_keys(password)
    context.driver.find_element_by_css_selector('#loginForm > div.formContainer > ul:nth-child(1) > li.perm > input.loginButton').click()

@then('User can see email list')
def step_valid_login(context):
   context.driver.save_screenshot("screenshot-login.png")
   allure.attach.file('screenshot-login.png', 'Opening url')
   assert context.driver.find_element_by_id('mailList-list-items')

@when('user fills invalid username {invalidusername} and invalid password {invalidpassword} and submits it')
def step_set_login_in(context, invalidusername, invalidpassword):
    context.driver.find_element_by_id('f_login').send_keys(invalidusername)
    context.driver.find_element_by_id('f_password').send_keys(invalidpassword)
    context.driver.find_element_by_css_selector('#loginForm > div.formContainer > ul:nth-child(1) > li.perm > input.loginButton').click()

@then('User can see alert about invalid date')
def step_valid_login(context):
   context.driver.save_screenshot("screenshot-invalidlogin.png")
   assert context.driver.find_element_by_css_selector('div.messageContent')


