from app.interfaces.telegram.client import send_message
from app.interfaces.telegram.keyboard.inline import about_keyboard_payload

async def handle_about(chat_id: int):
    message = (
        "Vantly — Your Personal Research and Intelligence Assistant.\n"
        "Your vantage point for information, research, and intelligence.\n\n"

        "Information is everywhere, but finding, evaluating, and understanding "
        "relevant information isn't always easy.\n\n"

        "Vantly addresses this challenge by discovering, curating, analysing, "
        "and organising information gathered from across the internet, "
        "turning scattered information into structured and meaningful research.\n\n"

        "How It Works:\n"
        "1. A registered user submits a research topic and specifies their "
        "Duration of Monitoring (DoM).\n"
        "2. AI analyses the topic and generates relevant keywords to broaden "
        "the scope of the research.\n"
        "3. Vantly searches for relevant information and organises its findings "
        "according to their credibility and reliability.\n"
        "4. AI provides detailed summaries and additional context for each "
        "piece of information discovered.\n"
        "5. At the end of the research process, Vantly presents an organised "
        "collection of information, summaries, and insights that users can "
        "use to support their research.\n\n"

        "Want to learn more about how Vantly works?\n"
        "See the Official Documentation for more details."
    )
    
    await send_message(chat_id, message, about_keyboard_payload)