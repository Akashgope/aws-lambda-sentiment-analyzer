# Assignment 8: Analyze Sentiment of User Reviews Using AWS Lambda and Amazon Comprehend

## Objective
Automatically analyze the sentiment of user reviews using Amazon Comprehend.

## Steps Followed

### 1. IAM Role Creation
- Created an IAM role for Lambda with the **ComprehendFullAccess** policy.
- Attached **AWSLambdaBasicExecutionRole** for logging.

### 2. Lambda Function Creation
- Created a Python 3.x Lambda function named `SentimentAnalyzer`.
- Assigned the IAM role.
- Wrote the code to extract the review from the event and call `comprehend.detect_sentiment()`.
- Deployed the function.

### 3. Testing
- Created test events with sample reviews:
  - Positive: *"This is an amazing product! I absolutely love it."*
  - Negative: *"I hated this product. It broke after one day."*
- Invoked the function and verified the sentiment output.

### Screenshots

#### Lambda Code
<img width="1390" height="741" alt="Screenshot 2026-03-22 at 5 21 01 PM" src="https://github.com/user-attachments/assets/f1d0dcd4-ab3d-48ff-a767-57996a09606b" />


#### Test Event (Positive)
<img width="1350" height="517" alt="Screenshot 2026-03-22 at 5 22 43 PM" src="https://github.com/user-attachments/assets/6953f889-7428-4606-aaa2-5bff305207fc" />


#### Execution Result (Positive)
<img width="1314" height="235" alt="Screenshot 2026-03-22 at 5 23 39 PM" src="https://github.com/user-attachments/assets/5176d067-69fc-40e4-9e29-a23c7b6ff92b" />


#### CloudWatch Logs
<img width="1664" height="551" alt="Screenshot 2026-03-22 at 5 24 17 PM" src="https://github.com/user-attachments/assets/0cd697e9-29b2-4cc2-9b13-9b742e073a9e" />


## Conclusion
The function successfully analyzes sentiment and logs the results.
