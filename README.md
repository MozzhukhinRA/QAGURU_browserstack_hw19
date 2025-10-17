# Used this command depending on env

# Для локального эмулятора
CONTEXT=local_emulator pytest test/test_onboarding.py -v

# Для реального устройства
CONTEXT=local_real pytest test/test_onboarding.py -v

# Для BrowserStack
CONTEXT=bstack pytest test/test_onboarding.py -v