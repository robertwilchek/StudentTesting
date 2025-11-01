
from collections import defaultdict
from orders_data import ORDERS  # reuse from Task 3

def group_totals_by_customer(orders):
    """
    Return a dict mapping 'Last, First' -> total_spent (float).
    TODO: implement
    """
    sums = defaultdict(float)
    # for o in orders: ... build key like "Last, First" and add float(o["total"]) to sums[key]
    return dict(sums)

def top_customers(sums, n=3):
    """
    Return a list of (name, total) sorted by total DESC, then name ASC.
    TODO: implement
    """
    # return sorted(sums.items(), key=..., reverse=...)[:n]
    return []

def render_html(top_list):
    """
    Return a minimal HTML string with a <ul> of 'Name — $Total'.
    TODO: implement (simple string builder is fine)
    """
    title = "Customer Spend — Top 3"
    # lines = [f"<li>{name} — ${total}</li>" for name, total in top_list]
    # html = f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title></head><body><h1>{title}</h1><ul>{''.join(lines)}</ul></body></html>"
    return ""

if __name__ == "__main__":
    sums = group_totals_by_customer(ORDERS)
    top3 = top_customers(sums, n=3)
    html = render_html(top3)
    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote report.html")