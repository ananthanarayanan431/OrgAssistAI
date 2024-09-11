from typing import Optional

from nemoguardrails.actions import action
from Model2 import ChatBot



@action(is_system_action=True)
async def check_blocked_terms(context: Optional[dict] = None):
    bot_response = context.get("bot_message")

    proprietary_terms = ["Nothing", "Nothing", "Nothing"]

    for term in proprietary_terms:
        if term in bot_response.lower():
            return True

    return False

@action(is_system_action=True)
async def check_quality(context: Optional[dict] = None):
    print("ADsfbdg")
    user_message = context.get("user_message")
    print('user_message is ', user_message)
    value=ChatBot(user_message)
    ans=value.Bot()
    return ans