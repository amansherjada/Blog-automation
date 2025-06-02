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

# Load environment variables from .env (for local dev; Cloud Run uses env vars)
load_dotenv()

# === Reference Blog and Constants ===
REFERENCE_BLOG = """ Are Celebrities Really Using Hair Toppers? The Answer May Surprise You!
Have you ever wondered how celebrities always seem to have perfect, voluminous hair? Whether on the red carpet, in movies, or on social media, their hair looks flawless. The truth is, many of them aren’t relying on genetics alone. The secret behind their luscious hairs? Hair toppers for thinning hair.
While most people associate hair extensions for women with length and volume, hair toppers specifically target thinning areas on the top and crown of the head. And guess what? Some of the most famous names in Hollywood and Bollywood swear by them. But why do they use them, and how do they achieve such natural results? Let’s dive in.
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
Camera-Ready Volume – Thin or flat hair doesn’t photograph well, and hair toppers for volume solve that instantly.
Age-Related Thinning – Many celebrities experience hair thinning as they age, just like millions of women worldwide.
Medical Conditions – Some stars suffer from conditions like alopecia or stress-related hair loss and use hair toppers for alopecia as a discreet solution.
Undetectable Enhancement – Today’s seamless hair toppers blend so well with natural hair that even HD cameras can’t detect them.
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
Absolutely. The beauty of natural-looking hair toppers is that they are not just for celebrities. With the right product and a few styling tricks, you can achieve the same flawless look in your daily life. Today’s human hair toppers are designed to blend seamlessly, offering a natural appearance that even up-close scrutiny won’t reveal. Unlike full wigs, toppers integrate with your own hair, enhancing volume and covering thinning areas without looking artificial.
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
Celebrities have long known the power of hair toppers for thinning hair, and now, this secret is available to everyone. Whether you’re looking for clip-in hair toppers for a quick fix or custom hair toppers for a long-term solution, there are options for every woman.
Looking your best isn’t just about vanity—it’s about confidence. With natural-looking hair toppers, you can step out feeling self-assured, knowing your hair looks just as glamorous as any celebrities. Why wait? Explore the best options and rediscover the beauty of full, voluminous hair today.
 """  # (Keep your reference blog here)

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

# === All your class definitions here ===
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
        # You can add duplicate checking logic here if needed

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
