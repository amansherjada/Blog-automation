import os
import re
import base64
import smtplib
import random
from email.mime.text import MIMEText
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import time
from urllib.parse import quote
import json

# Load environment variables
load_dotenv()

# Get the base URL from environment variable (for cloud deployment)
BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")

# Add logging to verify BASE_URL
print(f"🌐 BASE_URL is set to: {BASE_URL}")

REFERENCE_BLOG = """
Are Celebrities Really Using Hair Toppers? The Answer May Surprise You!
Have you ever wondered how celebrities always seem to have perfect, voluminous hair? Whether on the red carpet, in movies, or on social media, their hair looks flawless. The truth is, many of them aren't relying on genetics alone. The secret behind their luscious hairs? Hair toppers for thinning hair.
While most people associate hair extensions for women with length and volume, hair toppers specifically target thinning areas on the top and crown of the head. And guess what? Some of the most famous names in Hollywood and Bollywood swear by them. But why do they use them, and how do they achieve such natural results? Let's dive in.
Table of Contents
Why Celebs Use Hair Toppers
Science Behind Toppers for Thinning Hair
Secrets to a Seamless Celebrity Look
Can You Get Similar Results?
Achieving the Celebrity Look
Choosing the Best Toppers for Women
Why Do Celebrities Use Hair Toppers?
Many A-list celebrities, including actresses, models, and influencers, struggle with hair loss due to constant styling, heat exposure, and stress. Even though they have access to the best hair treatments, they often turn to human hair toppers to maintain a consistently flawless look.
Reasons Celebrities Opt for Hair Toppers:
Damage from Styling – Frequent blow-drying, coloring, and chemical treatments take a toll on natural hair.
Camera-Ready Volume – Thin or flat hair doesn't photograph well, and hair toppers for volume solve that instantly.
Age-Related Thinning – Many celebrities experience hair thinning as they age, just like millions of women worldwide.
Medical Conditions – Some stars suffer from conditions like alopecia or stress-related hair loss and use hair toppers for alopecia as a discreet solution.
Undetectable Enhancement – Today's seamless hair toppers blend so well with natural hair that even HD cameras can't detect them.
The Science Behind Hair Toppers for Thinning Hair
Hair toppers are a revolutionary solution for women experiencing hair thinning, hair loss, or reduced volume. They are designed to integrate seamlessly with natural hair, enhancing fullness while maintaining a lightweight and comfortable feel. Many women prefer them because they provide targeted coverage without requiring a complete transformation, making them a discreet yet effective option.
The technology behind modern hair toppers for thinning hair has advanced significantly. High-quality toppers are made with 100% human hair, ensuring a natural texture and realistic movement. The bases are crafted with materials that mimic the scalp, creating a flawless blend with existing hair. These toppers offer a non-invasive way to regain volume and confidence, making them a preferred choice for those who want an effortless, natural-looking solution.
Key Features of High-Quality Hair Toppers
100% Human Hair – The best hair toppers for women are crafted from real human hair, allowing them to be styled, washed, and treated just like natural hair.


Lightweight Construction – Lightweight hair toppers provide all-day comfort, ensuring they do not add excessive weight or strain to existing hair.


Scalp-Like Bases – Advanced silk hair toppers and skin hair toppers replicate the natural scalp, making the parting and hairline appear seamless.


Custom Fit – Custom hair toppers are designed to match different hair colors, textures, and densities, ensuring a perfect and undetectable blend.


By choosing the right hair topper, women can achieve a fuller, more youthful look while preserving the health of their natural hair. Whether the goal is to add volume, cover thinning areas, or boost confidence, a high-quality topper can make a remarkable difference.
How Celebrities Achieve a Seamless Look
The key to a natural-looking hair topper lies in how well it blends with natural hair. Celebrities achieve this through:
1. Choosing the Right Type
Silk Base Hair Toppers – Look ultra-realistic and give the appearance of a natural scalp.
Skin Hair Toppers – Blend well for a nearly invisible hairline.
Clip-In Hair Toppers – Ideal for quick, temporary volume without commitment.
2. Perfect Color Matching
Professional colorists ensure the best hair toppers for women match the root shade and undertones perfectly.
3. Expert Styling
Celebrity hair stylists trim and layer hair toppers for volume to integrate seamlessly with natural hair.
4. Secure Yet Comfortable Attachment
Using easy-to-wear hair toppers with hidden clips ensures a firm hold without discomfort.
Can You Get the Same Results?
Absolutely. The beauty of natural-looking hair toppers is that they are not just for celebrities. With the right product and a few styling tricks, you can achieve the same flawless look in your daily life. Today's human hair toppers are designed to blend seamlessly, offering a natural appearance that even up-close scrutiny won't reveal. Unlike full wigs, toppers integrate with your own hair, enhancing volume and covering thinning areas without looking artificial.
One of the biggest advantages of high-quality hair toppers is their scalp-like base, which makes them virtually undetectable. Options like silk hair toppers and skin hair toppers mimic the natural scalp, ensuring that your parting looks real. Many worry about comfort, but modern lightweight hair toppers are designed for all-day wear without causing strain or irritation. With proper attachment methods, such as clip-in hair toppers, you can confidently go about your day without worrying about shifting or discomfort.
Whether you have crown thinning, general hair loss, or alopecia, the right hair topper can help you reclaim your confidence. Celebrities rely on expert stylists, but with a little practice, you can achieve a salon-worthy look at home. Choosing a topper that matches your hair color and texture, along with some light styling, can give you the same polished, voluminous hair seen on the red carpet.
How to Achieve a Celebrity-Like Look with Hair Toppers
Invest in a High-Quality Hair Topper: The key to a seamless look is choosing 100% human hair toppers, as they blend better and allow for heat styling.
Get a Professional Color Match: A perfect match with your natural hair color ensures that the topper looks undetectable.
Customize Your Topper: Just like celebrities, you can take your hair topper to a stylist for a custom cut and layering to blend with your hair.
Use the Right Attachment Method: Ensure a secure and comfortable fit with clip-in hair toppers or tape-in hair toppers, depending on your lifestyle.
Style Like a Pro: Blow-drying, curling, or straightening your topper along with your natural hair helps in achieving a natural, voluminous look.
Regular Maintenance: Keeping your topper clean, conditioned, and tangle-free will help maintain its natural shine and softness for long-term use.
With the right approach, anyone can achieve that red-carpet-ready hair, boosting confidence and enhancing their overall appearance.
Choosing the Best Hair Toppers for Women
If you are struggling with thinning hair and looking for a confidence-boosting solution, investing in a high-quality hair topper can be life-changing. Here are the top factors to consider:
1. Hair Type
100% Human Hair – Offers the most natural look and can be heat-styled.
Synthetic Hair – Budget-friendly but lacks a realistic feel.
2. Base Construction
Silk Hair Toppers – Give a scalp-like illusion and look completely natural.
Skin Hair Toppers – Perfect for creating an undetectable hairline.
3. Attachment Method
Clip-In Hair Toppers – Easy to wear and remove daily.
Tape-In Hair Toppers – More secure for long-term use.
4. Volume Needs
Hair toppers for crown thinning – Ideal for localized volume at the crown.
Hair toppers for alopecia – Designed for widespread thinning.
5. Lifestyle Compatibility
Easy-to-wear hair toppers – Perfect for daily use without hassle.
Custom hair toppers – Designed for those who want a tailored fit.
Conclusion: Embrace Confidence with Natural-Looking Hair Toppers
Celebrities have long known the power of hair toppers for thinning hair, and now, this secret is available to everyone. Whether you're looking for clip-in hair toppers for a quick fix or custom hair toppers for a long-term solution, there are options for every woman.
Looking your best isn't just about vanity—it's about confidence. With natural-looking hair toppers, you can step out feeling self-assured, knowing your hair looks just as glamorous as any celebrities. Why wait? Explore the best options and rediscover the beauty of full, voluminous hair today.


"""

# Retrieve credentials from environment variables
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "service_account.json")
DOC_ID = os.getenv("GOOGLE_DOC_ID_TOPIC")
BLOG_PROMPT_DOC_ID = os.getenv("GOOGLE_DOC_BLOG_PROMPT_DOC_ID")
SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FROM_EMAIL = os.getenv("EMAIL_USERNAME")       
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
DESIGNER_EMAIL = os.getenv("DESIGNER_EMAIL")
HEAD_EMAIL = os.getenv("HEAD_EMAIL")
GAVARI_EMAIL = os.getenv("GAVARI_EMAIL")
APPROVED_BLOGS_FOLDER_ID = os.getenv("APPROVED_BLOGS_FOLDER_ID")
GIVEAWAY_DOC_ID = os.getenv("GIVEAWAY_DOC_ID")
RESTRICTED_DOC_ID = os.getenv("RESTRICTED_DOC_ID")
cta_agent = os.getenv("CTA_SHEET_ID")
PRODUCT_SHEET_ID = os.getenv("PRODUCT_SHEET_ID")

# Handle service account credentials with better error handling
try:
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON"):
        # If credentials are provided as JSON string (for other cloud platforms)
        print("🔐 Using GOOGLE_APPLICATION_CREDENTIALS_JSON from environment")
        creds_json = json.loads(os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON"))
        credentials = service_account.Credentials.from_service_account_info(
            creds_json,
            scopes=[
                "https://www.googleapis.com/auth/documents.readonly",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/spreadsheets.readonly"
            ]
        )
    elif os.path.exists("/secrets/ahl-api"):
        # Cloud Run mounts the secret as a file
        print("🔐 Using mounted secret file at /secrets/ahl-api")
        with open("/secrets/ahl-api", 'r') as f:
            creds_json = json.load(f)
        credentials = service_account.Credentials.from_service_account_info(
            creds_json,
            scopes=[
                "https://www.googleapis.com/auth/documents.readonly",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/spreadsheets.readonly"
            ]
        )
    elif os.getenv("GOOGLE_APPLICATION_CREDENTIALS") and os.path.exists(os.getenv("GOOGLE_APPLICATION_CREDENTIALS")):
        # Use the path specified in GOOGLE_APPLICATION_CREDENTIALS
        print(f"🔐 Using service account file at: {os.getenv('GOOGLE_APPLICATION_CREDENTIALS')}")
        SCOPES = [
            "https://www.googleapis.com/auth/documents.readonly",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/spreadsheets.readonly"
        ]
        credentials = service_account.Credentials.from_service_account_file(
            os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), scopes=SCOPES
        )
    else:
        # Use file-based credentials (for local development)
        print(f"🔐 Using default service account file: {SERVICE_ACCOUNT_FILE}")
        SCOPES = [
            "https://www.googleapis.com/auth/documents.readonly",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/spreadsheets.readonly"
        ]
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
    
    print("✅ Service account credentials loaded successfully")
    
except Exception as e:
    print(f"❌ Error loading service account credentials: {e}")
    print(f"Available environment variables: {list(os.environ.keys())}")
    raise

# Build Google API services
try:
    docs_service = build("docs", "v1", credentials=credentials)
    drive_service = build("drive", "v3", credentials=credentials)
    sheets_service = build("sheets", "v4", credentials=credentials)
    print("✅ Google API services initialized successfully")
except Exception as e:
    print(f"❌ Error initializing Google API services: {e}")
    raise

KEYWORD_SHEETS = {
    "CLIP IN HAIR EXTENSIONS": "1Nf1WjsXyPjGP3xlxOe_lYmC0gwmmoeJPO8P3WHWjRA4",
    "WIGS": "1zEgeYEJwqj4GvSkJeSGY_bOOf2HVBhAzeMLa-XP3Jxk",
    "SILK HAIR TOPPER": "1GI5ZRMegwqSx5RBjPe0WkEEOnEMeLbGazeyMNhSu7hs",
    "SKIN HAIR TOPPER": "1IvZn_OMNaOkJy4F_iYY7KOhMELr3Vta43Vx49d-ezn4",
    "HAIR TOPPERS": "1COFbm3zzdbkQsSi9WlLHwTvcbR1BhlspjDg1hM4FlRQ",
    "GLUE/KERATIN BOND HAIR EXTENSIONS": "1w-5O9BwCpzegMZkgBQbcEHgQ7tgBG560EFO4CgPDkqQ",
    "TAPE-IN HAIR EXTENSIONS": "1JaVZBMd355hvSdiSTpwD0irJaMepsuMWvUB-FwDEwNM",
    "Permanent Hair Extensions": "1_oTkBV2qCRyFKYSIbAHyWM4nPmHVcINGhmAZIej4-pE",
    "MICRO RING HAIR EXTENSIONS": "1iMwZ4VnK8VSYBBckTee5hvtkrWWrJrzfkd-8Brg3hds"
}

TARGET_AUDIENCE_DOCS = {
    "CLIP IN HAIR EXTENSIONS": "1Ly3vyL5LQIt_tidQ7KrmY5_nZNCDK9zxNK-tloGqIVQ",
    "WIGS": "1wkhdT3tpKNNWM4oVmuAaXhNh1Hw243LrEBxuXdrGwKc",
    "SILK HAIR TOPPER": "1KP96hqO8rhnWq0K5t33rF5B6Vdv9VGk5Pc4_Hw8NoI4",
    "SKIN HAIR TOPPER": "1K6O0ocZWndsG9eC3A1hbpPS3hLJQrpwyFIbHuAUraQI",
    "HAIR TOPPERS": "1k1dbAKRlPwqfLSVTIIzeASXr458RB8-fx7GvwdiM8Bg",
    "GLUE/KERATIN BOND HAIR EXTENSIONS": "1L4boRvpjbz1INQUQERf8mvFe7QKo5156BdrKPNPdi14",
    "TAPE-IN HAIR EXTENSIONS": "1R9MfHLR_GwjOzkF8hxwxNV0VVLt3DlRp5NmbM049QZw",
    "PERMANENT HAIR EXTENSIONS": "1SNX6Jamb2PDGUTj1osBVx0gyp0ODqWYu3RXF4vTmtAE",
    "MICRO RING HAIR EXTENSIONS": "12r4O5JFXDaAoH6ZWFzZLNb1FGzLVpYLtgJgGq153wiQ"
}

ALL_CATEGORIES = [k.replace('-', ' ').replace('_', ' ').lower() for k in KEYWORD_SHEETS.keys()]

app = Flask(__name__)
CORS(app)  # Enable CORS for cloud deployment

# Add health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "base_url": BASE_URL,
        "service": "blog-automation",
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }), 200

# Add root endpoint
@app.route("/", methods=["GET"])
def root():
    return jsonify({
        "service": "Blog Automation System",
        "status": "running",
        "endpoints": {
            "health": "/health",
            "approve": "/approve?topic=<topic>",
            "reject": "/reject?topic=<topic>",
            "approve-gavari": "/approve-gavari?topic=<topic>&category=<category>&keyword=<keyword>",
            "reject-gavari": "/reject-gavari?topic=<topic>&category=<category>&keyword=<keyword>"
        }
    }), 200

class PromptAgent:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.docs_service = docs_service

    def fetch_prompt(self):
        try:
            document = self.docs_service.documents().get(documentId=self.doc_id).execute()
            content = document.get("body", {}).get("content", [])
            prompt_text = ""
            for element in content:
                paragraph = element.get("paragraph")
                if paragraph:
                    for elem in paragraph.get("elements", []):
                        text_run = elem.get("textRun")
                        if text_run:
                            prompt_text += text_run.get("content", "")
            return prompt_text.strip()
        except Exception as e:
            print(f"❌ Error fetching prompt: {e}")
            return ""

class AudienceAgent:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.docs_service = docs_service

    def fetch_audience_text(self):
        try:
            document = self.docs_service.documents().get(documentId=self.doc_id).execute()
            content = document.get("body", {}).get("content", [])
            audience_text = ""
            for element in content:
                paragraph = element.get("paragraph")
                if paragraph:
                    for elem in paragraph.get("elements", []):
                        text_run = elem.get("textRun")
                        if text_run:
                            audience_text += text_run.get("content", "")
            return audience_text.strip()
        except Exception as e:
            print(f"❌ Error fetching audience text: {e}")
            return ""

class KeywordAgent:
    def __init__(self):
        self.sheets_service = sheets_service

    def get_random_keyword(self):
        categories = list(KEYWORD_SHEETS.items())
        random.shuffle(categories)
        for matched_category, sheet_id in categories:
            try:
                result = self.sheets_service.spreadsheets().values().get(
                    spreadsheetId=sheet_id,
                    range="A1:A"
                ).execute()
                values = result.get("values", [])
                if not values:
                    continue
                keyword = random.choice(values)[0]
                top_keywords = [v[0] for v in values[:5] if v]
                print(f"🔑 Random Keyword from '{matched_category}': {keyword}")
                return keyword, matched_category, top_keywords
            except Exception as e:
                print(f"⚠️ Skipping '{matched_category}' due to error: {e}")
        return None, None, []

class ProductSheetAgent:
    def __init__(self, sheet_id):
        self.sheet_id = sheet_id
        self.sheets_service = sheets_service

    def fetch_product_text(self, category):
        try:
            result = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=self.sheet_id,
                range="Sheet1!A:D"
            ).execute()

            rows = result.get("values", [])
            category = category.upper().strip()

            for row in rows[1:]:
                if row and row[0].strip().upper() == category:
                    return row[2]
        except Exception as e:
            print(f"⚠️ Could not fetch product info for category: {category} - {e}")
        return ""

class TopicAgent:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def clean_title(self, title):
        cleaned = re.sub(r"^\s*\d+\s*[\w\-]*\s*", "", title, count=1).strip()
        return cleaned[0].upper() + cleaned[1:] if cleaned else title

    def generate_topic(self, prompt, keyword, category):
        try:
            doc_id_audience = TARGET_AUDIENCE_DOCS.get(category.upper()) if category else None
            audience_text = ""
            product_text = ""

            if doc_id_audience:
                audience_text = AudienceAgent(doc_id_audience).fetch_audience_text()
            
            product_agent = ProductSheetAgent(PRODUCT_SHEET_ID)
            product_text = product_agent.fetch_product_text(category)

            combined_prompt = f"""{prompt}

    Target Audience Insights:
    {audience_text}

    Product Details:
    {product_text}

    Now based on the keyword: '{keyword}', suggest ONE blog topic title that is catchy, curiosity-driven, and clearly relevant to this keyword. Do not start with a number."""

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a blog expert. Generate a catchy blog topic title."},
                    {"role": "user", "content": combined_prompt}
                ],
                max_tokens=25,
                temperature=0.7,
                n=1
            )
            return self.clean_title(response.choices[0].message.content.strip())
        except Exception as e:
            print(f"❌ Error generating topic: {e}")
            return f"Error generating topic for {keyword}"

class GiveawayAgent:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.docs_service = docs_service

    def fetch_all_giveaways(self):
        try:
            document = self.docs_service.documents().get(documentId=self.doc_id).execute()
            content = document.get("body", {}).get("content", [])
            giveaways = []

            for element in content:
                paragraph = element.get("paragraph")
                if paragraph:
                    text = ""
                    for elem in paragraph.get("elements", []):
                        text_run = elem.get("textRun")
                        if text_run:
                            text += text_run.get("content", "")
                    text = text.strip()
                    if text:
                        giveaways.append(text)
            return giveaways
        except Exception as e:
            print(f"❌ Error fetching giveaways: {e}")
            return []

    def select_relevant_giveaway(self, keyword, category=None):
        from difflib import SequenceMatcher

        all_giveaways = self.fetch_all_giveaways()
        if not all_giveaways:
            return ""
        
        keyword = keyword.lower()
        category = (category or "").lower()

        for line in all_giveaways:
            if category in line.lower():
                print(f"🎯 Matched category-based giveaway for: {category}")
                return line

        for line in all_giveaways:
            if keyword in line.lower():
                print("✅ Exact match giveaway selected")
                return line

        best_match = None
        best_score = 0
        for line in all_giveaways:
            score = SequenceMatcher(None, keyword, line.lower()).ratio()
            if score > best_score:
                best_score = score
                best_match = line
        if best_score > 0.3:
            print(f"🤏 Fuzzy match giveaway selected (score: {best_score:.2f})")
            return best_match

        for line in all_giveaways:
            if "+91 9967123333" in line:
                print("📞 Fallback line with phone number used")
                return line

        return random.choice(all_giveaways) if all_giveaways else ""

class CTAAgent:
    def __init__(self, sheet_id):
        self.sheet_id = sheet_id
        self.sheets_service = sheets_service

    def fetch_all_ctas(self):
        try:
            result = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=self.sheet_id,
                range="Sheet1"
            ).execute()
            rows = result.get("values", [])
            return rows
        except Exception as e:
            print(f"❌ Error fetching CTAs: {e}")
            return []

    def select_cta(self, category=None):
        category = (category or "").lower().strip()
        rows = self.fetch_all_ctas()

        if not rows:
            return "👉 [Fill this quick form to get personalized guidance on your hair journey.](https://forms.gle/xdzYyJK5cH7HKEHW7)"

        headers = rows[0]
        category_col = 0
        option_cols = list(range(1, len(headers)))

        matched_row = None
        for row in rows[1:]:
            if row and row[0].lower().strip() == category:
                matched_row = row
                break

        if not matched_row:
            for row in rows[1:]:
                if row and row[0].lower().strip() == "default":
                    matched_row = row
                    break

        if not matched_row:
            return "👉 [Fill this quick form to get personalized guidance on your hair journey.](https://forms.gle/xdzYyJK5cH7HKEHW7)"

        options = [matched_row[i] for i in option_cols if i < len(matched_row) and matched_row[i].strip()]
        if options:
            selected_cta = random.choice(options).strip()

            if "forms.gle" not in selected_cta:
                selected_cta += "\n\n👉 [Fill out the form and get matched.](https://forms.gle/xdzYyJK5cH7HKEHW7)"

            return selected_cta

        return "👉 [Fill this quick form to get personalized guidance on your hair journey.](https://forms.gle/xdzYyJK5cH7HKEHW7)"

class BlogWriterAgent:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.docs_service = docs_service

    def fetch_blog_prompt(self):
        try:
            document = self.docs_service.documents().get(documentId=self.doc_id).execute()
            content = document.get("body", {}).get("content", [])
            prompt_text = ""
            for element in content:
                paragraph = element.get("paragraph")
                if paragraph:
                    for elem in paragraph.get("elements", []):
                        text_run = elem.get("textRun")
                        if text_run:
                            prompt_text += text_run.get("content", "")
            return prompt_text.strip()
        except Exception as e:
            print(f"❌ Error fetching blog prompt: {e}")
            return ""

    def generate_blog(self, title, keyword, extra_keywords, category=None):
        try:
            prompt = self.fetch_blog_prompt()
            audience_text = ""
            doc_id_audience = TARGET_AUDIENCE_DOCS.get(category.upper()) if category else None
            if doc_id_audience:
                audience_text = AudienceAgent(doc_id_audience).fetch_audience_text()

            product_text = ""
            rules_text = ""
            if category:
                product_text = ProductSheetAgent(PRODUCT_SHEET_ID).fetch_product_text(category)
                rules_text = restricted_agent.fetch_rules_as_text()

            final_prompt = f"""{prompt}

    Primary Keyword: {keyword}
    Secondary Keywords: {', '.join(extra_keywords)}
    Target Audience Insights: {audience_text}
    Product Details: {product_text}
    Content Writing Rules (Must be Followed): 
    {rules_text}

    Below is a reference blog. Your output should follow this same structure, tone, and style:

    {REFERENCE_BLOG}

---

Now write a complete blog on the topic STRICTLY with a minimum of **2000 words AND 11000 characters**.

Follow these important rules:

1. DO NOT write customer persona, target audience breakdown, or market research.
2. DO NOT include "Introduction" or "Conclusion" in the Table of Contents.
3. First write a strong INTRODUCTION (2–3 paragraphs) that emotionally connects with the reader and introduces the topic.
4. AFTER the introduction, give the Table of Contents.
5. In the Table of Contents, use **short and crisp titles** (max 5–6 words). For example, use "Choosing the Right Wig" instead of "How to Choose the Perfect Wig for Your Style."

6. BUT — in the actual blog sections, use **full and detailed section headers** like "How to Choose the Perfect Wig for Your Style."

(So the TOC is skimmable, but the blog itself stays rich.)

IMPORTANT:
- After the Table of Contents, do NOT reuse the short TOC titles in the blog.
- Instead, for each section in the blog, **write a longer, expanded version** of the TOC title.
  Example:
  - TOC: "Caring for Your Wig"
  - Blog Section Header: "How to Properly Care for Your Full Lace Front Wig to Make It Last"

This ensures short TOC + long SEO-friendly blog headers.

7. Format section headers using the **Section Title** format (bold with asterisks).
8. Each sub-section must have **at least 2–3 paragraphs**, go deep, and feel rich — no bullet-only content.
9. Use storytelling, examples, and light persuasive language.
10. Wherever useful, include **bullet points** using a dash (-) at the start of each point.
11. For numbered lists, use numbers followed by a period (1., 2., etc.).
12. DO NOT include a call-to-action section at the end of the blog. Custom CTAs will be added separately after generation.

"""

            for _ in range(3):
                response = OpenAI(api_key=OPENAI_API_KEY).chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You're a professional blog writer. "
                                "Use the Product Details section inside the blog where relevant to explain features, benefits, or help the user make decisions.\n\n"
                                f"{rules_text}"
                            )
                        },
                        {"role": "user", "content": final_prompt}
                    ],
                    max_tokens=4000,
                    temperature=0.7,
                )
                blog_content = response.choices[0].message.content.strip()
                if len(blog_content) >= 9000 and len(blog_content.split()) >= 1500:
                    break
                else:
                    print(f"⚠️ Blog too short: {len(blog_content.split())} words, {len(blog_content)} characters. Retrying...")

            giveaway_line = giveaway_agent.select_relevant_giveaway(keyword, category)
            if giveaway_line:
                blog_content += f"\n\n{giveaway_line.strip()}"
            
            normalized_category = category.replace("-", " ").replace("_", " ").lower() if category else None
            cta_line = cta_agent.select_cta(normalized_category)

            if cta_line:
                blog_content += f"\n{cta_line.strip()}"
            
            blog_content = restricted_agent.filter_content(blog_content)

            return blog_content
        except Exception as e:
            print(f"❌ Error generating blog: {e}")
            return f"Error generating blog content: {str(e)}"

class GavariAgent:
    def __init__(self, docs_service, drive_service, email_agent):
        self.docs_service = docs_service
        self.drive_service = drive_service
        self.email_agent = email_agent

    def send_blog_to_gavari(self, title, content, keyword, category):
        try:
            doc_metadata = {'title': title}
            doc = self.docs_service.documents().create(body=doc_metadata).execute()
            doc_id = doc['documentId']

            requests = []
        
            requests.append({
                'insertText': {
                    'location': {'index': 1},
                    'text': title + "\n\n"
                }
            })
        
            requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': 1,
                        'endIndex': len(title) + 1
                    },
                    'paragraphStyle': {
                        'namedStyleType': 'HEADING_1'
                    },
                    'fields': 'namedStyleType'
                }
            })
        
            lines = content.split('\n')
            current_index = len(title) + 2
        
            for line in lines:
                line_text = line + "\n"
                line_length = len(line_text)
            
                requests.append({
                    'insertText': {
                        'location': {'index': current_index},
                        'text': line_text
                    }
                })
            
                if line.startswith('**') and line.endswith('**'):
                    header_text = line.strip('*').strip()
                    requests.append({
                        'updateParagraphStyle': {
                            'range': {
                                'startIndex': current_index,
                                'endIndex': current_index + line_length - 1
                            },
                            'paragraphStyle': {
                                'namedStyleType': 'HEADING_2'
                            },
                            'fields': 'namedStyleType'
                        }
                    })
            
                elif line.strip().startswith('- '):
                    requests.append({
                        'createParagraphBullets': {
                            'range': {
                                'startIndex': current_index,
                                'endIndex': current_index + line_length - 1
                            },
                            'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'

                        }
                    })
            
                elif re.match(r'^\d+\.\s', line.strip()):
                    requests.append({
                        'createParagraphBullets': {
                            'range': {
                                'startIndex': current_index,
                                'endIndex': current_index + line_length - 1
                            },
                            'bulletPreset': 'NUMBERED_DECIMAL_ALPHA_ROMAN'

                        }
                    })
            
                current_index += line_length
        
            self.docs_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()

            self.drive_service.permissions().create(
                fileId=doc_id,
                body={
                    'type': 'user',
                    'role': 'writer',
                    'emailAddress': GAVARI_EMAIL
                },
                fields='id'
            ).execute()

            subject = f"Approved Blog for Review: {title}"
            encoded_title = quote(title.replace('"', ''))
            encoded_keyword = quote(keyword)
            encoded_category = quote(category)

            approval_link = f"{BASE_URL}/approve-gavari?topic={encoded_title}&category={encoded_category}&keyword={encoded_keyword}"
            reject_link = f"{BASE_URL}/reject-gavari?topic={encoded_title}&category={encoded_category}&keyword={encoded_keyword}"

            message_body = f"""
            <p>Hey Gauri Mam,</p>
            <p>A new blog has been generated and is ready for your review.</p>
            <p><strong>Title:</strong> {title}</p>
            <p><strong>Keyword:</strong> {keyword}</p>
            <p><a href="https://docs.google.com/document/d/{doc_id}">Click here to view/edit the blog</a></p>
            <p>You have edit and view access.</p>
            <p>Kindly approve or reject the blog:</p>
            <a href="{approval_link}" style="padding:10px;background:#27ae60;color:white;text-decoration:none;margin-right:10px;">✅ Approve</a>
            <a href="{reject_link}" style="padding:10px;background:#c0392b;color:white;text-decoration:none;">❌ Reject and Regenerate</a>

            <p>Thanks,<br>AutoBot 💡</p>
            """

            self.email_agent.send_email(GAVARI_EMAIL, subject, message_body)
            print(f"✅ Blog sent to Gavari: {title}")
        except Exception as e:
            print(f"❌ Error sending blog to Gavari: {e}")
            raise

class SheetAgent:
    def __init__(self):
        self.sheets_service = sheets_service

    def get_all_topics(self):
        try:
            sheet = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=SHEET_ID,
                range="Sheet1!A:A"
            ).execute()
            return set(row[0].strip().lower() for row in sheet.get("values", []) if row)
        except Exception as e:
            print(f"❌ Error getting all topics: {e}")
            return set()

    def topic_exists(self, topic):
        return topic.strip().lower() in self.get_all_topics()

    def update_blog_status(self, topic, new_status):
        try:
            sheet = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=SHEET_ID,
                range="Sheet1!A:E"
            ).execute()
            rows = sheet.get("values", [])
            for i, row in enumerate(rows):
                if row and row[0].strip().lower() == topic.strip().lower():
                    cell_range = f"Sheet1!D{i+1}"
                    self.sheets_service.spreadsheets().values().update(
                        spreadsheetId=SHEET_ID,
                        range=cell_range,
                        valueInputOption="RAW",
                        body={"values": [[new_status]]}
                    ).execute()
                    print(f"🔄 Updated status of '{topic}' to '{new_status}'")
                    break
        except Exception as e:
            print(f"❌ Error updating blog status: {e}")

    def add_blog_entry(self, topic, keyword, category, extra_keywords, status="Generated"):
        try:
            if self.topic_exists(topic):
                print(f"🚫 Skipping duplicate topic: {topic}")
                return False

            values = [[
                topic,
                keyword,
                category,
                status,
                str(__import__('datetime').datetime.now().date()),
                "Generated",
                ", ".join(extra_keywords)
            ]]
            body = {"values": values}
            self.sheets_service.spreadsheets().values().append(
                spreadsheetId=SHEET_ID,
                range="Sheet1!A:G",
                valueInputOption="RAW",
                body=body
            ).execute()
            print(f"✅ Blog entry added to sheet: {topic}")
            return True
        except Exception as e:
            print(f"❌ Error adding blog entry: {e}")
            return False

    def get_topic_data(self, topic):
        try:
            result = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=SHEET_ID,
                range="Sheet1!A:G"
            ).execute()
            rows = result.get("values", [])
            for row in rows:
                if row and row[0].strip().lower() == topic.strip().lower():
                    keyword = row[1] if len(row) > 1 else ""
                    category = row[2] if len(row) > 2 else ""
                    extra_keywords = row[6].split(",") if len(row) > 6 and row[6] else []
                    return keyword, category, extra_keywords
            return None, None, []
        except Exception as e:
            print(f"❌ Error getting topic data: {e}")
            return None, None, []

class EmailAgent:
    def send_email(self, to_email, subject, message_text):
        msg = MIMEText(message_text, "html")
        msg["Subject"] = subject
        msg["From"] = FROM_EMAIL
        msg["To"] = to_email

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(FROM_EMAIL, EMAIL_APP_PASSWORD)
                server.sendmail(FROM_EMAIL, to_email, msg.as_string())
            print(f"✅ Email sent to {to_email}")
        except Exception as e:
            print("❌ Failed to send email:", str(e))

class DriveAgent:
    def __init__(self, drive_service, parent_folder_id):
        self.drive_service = drive_service
        self.parent_folder_id = parent_folder_id

    def create_blog_folder(self, blog_title):
        try:
            folder_metadata = {
                'name': blog_title,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [self.parent_folder_id]
            }
            folder = self.drive_service.files().create(body=folder_metadata, fields='id').execute()
            return folder.get('id')
        except Exception as e:
            print(f"❌ Error creating blog folder: {e}")
            return None

    def move_doc_to_folder(self, doc_id, folder_id):
        try:
            self.drive_service.files().update(
                fileId=doc_id,
                addParents=folder_id,
                removeParents='root',
                fields='id, parents'
            ).execute()
        except Exception as e:
            print(f"❌ Error moving doc to folder: {e}")

    def get_doc_id_by_title(self, title):
        try:
            query = f"name contains '{title}' and mimeType = 'application/vnd.google-apps.document'"
            response = self.drive_service.files().list(q=query, fields="files(id, name)").execute()
            files = response.get('files', [])
            if files:
                return files[0]['id']
            return None
        except Exception as e:
            print(f"❌ Error getting doc by title: {e}")
            return None

class RestrictedWordAgent:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.docs_service = docs_service

    def fetch_rules_as_text(self):
        try:
            document = self.docs_service.documents().get(documentId=self.doc_id).execute()
            content = document.get("body", {}).get("content", [])
            rules = []

            for element in content:
                paragraph = element.get("paragraph")
                if paragraph:
                    rule_text = ""
                    for elem in paragraph.get("elements", []):
                        text_run = elem.get("textRun")
                        if text_run:
                            rule_text += text_run.get("content", "")
                    rule_text = rule_text.strip()
                    if rule_text:
                        rules.append(rule_text)
            return "\n".join(rules).strip()
        except Exception as e:
            print(f"❌ Error fetching rules: {e}")
            return ""
    
    def filter_content(self, content):
        try:
            rules_text = self.fetch_rules_as_text()
            if not rules_text:
                return content

            patterns = [line.strip() for line in rules_text.split('\n') if line.strip()]
        
            for pattern in patterns:
                try:
                    content = re.sub(pattern, '', content, flags=re.IGNORECASE)
                except re.error as e:
                    print(f"⚠️ Invalid regex pattern: {pattern} – {e}")
        
            return content
        except Exception as e:
            print(f"❌ Error filtering content: {e}")
            return content

# Initialize agents
try:
    sheet_agent = SheetAgent()
    email_agent = EmailAgent()
    blog_writer = BlogWriterAgent(BLOG_PROMPT_DOC_ID)
    gavari_agent = GavariAgent(docs_service, drive_service, email_agent)
    drive_agent = DriveAgent(drive_service, APPROVED_BLOGS_FOLDER_ID)
    giveaway_agent = GiveawayAgent(GIVEAWAY_DOC_ID)
    restricted_agent = RestrictedWordAgent(RESTRICTED_DOC_ID)
    cta_agent = CTAAgent(cta_agent)
    print("✅ All agents initialized successfully")
except Exception as e:
    print(f"❌ Error initializing agents: {e}")
    raise

topic_context = {}

@app.route("/approve", methods=["GET"])
def approve_topic():
    try:
        topic = request.args.get("topic")
        if not topic:
            return "Missing topic", 400

        keyword, category, extra_keywords = sheet_agent.get_topic_data(topic)

        if not keyword or not category:
            return "Missing keyword or category in sheet", 400

        extra_keywords = topic_context.get(topic, {}).get("extra_keywords", extra_keywords)
        blog_content = blog_writer.generate_blog(topic, keyword, extra_keywords, category)

        gavari_agent.send_blog_to_gavari(topic, blog_content, keyword, category)

        sheet_agent.update_blog_status(topic, "Approved")

        subject = "Approved Blog Topic - Proceed with Thumbnail"
        body = f"""
        <p>The following blog topic has been approved:</p>
        <h3>{topic}</h3>
        <p><strong>Category:</strong> {category}</p>
        <p>Please check the tracker sheet for details.</p>
        <p>💾 Shared Google Drive Folder (for graphics):<br>
        <a href="https://drive.google.com/drive/folders/1pmHyrIZsXO7TpcvUnRsAoMZSEX1LXgXH?usp=sharing" target="_blank">
        https://drive.google.com/drive/folders/1pmHyrIZsXO7TpcvUnRsAoMZSEX1LXgXH?usp=sharing
        </a></p>
        """

        email_agent.send_email(DESIGNER_EMAIL, subject, body)

        return f"✅ Blog approved and email sent to designer for topic: {topic}"
    except Exception as e:
        print(f"❌ Error in approve_topic: {e}")
        return f"Error approving topic: {str(e)}", 500

@app.route("/reject", methods=["GET"])
def reject_topic():
    try:
        topic = request.args.get("topic")
        if not topic:
            return "Missing topic", 400

        sheet = sheet_agent.sheets_service.spreadsheets().values().get(
            spreadsheetId=SHEET_ID,
            range="Sheet1!A:E"
        ).execute()
        rows = sheet.get("values", [])
        for i, row in enumerate(rows):
            if row and row[0] == topic:
                sheet_agent.sheets_service.spreadsheets().values().clear(
                    spreadsheetId=SHEET_ID,
                    range=f"Sheet1!A{i+1}:E{i+1}"
                ).execute()
                print(f"🗑️ Deleted row for topic: {topic}")
                break

        return f"""
        <p>🗑️ Topic '<strong>{topic}</strong>' rejected and removed from sheet.</p>
        <script>
            const approveBtn = document.querySelector('a[href*="approve"]');
            if (approveBtn) approveBtn.style.display = 'none';
        </script>
    """
    except Exception as e:
        print(f"❌ Error in reject_topic: {e}")
        return f"Error rejecting topic: {str(e)}", 500

@app.route("/approve-gavari", methods=["GET"])
def approve_gavari():
    try:
        topic = request.args.get("topic")
        category = request.args.get("category")
        keyword = request.args.get("keyword")

        if not topic or not category or not keyword:
            return "Missing topic, keyword, or category", 400

        doc_id = drive_agent.get_doc_id_by_title(topic)
        if doc_id:
            blog_folder_id = drive_agent.create_blog_folder(topic)
            if blog_folder_id:
                drive_agent.move_doc_to_folder(doc_id, blog_folder_id)

                folder_link = f"https://drive.google.com/drive/folders/{blog_folder_id}"
                sheet_agent.update_blog_status(topic, f"Approved ✅ - {folder_link}")

                sheet_data = sheet_agent.sheets_service.spreadsheets().values().get(
                    spreadsheetId=SHEET_ID,
                    range="Sheet1!A:A"
                ).execute()
                rows = sheet_data.get("values", [])

                cleaned_topic = topic.strip().lower().replace('"', '')
                row_number = None

                for i, row in enumerate(rows):
                    if row and row[0].strip().lower().replace('"', '') == cleaned_topic:
                        row_number = i + 1
                        break

                if row_number:
                    sheet_agent.sheets_service.spreadsheets().values().update(
                        spreadsheetId=SHEET_ID,
                        range=f"Sheet1!F{row_number}",
                        valueInputOption="RAW",
                        body={"values": [["Approved by Gauri ✅"]]}
                    ).execute()
                    print(f"🟢 Content_Status updated for topic: {topic}")
                else:
                    print(f"⚠️ Could not find topic in sheet for updating Content_Status: {topic}")
        else:
            print("❌ Could not find doc to move.")

        return f"<p>✅ Approved by Gauri. Blog stored in Drive and status updated.</p>"
    except Exception as e:
        print(f"❌ Error in approve_gavari: {e}")
        return f"Error approving by Gavari: {str(e)}", 500

@app.route("/reject-gavari", methods=["GET"])
def reject_topic_gavari():
    try:
        topic = request.args.get("topic")
        keyword = request.args.get("keyword")
        category = request.args.get("category")

        if not topic or not keyword or not category:
            return "Missing topic, keyword, or category", 400

        extra_keywords = topic_context.get(topic, {}).get("extra_keywords", [])
        blog_content = blog_writer.generate_blog(topic, keyword, extra_keywords, category)
        gavari_agent.send_blog_to_gavari(topic, blog_content, keyword, category)

        return f"""
        <p>🔁 A new version of the blog for '<strong>{topic}</strong>' has been generated and sent to Gauri Mam.</p>
        """
    except Exception as e:
        print(f"❌ Error in reject_topic_gavari: {e}")
        return f"Error regenerating blog: {str(e)}", 500

# Background task for generating topics
generation_enabled = os.getenv("ENABLE_AUTO_GENERATION", "true").lower() == "true"

def generate_and_send_topic():
    print(f"🚀 Background thread started. Auto-generation is {'enabled' if generation_enabled else 'disabled'}")
    
    while generation_enabled:
        try:
            print(f"⏰ Checking for topic generation at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            
            prompt_agent = PromptAgent(DOC_ID)
            keyword_agent = KeywordAgent()
            topic_agent = TopicAgent(OPENAI_API_KEY)

            prompt_text = prompt_agent.fetch_prompt()
            if prompt_text:
                keyword, matched_category, extra_keywords = keyword_agent.get_random_keyword()
                if keyword:
                    topic = topic_agent.generate_topic(prompt_text, keyword, matched_category)

                    if sheet_agent.topic_exists(topic):
                        print(f"⚠️ Duplicate topic skipped: {topic}")
                        continue

                    success = sheet_agent.add_blog_entry(topic, keyword, matched_category, extra_keywords)
                    if not success:
                        continue

                    approval_link = f"{BASE_URL}/approve?topic={quote(topic)}"
                    reject_link = f"{BASE_URL}/reject?topic={quote(topic)}"

                    approval_body = f"""
                    <p>New blog topic generated. Please review:</p>
                    <h3>{topic}</h3>
                    <p>Keyword: {keyword}</p>
                    <p>Category: {matched_category}</p>
                    <a href='{approval_link}' style='padding:10px;background:#2e86de;color:white;text-decoration:none;margin-right:10px;'>✅ Approve</a>
                    <a href='{reject_link}' style='padding:10px;background:#e74c3c;color:white;text-decoration:none;'>❌ Reject</a>
                    """

                    email_agent.send_email(HEAD_EMAIL, "Approval Needed: Blog Topic", approval_body)
                    print(f"📬 Blog topic sent for approval: {topic}")
                else:
                    print("⚠️ No keywords found to generate topic")
            else:
                print("⚠️ No prompt found in Google Doc.")
        except Exception as e:
            print(f"🔥 Error generating topic: {e}")
            import traceback
            traceback.print_exc()

        sleep_interval = int(os.getenv("GENERATION_INTERVAL", "60"))
        print(f"💤 Sleeping for {sleep_interval} seconds...")
        time.sleep(sleep_interval)

if __name__ == "__main__":
    # Start background thread for topic generation
    if generation_enabled:
        thread = threading.Thread(target=generate_and_send_topic)
        thread.daemon = True
        thread.start()
        print("✅ Background topic generation thread started")
    else:
        print("⚠️ Auto-generation is disabled")

    # Run Flask app
    port = int(os.environ.get("PORT", 8080))
    print(f"🚀 Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
