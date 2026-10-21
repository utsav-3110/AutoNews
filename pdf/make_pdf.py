import requests
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet



def generate_news_pdf(news_items, filename="news_report.pdf", sources=[]):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for item in news_items:
        sources.append(item['source']['name'])
      
        story.append(Paragraph(f"<b>{item['title']}</b>", styles["Title"]))
        story.append(Spacer(1, 12))

     
        meta = f"Source: {item['source']['name']} | Author: {item['author'] or 'Unknown'} | Published: {item['publishedAt']}"
        story.append(Paragraph(meta, styles["Normal"]))
        story.append(Spacer(1, 12))

        if item.get("urlToImage"):
            try:
                response = requests.get(item["urlToImage"])
                if response.status_code == 200:
                    img_data = BytesIO(response.content)
                    img = Image(img_data, width=400, height=225)  
                    story.append(img)
                    story.append(Spacer(1, 12))
            except Exception as e:
                story.append(Paragraph(f"[Image not available: {e}]", styles["Normal"]))

       
        if item.get("description"):
            story.append(Paragraph(f"<i>{item['description']}</i>", styles["Normal"]))
            story.append(Spacer(1, 12))

     
        if item.get("content"):
            story.append(Paragraph(item['content'], styles["Normal"]))
            story.append(Spacer(1, 24))  

    # summary of every outlet used in this report
    story.append(Paragraph("Sources: " + ", ".join(sorted(set(sources))), styles["Normal"]))

    doc.build(story)


# generate_news_pdf(news_data, "latest_news.pdf")
