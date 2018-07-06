from selenium import webdriver
import selenium


def before_scenario(context, scenario):

    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(3)

def after_scenario(context, scenario):
    context.driver.quit()

