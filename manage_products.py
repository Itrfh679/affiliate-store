#!/usr/bin/env python3
"""
DealWear India - Auto Product Manager
=====================================
Yeh script automatically products.json update karta hai.
Aap mujhe batao (AI ko), aur main yeh run kar doonga.

Usage:
  python3 manage_products.py add      → Product add karo
  python3 manage_products.py list     → Sab products dekho
  python3 manage_products.py remove   → Product hatao (ID se)
  python3 manage_products.py trending → Trending products dekho
  python3 manage_products.py seo      → SEO suggestions generate karo
"""

import json
import sys
import os
from datetime import datetime

PRODUCTS_FILE  = os.path.join(os.path.dirname(__file__), "products.json")
AFFILIATE_ID   = "Itrfh679"

def load_products():
    with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_products(products):
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    print(f"✅ products.json updated! ({len(products)} products)")

def add_product():
    products = load_products()
    next_id = max(p["id"] for p in products) + 1 if products else 1
    
    print("\n🆕 NEW PRODUCT ADD KARO")
    print("=" * 40)
    name        = input("Product name (English): ").strip()
    name_hi     = input("Product name (Hindi, optional): ").strip()
    price       = int(input("Current price (₹): "))
    orig_price  = int(input("Original price (₹): "))
    category    = input("Category (men/women/kids): ").strip().lower()
    image       = input("Image URL: ").strip()
    fk_link     = input(f"Flipkart link (affid={AFFILIATE_ID} auto-lagega agar nahi hai): ").strip()
    mn_link     = input(f"Myntra link: ").strip()
    
    # Auto-inject affiliate ID into Flipkart link if missing
    if "affid=" not in fk_link:
        sep = "&" if "?" in fk_link else "?"
        fk_link = f"{fk_link}{sep}affid={AFFILIATE_ID}"
    
    rating      = float(input("Rating (1-5): "))
    reviews     = int(input("Review count: "))
    description = input("Short description: ").strip()
    tags_input  = input("Tags (comma separated, e.g. men,tshirt,casual): ").strip()
    tags        = [t.strip() for t in tags_input.split(",")]
    trending    = input("Trending? (y/n): ").lower() == 'y'
    is_new      = input("Mark as New? (y/n): ").lower() == 'y'
    
    discount = round((1 - price / orig_price) * 100)
    
    product = {
        "id": next_id,
        "name": name,
        "name_hi": name_hi or name,
        "price": price,
        "original_price": orig_price,
        "discount": discount,
        "category": category,
        "tags": tags,
        "image": image,
        "flipkart_link": fk_link,
        "myntra_link": mn_link,
        "rating": rating,
        "reviews": reviews,
        "description": description,
        "trending": trending,
        "new": is_new,
        "added_on": datetime.now().isoformat()
    }
    
    products.append(product)
    save_products(products)
    print(f"\n✅ Product added! ID: {next_id}, Discount: {discount}%")
    print(f"   🛒 Flipkart: {fk_link[:70]}...")
    print(f"   👗 Myntra  : {mn_link[:70]}...")

def list_products():
    products = load_products()
    print(f"\n📦 TOTAL PRODUCTS: {len(products)}")
    print("=" * 65)
    for p in products:
        trend = "🔥" if p.get("trending") else "  "
        new   = "✨" if p.get("new")      else "  "
        print(f"  [{p['id']}] {trend}{new} {p['name']}")
        print(f"       ₹{p['price']} (was ₹{p['original_price']}) | {p['discount']}% OFF | {p['category'].upper()}")
        fk = p.get('flipkart_link', p.get('affiliate_link', 'N/A'))
        mn = p.get('myntra_link', 'N/A')
        print(f"       🛒 Flipkart: {fk[:60]}...")
        print(f"       👗 Myntra  : {mn[:60]}...")
        print()

def remove_product():
    list_products()
    pid = int(input("Kaunsa product hatana hai? ID enter karo: "))
    products = load_products()
    original = len(products)
    products = [p for p in products if p["id"] != pid]
    if len(products) < original:
        save_products(products)
        print(f"✅ Product ID {pid} remove ho gaya!")
    else:
        print(f"❌ ID {pid} nahi mila.")

def show_trending():
    products = load_products()
    trending = [p for p in products if p.get("trending")]
    print(f"\n🔥 TRENDING PRODUCTS ({len(trending)})")
    print("=" * 40)
    for p in trending:
        print(f"  • {p['name']} — ₹{p['price']} ({p['discount']}% OFF)")

def generate_seo():
    products = load_products()
    all_tags = set()
    for p in products:
        all_tags.update(p.get("tags", []))
    
    categories = set(p["category"] for p in products)
    
    print("\n🔍 SEO KEYWORDS (Website ke liye):")
    print("=" * 50)
    
    keywords = []
    for tag in all_tags:
        keywords.extend([
            f"{tag} online india",
            f"buy {tag} cheap",
            f"best {tag} meesho",
            f"{tag} discount india",
        ])
    
    for cat in categories:
        keywords.extend([
            f"{cat} tshirt online",
            f"cheap {cat} shirts india",
            f"best {cat} clothing deals",
        ])
    
    print("Top Keywords:")
    for kw in sorted(set(keywords))[:20]:
        print(f"  📌 {kw}")
    
    print("\n📱 Hashtags for Social Media:")
    hashtags = [f"#{tag.replace(' ','')}" for tag in all_tags] + [
        "#MeeshoDeals", "#IndianFashion", "#OnlineShoppingIndia",
        "#AffordableClothing", "#FashionOnBudget", "#DealWearIndia"
    ]
    print("  " + " ".join(sorted(set(hashtags))))
    
    print("\n📝 WhatsApp Caption Template:")
    print("""
🛍️ *DealWear India* — Best Fashion Deals!
👕 Men, Women & Kids T-Shirts & Shirts
💰 Up to 60% OFF on Meesho!
🚚 Free Delivery available

👇 Shop Karo:
[YOUR WEBSITE LINK]

#MeeshoDeals #DealWearIndia #OnlineShopping
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    
    cmd = sys.argv[1].lower()
    
    if cmd == "add":
        add_product()
    elif cmd == "list":
        list_products()
    elif cmd == "remove":
        remove_product()
    elif cmd == "trending":
        show_trending()
    elif cmd == "seo":
        generate_seo()
    else:
        print(f"❌ Unknown command: {cmd}")
        print("Use: add / list / remove / trending / seo")
