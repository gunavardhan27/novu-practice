from novu.api import EventApi
from novu.dto.subscriber import SubscriberDto
from novu.api.subscriber import SubscriberApi
url = "https://api.novu.co"
api_key = "cc88a54a19c6aef6a95fef6be5b829fd"

# You can sign up on https://dashboard.novu.co to get your API key from https://dashboard.novu.co/settings

'''novu = EventApi(url, api_key).trigger(
    name="digest-workflow-example",  # This is the Workflow ID. It can be found on the workflow page.
    recipients="<SUBSCRIBER_IDENTIFIER>", # The subscriber ID can be gotten from the dashboard.
    payload={},  # Your custom Novu payload goes here
)'''
subscriber_api = SubscriberApi(url,api_key)
def create_subscriber():
    subscriber = SubscriberDto(
    subscriber_id = '23',
    email = 'bgunavardhan27@gmail.com'
    )
    sub = subscriber_api.create(subscriber)
    print(sub)
    #print(SubscriberApi(url,api_key).list())

