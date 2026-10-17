# DealWear India — Affiliate Store

Aapka **fully automatic affiliate marketing website** ready hai! 🎉

---

## 📁 Files

| File | Purpose |
|------|---------|
| `index.html` | Main website |
| `products.json` | Products database (yahan se products load hote hain) |
| `manage_products.py` | Product add/remove karne ka tool |

---

## 🚀 GitHub Pages pe Deploy Kaise Karein (Free!)

### Step 1: GitHub pe Repository Banao
1. [github.com](https://github.com) pe jaao
2. **"New Repository"** click karo
3. Name rakho: `affiliate-store`
4. **Public** select karo ✅
5. **Create Repository** click karo

### Step 2: Files Upload Karo
1. Repository page pe **"uploading an existing file"** click karo
2. `index.html`, `products.json`, aur `manage_products.py` upload karo
3. **Commit changes** click karo

### Step 3: GitHub Pages ON Karo
1. Repository **Settings** → **Pages**
2. Source: **"Deploy from a branch"**
3. Branch: **main** / root
4. **Save** click karo

### Step 4: Website Live! 🎉
Aapki website ka URL hoga:
```
https://YOUR_USERNAME.github.io/affiliate-store
```
> ⚠️ `YOUR_USERNAME` ko apne GitHub username se replace karo — website mein bhi!

---

## ➕ Naya Product Add Karna (Mujhe Batao!)

Aap mujhe (AI ko) simply boldo:

> *"Ek nayi product add karo: naam XYZ, price ₹299, original ₹599, Meesho link: https://..."*

Main automatically `products.json` update kar dunga aur aapko updated file de dunga jo aap GitHub pe upload kar do.

Ya phir terminal se khud bhi kar sakte ho:
```bash
python3 manage_products.py add
python3 manage_products.py list
python3 manage_products.py seo
```

---

## 🔄 Automatic Features

| Feature | Kaise Kaam Karta Hai |
|---------|---------------------|
| **Product Display** | `products.json` se automatically load |
| **Search** | Real-time search — name, tags, category |
| **Filter** | Men / Women / Kids / Trending / New |
| **WhatsApp Share** | Auto-formatted message with affiliate link |
| **Telegram Share** | One-click share |
| **Twitter Share** | Auto hashtags ke saath |
| **SEO** | Meta tags, Open Graph, Structured data — sab auto |
| **Auto Refresh** | Har 5 minute mein products refresh |
| **Hashtag Copier** | Ek click mein hashtag copy |

---

## 📱 Promote Kaise Karein (Meri Help Lena!)

Mujhe batao aur main generate kar dunga:
- ✅ WhatsApp status caption
- ✅ Instagram post description + hashtags  
- ✅ Facebook post
- ✅ Telegram channel message
- ✅ Twitter/X thread

---

## 💰 Meesho Affiliate Join Karna

1. [meesho.com/affiliate](https://meesho.com) pe jaao
2. Affiliate program join karo (free hai)
3. Apne unique affiliate links products mein dalo
4. Har sale pe commission milega! 🎉

---

## 🔑 Apna Affiliate Link Kaise Lagaayein

`products.json` mein har product ke `"affiliate_link"` field mein apna **Meesho affiliate link** daalo.

Mujhe batao: *"Product ID 1 ka link update karo: https://meesho.com/..."*
