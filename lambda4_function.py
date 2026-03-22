import boto3
import json


def lambda_handler(event, context):
   # The review text is expected in the event as a string under the key "review"
   review_text = event.get("review", "")
   if not review_text:
       return {
           "statusCode": 400,
           "body": "No review text provided in the event."
       }


   comprehend = boto3.client("comprehend")
  
   try:
       response = comprehend.detect_sentiment(
           Text=review_text,
           LanguageCode="en"
       )
       sentiment = response["Sentiment"]          # e.g., POSITIVE, NEGATIVE, NEUTRAL, MIXED
       confidence = response["SentimentScore"]    # dictionary with scores
      
       print(f"Review: {review_text}")
       print(f"Sentiment: {sentiment}")
       print(f"Confidence: {confidence}")
      
       return {
           "statusCode": 200,
           "body": json.dumps({
               "review": review_text,
               "sentiment": sentiment,
               "confidence": confidence
           })
       }
   except Exception as e:
       print(f"Error: {e}")
       return {
           "statusCode": 500,
           "body": f"Error analyzing sentiment: {e}"
       }