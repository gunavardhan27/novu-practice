from novu.api import EventApi,NotificationTemplateApi
from novu.dto.subscriber import SubscriberDto
from novu.api.subscriber import SubscriberApi
import requests
url = "https://api.novu.co"
api_key = "0e2a1305be57348bc5f9e32ce728f163"

# You can sign up on https://dashboard.novu.co to get your API key from https://dashboard.novu.co/settings

'''novu = EventApi(url, api_key).trigger(
    name="digest-workflow-example",  # This is the Workflow ID. It can be found on the workflow page.
    recipients="<SUBSCRIBER_IDENTIFIER>", # The subscriber ID can be gotten from the dashboard.
    payload={},  # Your custom Novu payload goes here
)'''
subscriber_api = SubscriberApi(url,api_key)
event_api = EventApi(url,api_key)
not_api = NotificationTemplateApi(url,api_key)
def create_subscriber():
    subscriber = SubscriberDto(
    subscriber_id = '23',
    email = 'bgunavardhan27@gmail.com'
    )
    sub = subscriber_api.create(subscriber)
    print(sub)
    #print(SubscriberApi(url,api_key).list())

def send_notification():
    k=event_api.trigger(
        name="normal_message",
        
        recipients = "23",
        actor={
            "subscriberId":["12"]
        },
        payload={
           "message":"demuda",
        },
    )
    print(k)

def create_workflows():

    # Replace with your actual API key and endpoint

    headers = {
        'Authorization': f'ApiKey {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        "notificationGroupId": "507f1f77bcf86cd799439014",
        "name":"email-workflow",
        "steps": [
            {
                "type": "custom",
                "template": {
                "subject": "Welcome!",
                "body": "Thank you for signing up."
                },
                "recipient": "bgunavardhan27@gmail.com",
                "filters": [
                    {
                        "property": "user.role",
                        "operator": "equals",
                        "value": "new_user"
                    }
                ],
                "variant": {
                    "variantName": "New User Welcome Email",
                    "variantId": "507f1f77bcf86cd799439011"
                }
            },
           
        ],
        
    }

    response = requests.post('https://api.novu.co/v1/workflows', headers=headers, json=payload)

    if response.status_code == 201: 
        print("Workflow created successfully!")
    else:
        print(f"Failed to create workflow: {response.status_code}")
        print(response.json())

# Call the function to create the workflow



'''
{
                "type": "updateDatabase",
                "table": "users",
                "recordId": "12345",
                "fields": {
                    "status": "active"
                },
                "variant": {
                    "variantName": "Update User Status",
                    "variantId": "507f1f77bcf86cd799439012"
                }
            },
            {
                "type": "webhook",
                "url": "https://api.example.com/notify",
                "method": "POST",
                "body": {
                    "userId": "12345",
                    "event": "signup"
                },
                "variant": {
                    "variantName": "Signup Notification",
                    "variantId": "507f1f77bcf86cd799439013"
                }
            }'''