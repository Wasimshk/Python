myjson = {
    "status": "success",
    "data": {
        "users": [
            {
                "id": 1,
                "profile": {
                    "name": "Alice",
                    "contact": {
                        "email": "alice@example.com",
                        "phones": ["123-456-7890", "987-654-3210"]
                    }
                }
            },
            {
                "id": 2,
                "profile": {
                    "name": "Bob",
                    "contact": {
                        "email": "bob@example.com",
                        "phones": []
                    }
                }
            }
        ],
        "meta": {
            "total_users": 2,
            "generated_at": "2025-09-26T10:00:00Z"
        }
    }
}

# import json
# mydict = json.loads(myjson)
# # print(mydict)

mydict = myjson

print(mydict["data"]["users"][0]["profile"]["contact"]["phones"][0])

import numpy as np
import pandas as pd

df = pd.DataFrame(mydict)
# print(df)
#
# print(df.describe())

# print(df["users"])
