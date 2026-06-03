import json

from openai import OpenAI

from src.config.settings import OPENAI_API_KEY
from src.ingestion.utils.logger import get_logger

logger = get_logger(__name__)

client = OpenAI(
    api_key=OPENAI_API_KEY
)

RISK_CATEGORIES = [
    "Fraud Risk",
    "Credit Reporting Risk",
    "Payment Processing Risk",
    "Customer Service Risk",
    "Debt Collection Risk",
    "Mortgage Risk",
    "Compliance Risk",
    "Other"
]


def analyze_complaint(
    complaint_text: str
):

    prompt = f"""
You are a Financial Risk Analyst.

Analyze the complaint and return ONLY valid JSON.

Choose ONE risk category from:

{RISK_CATEGORIES}

Sentiment must be:
Positive, Neutral, or Negative.

Return this structure:

{{
    "risk_category": "",
    "sentiment": "",
    "summary": ""
}}

Complaint:

{complaint_text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        response_format={
            "type": "json_object"
        },
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = json.loads(
        response.choices[0].message.content
    )

    return result