#You can use this SDK for either production or #sandbox apps. For sandbox, the app username is #ALWAYS sandbox

# import package
import africastalking


# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "06350ab298d78637d78c439e6f3b2aaa2e949fd7b32e9fa458ae9f1a614cd83b"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello Message!", ["+254701869953"])
print(response)

# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send("Hello Message!", ["+254701869953"], callback=on_finish) 