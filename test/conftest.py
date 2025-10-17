import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os

import config
from appium import webdriver

from selene_in_action.utils import file
from selene_in_action.utils.attach_allure import attach_bstack_video


@pytest.fixture(scope='function', autouse=True)
def mobile_manager():
    if config.is_bstack:
        # BrowserStack configuration
        options = UiAutomator2Options().load_capabilities({
            'platformName': config.platformName,
            'platformVersion': config.platformVersion,
            'deviceName': config.deviceName,
            'app': config.app,
            'bstack:options': {
                'projectName': config.projectName,
                'buildName': config.buildName,
                'sessionName': config.sessionName,
                'userName': config.bstack_userName,
                'accessKey': config.bstack_accessKey,
            }
        })
        remote_url = config.remote_url
    else:
        # Local configuration (emulator or real device)
        app_path = (config.app if config.app.startswith('/')
                    else file.abs_path_from_project(config.app))

        options = UiAutomator2Options().load_capabilities({
            'platformName': config.platformName,
            'appium:deviceName': config.deviceName,
            'appium:app': app_path,
            'appium:appPackage': config.appPackage,
            'appium:appActivity': config.appActivity,
            'appium:automationName': config.automationName,
            'appium:noSign': True,
            'appium:autoGrantPermissions': True,
            'appium:skipDeviceInitialization': True,
            'appium:skipServerInstallation': True
        })
        remote_url = config.remote_url

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            remote_url,
            options=options
        )

    browser.config.timeout = config.timeout

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    # Attachments
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    if config.is_bstack:
        attach_bstack_video(session_id)