import os
from dotenv import load_dotenv


def context_manager():
    context = os.getenv('CONTEXT', 'local_emulator')
    load_dotenv(f'.env.{context}')
    return context


CONTEXT = context_manager()

# Common settings
remote_url = os.getenv('REMOTE_URL')
deviceName = os.getenv('DEVICE_NAME')
platformName = os.getenv('PLATFORM_NAME')
app = os.getenv('APP')
appPackage = os.getenv('APP_PACKAGE')
appActivity = os.getenv('APP_ACTIVITY')
automationName = os.getenv('AUTOMATION_NAME')
timeout = float(os.getenv('TIMEOUT', '10.0'))

# BrowserStack specific
bstack_userName = os.getenv('BSTACK_USERNAME')
bstack_accessKey = os.getenv('BSTACK_ACCESS_KEY')
platformVersion = os.getenv('PLATFORM_VERSION')
projectName = os.getenv('PROJECT_NAME')
buildName = os.getenv('BUILD_NAME')
sessionName = os.getenv('SESSION_NAME')

# Context flags
is_bstack = CONTEXT == 'bstack'
is_local_emulator = CONTEXT == 'local_emulator'
is_local_real = CONTEXT == 'local_real'