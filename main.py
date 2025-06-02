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
from urllib.parse import quote
import time

# Load environment variables
load_dotenv()

# === Environment Variables ===
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
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
CTA_SHEET_ID = os.getenv("CTA_SHEET_ID")
PRODUCT_SHEET_ID = os.getenv("PRODUCT_SHEET_ID")

SCOPES = [
    "https://www.googleapis.com/auth/documents.readonly",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets.readonly"
]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
docs_service = build("docs", "v1", credentials=credentials)
drive_service = build("drive", "v3", credentials=credentials)
sheets_service = build("sheets", "v4", credentials=credentials)

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
    "WIGS": "1wkhdD3tpKNNWM4oVmuAaXhNh1Hw243LrEBxuXdrGwKc",
    "SILK HAIR TOPPER": "1KP96hqO8rhnWq0K5t33rF5B6Vdv9VGk5Pc4_Hw8NoI4",
    "SKIN HAIR TOPPER": "1K6O0ocZWndsG9eC3A1hbpPS3hLJQrpwyFIbHuAUraQI",
    "HAIR TOPPERS": "1k1dbAKRlPwqfLSVTIIzeASXr458RB8-fx7GvwdiM8Bg",
    "GLUE/KERATIN BOND HAIR EXTENSIONS": "1L4boRvpjbz1INQUQERf8mvFe7QKo5156BdrKPNPdi14",
    "TAPE-IN HAIR EXTENSIONS": "1R9MfHLR_GwjOzkF8hxwxNV0VVLt3DlRp5NmbM049QZw",
    "PERMANENT HAIR EXTENSIONS": "1SNX6Jamb2PDGUTj1osBVx0gyp0ODqWYu3RXF4vTmtAE",
    "MICRO RING HAIR EXTENSIONS": "12r4O5JFXDaAoH6ZWFzZLNb1FGzLVpYLtgJgGq153wiQ"
}

ALL_CATEGORIES = [k.replace('-', ' ').replace('_', ' ').lower() for k in KEYWORD_SHEETS.keys()]

class PromptAgent:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.docs_service = build("docs", "v1", credentials=credentials)

    def fetch_prompt(self):
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
class AudienceAgent:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.docs_service = build("docs", "v1", credentials=credentials)

    def fetch_audience_text(self):
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

class KeywordAgent:
    def __init__(self):
        self.sheets_service = build("sheets", "v4", credentials=credentials)

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
        self.sheets_service = build("sheets", "v4", credentials=credentials)

    def fetch_product_text(self, category):
        try:
            result = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=self.sheet_id,
                range="Sheet1!A:D"  # Assuming 4 columns: Category, Sub-type, Long Text, Short Text
            ).execute()

            rows = result.get("values", [])
            category = category.upper().strip()

            for row in rows[1:]:  # Skip header
                if row and row[0].strip().upper() == category:
                    return row[2]  # Return the long product detail (column C)
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
        doc_id_audience = TARGET_AUDIENCE_DOCS.get(category.upper()) if category else None
        audience_text = ""
        product_text = ""

        if doc_id_audience:
            audience_text = AudienceAgent(doc_id_audience).fetch_audience_text()
        # ✅ Fetch product details
        product_text = ""
        product_agent = ProductSheetAgent(PRODUCT_SHEET_ID)
        if category:
            product_text = product_agent.fetch_product_text(category)


        # ✅ Now fetch product text from sheet
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

class GiveawayAgent:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.docs_service = build("docs", "v1", credentials=credentials)

    def fetch_all_giveaways(self):
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

    def select_relevant_giveaway(self, keyword, category=None):
        from difflib import SequenceMatcher

        all_giveaways = self.fetch_all_giveaways()
        keyword = keyword.lower()
        category = (category or "").lower()

        # 1. Check for lines that include the category keyword (like "wig" or "topper")
        for line in all_giveaways:
            if category in line.lower():
                print(f"🎯 Matched category-based giveaway for: {category}")
                return line

        # 2. Exact keyword match
        for line in all_giveaways:
            if keyword in line.lower():
                print("✅ Exact match giveaway selected")
                return line

        # 3. Fuzzy match
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

    # 4. Fallback with phone number
        for line in all_giveaways:
            if "+91 9967123333" in line:
                print("📞 Fallback line with phone number used")
                return line

        return random.choice(all_giveaways) if all_giveaways else ""


class CTAAgent:
    def __init__(self, sheet_id):
        self.sheet_id = sheet_id
        self.sheets_service = build("sheets", "v4", credentials=credentials)

    def fetch_all_ctas(self):
        result = self.sheets_service.spreadsheets().values().get(
            spreadsheetId=self.sheet_id,
            range="Sheet1"
        ).execute()
        rows = result.get("values", [])
        return rows

    def select_cta(self, category=None):
        category = (category or "").lower().strip()
        rows = self.fetch_all_ctas()

        if not rows:
            return "👉 [Fill this quick form to get personalized guidance on your hair journey.](https://forms.gle/xdzYyJK5cH7HKEHW7)"

        headers = rows[0]
        category_col = 0
        option_cols = list(range(1, len(headers)))

        # Try finding matching row for category
        matched_row = None
        for row in rows[1:]:
            if row and row[0].lower().strip() == category:
                matched_row = row
                break

        # Fallback: use default row
        if not matched_row:
            for row in rows[1:]:
                if row and row[0].lower().strip() == "default":
                    matched_row = row
                    break

        if not matched_row:
            return "👉 [Fill this quick form to get personalized guidance on your hair journey.](https://forms.gle/xdzYyJK5cH7HKEHW7)"

        # Pick a non-empty Option randomly
        options = [matched_row[i] for i in option_cols if i < len(matched_row) and matched_row[i].strip()]
        if options:
            selected_cta = random.choice(options).strip()

            if "forms.gle" not in selected_cta:
            # Optional: add as new line (for better formatting)
                selected_cta += "\n\n👉 [Fill out the form and get matched.](https://forms.gle/xdzYyJK5cH7HKEHW7)"

            return selected_cta



        return "👉 [Fill this quick form to get personalized guidance on your hair journey.](https://forms.gle/xdzYyJK5cH7HKEHW7)"

class BlogWriterAgent:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.docs_service = build("docs", "v1", credentials=credentials)

    def fetch_blog_prompt(self):
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

    def generate_blog(self, title, keyword, extra_keywords, category=None):
        prompt = self.fetch_blog_prompt()
        # ✅ Fetch audience insights
        audience_text = ""
        doc_id_audience = TARGET_AUDIENCE_DOCS.get(category.upper()) if category else None
        if doc_id_audience:
            audience_text = AudienceAgent(doc_id_audience).fetch_audience_text()

        product_text = ""
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

        # Retry logic for length
        for _ in range(3):
            response = OpenAI(api_key=OPENAI_API_KEY).chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": (
                "You're a professional blog writer. "
                "Use the Product Details section inside the blog where relevant to explain features, benefits, or help the user make decisions.\n\n"
                f"{rules_text}"  # ← Put rules here
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

        # ✅ Append a relevant giveaway
        giveaway_line = giveaway_agent.select_relevant_giveaway(keyword, category)
        if giveaway_line:
            blog_content += f"\n\n{giveaway_line.strip()}"
        # Normalize the category before using it to fetch CTA
        normalized_category = category.replace("-", " ").replace("_", " ").lower() if category else None
        cta_line = cta_agent.select_cta(normalized_category)

        if cta_line:
            blog_content += f"\n{cta_line.strip()}"
        # ✅ Apply restricted word filtering
        blog_content = restricted_agent.filter_content(blog_content)

        return blog_content
class GavariAgent:
    def __init__(self, docs_service, drive_service, email_agent):
        self.docs_service = docs_service
        self.drive_service = drive_service
        self.email_agent = email_agent

    def send_blog_to_gavari(self, title, content, keyword, category):
        # 1. Create Google Doc
        doc_metadata = {'title': title}
        doc = self.docs_service.documents().create(body=doc_metadata).execute()
        doc_id = doc['documentId']

        # 2. Insert blog content with proper formatting
        requests = []
    
        # Add title with heading formatting
        requests.append({
            'insertText': {
                'location': {'index': 1},
                'text': title + "\n\n"
            }
        })
    
        # Format the title as Heading 1
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
    
        # Process the content to identify headers and lists
        lines = content.split('\n')
        current_index = len(title) + 2  # Start after title and two newlines
    
        for line in lines:
            line_text = line + "\n"
            line_length = len(line_text)
        
            # Insert the text line
            requests.append({
                'insertText': {
                    'location': {'index': current_index},
                    'text': line_text
                }
            })
        
            # Format headers
            if line.startswith('**') and line.endswith('**'):
                # This is a header (remove the ** markers)
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
        
            # Format bullet points
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
        
            # Format numbered lists
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
    
        # Execute all formatting requests
        self.docs_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()

        # 3. Share the document with Gauri Mam (edit access)
        self.drive_service.permissions().create(
            fileId=doc_id,
            body={
                'type': 'user',
                'role': 'writer',
                'emailAddress': GAVARI_EMAIL
            },
            fields='id'
        ).execute()

        # 4. Send email to Gauri mam
        subject = f"Approved Blog for Review: {title}"
        encoded_title = quote(title.replace('"', ''))
        encoded_keyword = quote(keyword)
        encoded_category = quote(category)

        approval_link = f"http://localhost:5000/approve-gavari?topic={encoded_title}&category={encoded_category}&keyword={encoded_keyword}"

        reject_link = f"http://localhost:5000/reject-gavari?topic={encoded_title}&category={encoded_category}&keyword={encoded_keyword}"

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

class SheetAgent:
    def __init__(self):
        self.sheets_service = build("sheets", "v4", credentials=credentials)

    def get_all_topics(self):
        sheet = self.sheets_service.spreadsheets().values().get(
            spreadsheetId=SHEET_ID,
            range="Sheet1!A:A"
        ).execute()
        return set(row[0].strip().lower() for row in sheet.get("values", []) if row)

    def topic_exists(self, topic):
        return topic.strip().lower() in self.get_all_topics()

    def update_blog_status(self, topic, new_status):
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

    def add_blog_entry(self, topic, keyword, category, extra_keywords, status="Generated"):
        if self.topic_exists(topic):
            print(f"🚫 Skipping duplicate topic: {topic}")
            return False  # Don't add if already exists

        values = [[
            topic,
            keyword,
            category,
            status,
            str(__import__('datetime').datetime.now().date()),
            "Generated",  # Column F: Content_Status
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

    def get_topic_data(self, topic):
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
        folder_metadata = {
            'name': blog_title,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [self.parent_folder_id]
        }
        folder = self.drive_service.files().create(body=folder_metadata, fields='id').execute()
        return folder.get('id')

    def move_doc_to_folder(self, doc_id, folder_id):
        self.drive_service.files().update(
            fileId=doc_id,
            addParents=folder_id,
            removeParents='root',  # Optional: remove from root
            fields='id, parents'
        ).execute()

    def get_doc_id_by_title(self, title):
        query = f"name contains '{title}' and mimeType = 'application/vnd.google-apps.document'"
        response = self.drive_service.files().list(q=query, fields="files(id, name)").execute()
        files = response.get('files', [])
        if files:
            return files[0]['id']
        return None
class RestrictedWordAgent:
    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.docs_service = build("docs", "v1", credentials=credentials)

    def fetch_rules_as_text(self):
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
    def filter_content(self, content):
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
# === Main Execution Block ===
def main():
    try:
        prompt_agent = PromptAgent(DOC_ID)
        keyword_agent = KeywordAgent()
        topic_agent = TopicAgent(OPENAI_API_KEY)
        cta_agent = CTAAgent(CTA_SHEET_ID)
        blog_writer = BlogWriterAgent(BLOG_PROMPT_DOC_ID)
        giveaway_agent = GiveawayAgent(GIVEAWAY_DOC_ID)
        restricted_agent = RestrictedWordAgent(RESTRICTED_DOC_ID)
        email_agent = EmailAgent(FROM_EMAIL, EMAIL_APP_PASSWORD)
        gavari_agent = GavariAgent(docs_service, drive_service, email_agent)

        prompt_text = prompt_agent.fetch_prompt()
        if not prompt_text:
            print("⚠️ No prompt found in Google Doc.")
            return

        keyword, matched_category, extra_keywords = keyword_agent.get_random_keyword()
        if not keyword or not matched_category:
            print("⚠️ No keyword/category found.")
            return

        topic = topic_agent.generate_topic(prompt_text, keyword, matched_category)
        blog_content = blog_writer.generate_blog(topic, keyword, extra_keywords, matched_category)
        gavari_agent.send_blog_to_gavari(topic, blog_content, keyword, matched_category)

        # Compose and send approval email
        approval_link = f"https://your-approval-url/approve?topic={quote(topic)}"
        reject_link = f"https://your-approval-url/reject?topic={quote(topic)}"
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

    except Exception as e:
        print("🔥 Error generating topic:", str(e))

if __name__ == "__main__":
    main()
