import webbrowser
import urllib.parse
import os
import subprocess

def execute_os_action(action_data):
    action = action_data.get("action")

    # ---- Browser actions ----
    if action == "open_chrome":
        webbrowser.open("https://www.google.com")
        return "Opening Chrome."

    if action == "open_youtube":
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    if action == "youtube_search":
        query = action_data.get("query", "")
        if query:
            url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
            webbrowser.open(url)
            return f"Searching {query} on YouTube."

    if action == "google_search":
        query = action_data.get("query", "")
        if query:
            url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            webbrowser.open(url)
            return f"Searching {query} on Google."

    # ---- Application actions ----
    if action == "open_app":
        app = action_data.get("app", "").lower()

        if app == "notepad":
            subprocess.Popen("notepad")
            return "Opening Notepad."

        if app == "calculator":
            subprocess.Popen("calc")
            return "Opening Calculator."

        if app == "file explorer":
            subprocess.Popen("explorer")
            return "Opening File Explorer."

        if app == "vscode":
            subprocess.Popen("code", shell=True)
            return "Opening Visual Studio Code."

        if app == "settings":
            subprocess.Popen("start ms-settings:", shell=True)
            return "Opening Settings."

        return "That application is not supported yet."

    return None
