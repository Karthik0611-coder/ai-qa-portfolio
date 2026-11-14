import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

print("1. Initializing GenAI client with a 15-second timeout...")
try:
    # Set timeout to 15,000 milliseconds (15 seconds) so it fails fast if network drops
    client = genai.Client(
        http_options=types.HttpOptions(timeout=15_000)
    )
except Exception as e:
    print(f"Failed to initialize client: {e}")
    exit()

class BugTriage(BaseModel):
    bug_title: str = Field(description="Short, clear summary of the bug")
    severity: str = Field(description="Must be one of: Low, Medium, High, Critical")
    affected_module: str = Field(description="The UI page, API endpoint, or system component involved")
    is_regression: bool = Field(description="True if the text mentions it worked previously")
    recommended_action: str = Field(description="Suggested next steps for the engineering or QA team")

bug_log = "Users clicking checkout on mobile Safari get a white screen instead of the payment gateway, throwing a 500 internal server error."

print("2. Sending request to gemini-3.8-flash...")
try:
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=f"Analyze and triage this bug report: {bug_log}",
        config={
            'response_mime_type': 'application/json',
            'response_schema': BugTriage,
        },
    )
    print("3. Response received successfully!\n")
    print(response.text)
except Exception as e:
    print(f"\n[Network/API Error Caught]: {e}")
    print("Tip: Check if your internet connection or VPN is blocking api.generativeai.googleapis.com")