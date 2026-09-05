# age= 21
# print(age,type(age))
# age="hello"
# print(age,type(age))

# age =3.14
# print(age,type(age))

# Age=(input('Enter age:'))
# print(Age,type(Age))

# age = 25
# if (age>18):
#     print("Yes")
# else:
#     print("No")

# def square(x):
#     return x*x

# numbers=[1,2,3,4,5,6,7]

# print(list(map(square,numbers)))

# a=int(input("Enter a number:"))
# print(a)
# print(a)#


import asyncio
import webbrowser
from datetime import datetime
from pathlib import Path

from agents import Agent, Runner, function_tool


@function_tool
def get_current_time() -> str:
    """Return the user's current local date and time."""
    return datetime.now().strftime("%A, %d %B %Y, %I:%M %p")


@function_tool
def save_note(note: str) -> str:
    """Save a short note requested by the user."""
    notes_file = Path("notes.txt")

    with notes_file.open("a", encoding="utf-8") as file:
        file.write(f"{datetime.now().isoformat()} — {note}\n")

    return "The note was saved successfully."


@function_tool
def open_website(site: str) -> str:
    """Open one approved website by name."""
    allowed_sites = {
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "google": "https://www.google.com",
        "wikipedia": "https://www.wikipedia.org",
    }

    requested_site = site.strip().lower()
    url = allowed_sites.get(requested_site)

    if not url:
        return f"{requested_site} is not on the approved website list."

    webbrowser.open(url)
    return f"Opened {requested_site}."


jarvis = Agent(
    name="JARVIS Mark I",
    model="gpt-5.6",
    instructions="""
You are JARVIS Mark I, a calm and capable personal desktop assistant.

Personality:
- Concise, intelligent, composed, and occasionally dryly humorous.
- Address the user respectfully without becoming theatrical.
- Do not imitate any actor or copyrighted character's exact voice.

Rules:
- Use tools when the user asks you to perform an available action.
- Never claim an action succeeded unless its tool returned success.
- Do not invent capabilities you do not possess.
- Ask for confirmation before destructive, financial, private,
  or externally visible actions.
- Keep ordinary answers short unless the user requests detail.
""",
    tools=[get_current_time, save_note, open_website],
)


async def main() -> None:
    history = []
    print("JARVIS Mark I online. Type 'exit' to shut down.")

    while True:
        user_message = input("\nYou: ").strip()

        if user_message.lower() in {"exit", "quit", "shutdown"}:
            print("JARVIS: Shutting down. Goodbye.")
            break

        history.append({"role": "user", "content": user_message})
        result = await Runner.run(jarvis, history)
        history = result.history

        print(f"JARVIS: {result.final_output}")


if __name__ == "__main__":
    asyncio.run(main())