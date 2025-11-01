# report_answer.py (one possible solution)
from collections import defaultdict
from orders_data import ORDERS

def group_totals_by_customer(orders):
    sums = defaultdict(float)
    for o in orders:
        name = f"{o['customer']['last']}, {o['customer']['first']}"
        sums[name] += float(o["total"])
    return dict(sums)

def top_customers(sums, n=3):
    # sort by total DESC, then name ASC
    return sorted(sums.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

def render_html(top_list):
    title = "Customer Spend — Top 3"
    items = "".join(f"<li>{name} — ${total}</li>" for name, total in top_list)
    return (
        "<!doctype html>"
        "<html><head><meta charset='utf-8'>"
        f"<title>{title}</title></head><body>"
        f"<h1>{title}</h1><ul>{items}</ul>"
        "</body></html>"
    )

if __name__ == "__main__":
    sums = group_totals_by_customer(ORDERS)
    top3 = top_customers(sums, n=3)
    html = render_html(top3)
    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote report.html")