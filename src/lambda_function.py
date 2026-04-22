import pandas as pd
import numpy as np

def lambda_handler(event, context):
    # Create numpy data
    data = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    # Create pandas DataFrame
    df = pd.DataFrame(data, columns=["A", "B", "C"])

    # Print dataframe (will appear in CloudWatch logs)
    print("DataFrame output:")
    print(df)

    return {
        "statusCode": 200,
        "body": df.to_json()
    }
