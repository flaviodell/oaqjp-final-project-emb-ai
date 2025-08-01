"""
This module contains the function that performs emotion detection.
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """
    This is the function that performs emotion detection.
    """
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions.get('anger')
    disgust_score = emotions.get('disgust')
    fear_score = emotions.get('fear')
    joy_score = emotions.get('joy')
    sadness_score = emotions.get('sadness')

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)

    return emotion_scores
