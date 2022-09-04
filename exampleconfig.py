from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 15855531
    API_HASH = "31e0b87de4285ebff259e003f58bf469"
    # the name to display in your alive message
    ALIVE_NAME = "Tony"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://fkwuufyg:UZrl_PEvo2vTRHxTKGa9XAM54lxZ0UaL@kashin.db.elephantsql.com/fkwuufyg"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOMABuwNrcnt4IoitNMfNGm6BTcLVENSfvUFLM9TentiMK8cpB09VQfIDBvlxc1XMLIwRGRrYxfz8LNOMk_tTl1o4Ll404PcP_FFF9IMJ2RlUiHke8nEB_vpMoJrASgmZjSI3t9oA57Ftu4ngEEO-JpNYzpuqsy9eUrOJPPv_WpKOlnn6_3caes_OPvGs7oicJ5Q-eTHOHLE73QL3xFEoDlIJSUmgweL9of7KF6x5Wq6ZKQ4IlGpwYzoDxqq7LS7p7NUf2TAQr-3oJ4LKsdYKzRWp2pKGRllqbZqPTQaxuiw5gHs4530nwtXZ6Rbh3SxG5HdD4RGPcBWmWbJURazdrz4H16M="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5770196022:AAHD_1HsiBFApSJe6X9h9Vyn64HbPG0NLLE"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001585340316
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
