# logger.py (buggy behavior across calls)

def log_event(event, events=[]):
    events.append(event)
    return events

# self‑test
if __name__ == "__main__":
    print(log_event("start"))      # expect ["start"]
    print(log_event("next"))       # expect ["next"], NOT ["start", "next"]