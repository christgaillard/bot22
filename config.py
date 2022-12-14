import os


class DefaultConfig:
    """Configuration for the bot. sever"""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "d621f3cd-6d23-48a7-9581-b41aa80c4b0b")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "04a56dae074d46c18b122568ef6474e8")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "francecentral.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("INSTRUMENTATION_KEY", "5a851946-6687-43a8-ab57-72221a74b56e")
