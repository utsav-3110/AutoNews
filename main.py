from news.get_news import get_news
from pdf.make_pdf import generate_news_pdf
from email_pdf.email_the_pdf import send_mail


articals = get_news()
report = generate_news_pdf(articals)
print(f"Report saved to: {report}")
send_mail(report)