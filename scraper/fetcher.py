import requests
import time
from datetime import datetime
from rich.console import Console
from rich.text import Text

console = Console()

def fetch_url(url, max_attempts=5, back_off=2):
    """
    Fetch a URL with retry logic and exponential backoff.
    """
    for attempt in range(1, max_attempts + 1):
        timestamp = datetime.now().isoformat(timespec="seconds")

        try:
            response = requests.get(url)
            response.raise_for_status()

            msg = Text(f"[{timestamp}] ✅ SUCCESS:", style="bold green")
            msg.append(f" Requested ", style="white")
            msg.append(url, style="cyan")
            msg.append(f" on attempt {attempt}.", style="white")
            console.print(msg)

            return response

        except requests.exceptions.ConnectionError:
            console.print(
                f"[{timestamp}] ❌ ERROR: Attempt {attempt} - Connection error. Check your internet connection.",
                style="bold red"
            )

        except requests.exceptions.HTTPError as e:
            console.print(
                f"[{timestamp}] ❌ ERROR: Attempt {attempt} - HTTP {e.response.status_code} for URL '{url}'.",
                style="bold red"
            )

        except requests.exceptions.RequestException as e:
            console.print(
                f"[{timestamp}] ❌ ERROR: Attempt {attempt} - Request failed for URL '{url}': {e}",
                style="bold red"
            )

        # Retry logic
        if attempt < max_attempts:
            retry = back_off * attempt
            console.print(
                f"[{timestamp}] ℹ INFO: Retrying in {retry} seconds...",
                style="cyan"
            )
            time.sleep(retry)
        else:
            console.print(
                f"[{timestamp}] 💥 FAILURE: All {max_attempts} attempts failed for URL '{url}'.",
                style="bold red"
            )
            return None
