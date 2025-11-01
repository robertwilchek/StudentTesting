def log_event(event, events=None):
    if events is None:
        events = []
    events.append(event)
    return events

# self‑test
if __name__ == "__main__":
    print(log_event("start"))  # ["start"]
    print(log_event("next"))   # ["next"]