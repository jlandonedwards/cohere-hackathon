import weaviate

client = weaviate.Client(
    url="https://turing-testers-oxy462kj.weaviate.network",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key="O71ZPqqOd547JzNIhaqjiWaXB7P3HVkxgXb9"),  # Replace w/ your Weaviate instance API key
)

client.schema.get()