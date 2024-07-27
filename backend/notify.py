from novu.api import EventApi,NotificationTemplateApi
from novu.dto.subscriber import SubscriberDto
from novu.api.subscriber import SubscriberApi
import requests
url = "https://api.novu.co"
api_key = "cc88a54a19c6aef6a95fef6be5b829fd"
#api_key = "e4be5ff470630be770f2412b4b8961c2"

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
        name="welcome-onboarding-email",
        recipients = ["23"],
        actor={
            "subscriberId":"12"
        },
        payload={
           "message":"demuda",
        },
    )
    print(k)
#this is working
def get_workflow():
    x=NotificationTemplateApi(url,api_key).get(
        notification_template_id='example'
    )
    print(x)
    

def create_workflows():
    

    # Replace with your actual API key and endpoint

    headers = {
        'Authorization': f'ApiKey {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        "notificationGroupId": "607f1f77bcf86cd799439980",
        "name":"example",
        "steps": [
            {
                "template": {
                "type": "in_app",
                "subject": "Welcome!",
                "body": "Thank you for signing up.",
                    "cta": {
                        "data": {
                            "url": "circle/profile/new_circle.id"
                        },
                    },
                
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
        "triggers":[
            {
            "type":"event",
            "identifier":"example",
            "variables":[
                {
                    "name":"ussr-name"
                }
            ]
            }
            
        ],
        
    }

    response = requests.request('POST','https://api.novu.co/v1/workflows', headers=headers, json=payload)

    if response.status_code == 201: 
        print("Workflow created successfully!")
    else:
        print(f"Failed to create workflow: {response.status_code}")
        print(response.json())

# np
'''
{
  "data": {
    "preferenceSettings": {
      "email": true,
      "sms": true,
      "in_app": true,
      "chat": true,
      "push": true
    },
    "_id": "6671b6bb7a3b0c4477a681a2",
    "name": "new-user-circle-content",
    "active": true,
    "type": "REGULAR",
    "draft": false,
    "critical": false,
    "isBlueprint": false,
    "_notificationGroupId": "65fd9b098b3193b7f000e4a6",
    "tags": [],
    "triggers": [
      {
        "type": "event",
        "identifier": "new-user-circle-content",
        "variables": [
          {
            "name": "followed_user.username",
            "type": "String",
            "_id": "6671b732db3e854f50641e88",
            "id": "6671b732db3e854f50641e88"
          },
          {
            "name": "new_topic.title",
            "type": "String",
            "_id": "6671b732db3e854f50641e89",
            "id": "6671b732db3e854f50641e89"
          }
        ],
        "reservedVariables": [],
        "subscriberVariables": [],
        "_id": "6671b6bb7a3b0c4477a681a3",
        "id": "6671b6bb7a3b0c4477a681a3"
      }
    ],
    "steps": [
      {
        "replyCallback": {},
        "metadata": {
          "timed": {
            "weekDays": [],
            "monthDays": []
          }
        },
        "active": true,
        "shouldStopOnFail": false,
        "uuid": "4e78409f-b403-45a6-943f-be27ddb7d7ed",
        "name": "In-App",
        "type": "REGULAR",
        "filters": [],
        "_templateId": "6671b732db3e854f50641e70",
        "_parentId": null,
        "_id": "6671b732db3e854f50641e70",
        "variants": [],
        "id": "6671b732db3e854f50641e70",
        "template": {
          "cta": {
            "data": {
              "url": "circle/profile/new_circle.id"
            }
          },
          "actor": {
            "type": "none",
            "data": null
          },
          "_id": "6671b732db3e854f50641e70",
          "type": "in_app",
          "active": true,
          "subject": "",
          "variables": [
            {
              "name": "followed_user.username",
              "type": "String",
              "required": false,
              "_id": "6671b732db3e854f50641e71",
              "id": "6671b732db3e854f50641e71"
            },
            {
              "name": "new_topic.title",
              "type": "String",
              "required": false,
              "_id": "6671b732db3e854f50641e72",
              "id": "6671b732db3e854f50641e72"
            }
          ],
          "content": "{{followed_user.username}} posted a new topic {{new_topic.title}}.",
          "contentType": "editor",
          "_environmentId": "65fd9b098b3193b7f000e4a0",
          "_organizationId": "65fd9b098b3193b7f000e48f",
          "_creatorId": "65fd9ac339829e6c76ea75c0",
          "_feedId": null,
          "_layoutId": null,
          "deleted": false,
          "createdAt": "2024-06-18T16:34:58.497Z",
          "updatedAt": "2024-06-18T16:34:58.497Z",
          "__v": 0,
          "id": "6671b732db3e854f50641e70"
        }
      }
    ],
    "_environmentId": "65fd9b098b3193b7f000e4a0",
    "_organizationId": "65fd9b098b3193b7f000e48f",
    "_creatorId": "65fd9ac339829e6c76ea75c0",
    "deleted": false,
    "createdAt": "2024-06-18T16:32:59.157Z",
    "updatedAt": "2024-06-18T16:34:58.539Z",
    "__v": 0,
    "id": "6671b6bb7a3b0c4477a681a2"
  }
}'''