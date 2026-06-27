from mcp.server.fastmcp import FastMCP
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import os

print("Starting Calendar MCP")

mcp = FastMCP("CalendarMCP")

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

if not os.path.exists("token.json"):
    raise FileNotFoundError(
        "token.json not found. Run server.py first."
    )

creds = Credentials.from_authorized_user_file(
    "token.json",
    SCOPES
)

service = build(
    "calendar",
    "v3",
    credentials=creds,
    cache_discovery=False
)

print("Google Calendar Connected")


@mcp.tool()
def list_events():
    """
    Get next 10 calendar events
    """

    events = service.events().list(
        calendarId="primary",
        maxResults=10,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    result = []

    for event in events.get("items", []):
        start = event.get("start", {}).get(
            "dateTime",
            event.get("start", {}).get("date", "No Date")
        )

        summary = event.get("summary", "No Title")

        result.append(
            f"{summary} | {start}"
        )

    return result


@mcp.tool()
def calendar_count():
    """
    Number of upcoming events
    """

    events = service.events().list(
        calendarId="primary",
        maxResults=100
    ).execute()

    return len(events.get("items", []))


print("About to start MCP server")
print("Started Calendar MCP")

if __name__ == "__main__":
    mcp.run()