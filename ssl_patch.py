
import ssl, certifi

# Override the global SSL context
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
