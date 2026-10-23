# 📰 Automated Newsletter Generator

A Python script that fetches the latest news from [NewsAPI](https://newsapi.org/), converts them into a neat PDF report, and sends it directly to your email inbox using SMTP.  

---

## ✨ Features
- Fetches real-time top headlines from NewsAPI.
- Converts news into a PDF with `reportlab`.
- Sends the PDF to your email with `smtplib`.
- Simple setup — just add your API key, email, and app password directly in the script.

---

## ⚙️ Setup
1. Create a NewsAPI key at https://newsapi.org/ and put it in the script.
2. Create a Gmail app password for the sending account.
3. Run `python main.py` and answer the prompts.

---

## 🛠️ Requirements
Install dependencies:
```bash
pip install requests reportlab
