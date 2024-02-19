
from django.conf import settings

from lib.twitter import post_tweet
from lib.llm import ai
from lib.llm.semantic import get_random_topic
from lib.llm.templates import promts_templates

sent_tweet_number = 0
def tweet():
    global sent_tweet_number

    model = ai.get_model(0.6)
    topic = get_random_topic()
    response, iterations = ai.generate_response(llm=model, topic=topic,

                                                sys_template=promts_templates.one_twitter_system)
    post_tweet(response, fakeSend=False)
    sent_tweet_number += 1

    return sent_tweet_number