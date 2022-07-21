from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 6
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
    # the name to display in your alive message
    ALIVE_NAME = "Your value"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "mongodb+srv://Devilharsha:Devilharsha@cluster0.exwkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOMABu6OXr8Cc55nbqq2UgfskIgw-NNupVHW65PQ98XRvg4Fi_a6gHQE8xGz3VRPcixdx9ambahFIp2m6wRAjd2lAvwNnwD8vmQjatNnHyIAuNZjf-jteGvJPww6iLVssU9N7rASyThAGeJB2mdTu3aas3GHemVd8juXVO9xOnyY6Kx3P_daYOiyg5GZ5SXUwgou0uO1Ad1Jt_M8vDPJzotqFvngiHt-0VOktoPlacf5s9FHmzH7vif5NiVpPU1Y5DT30RVedpXKOjgocp_r0vEQVQHHbXhi6VpVPQuOykjsXO9axPnbgEN_REzT6g4sbC7yN2MJm3NfPf-lJhzkN4mfQsMY="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5317920065:AAGWadLJ4IfcGqANBR3Yes4QUflJXaHvJ7o"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
