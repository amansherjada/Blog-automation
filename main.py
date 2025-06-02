import logging
import os
import signal
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

# Attempt to import necessary agent classes; if not available, define placeholders
try:
    from prompt_agent import PromptAgent
    from keyword_agent import KeywordAgent
    from topic_agent import TopicAgent
    from blog_writer_agent import BlogWriterAgent
    from email_agent import EmailAgent
except ImportError:
    # Placeholder implementations for demonstration purposes
    class PromptAgent:
        def get_prompt(self):
            logging.info("PromptAgent: fetching prompt")
            # Example: retrieve prompt from a data source
            return "Sample prompt"
    class KeywordAgent:
        def get_keyword(self, prompt):
            logging.info("KeywordAgent: determining keyword from prompt")
            # Example: determine a keyword or category from the prompt
            return "SampleKeyword"
    class TopicAgent:
        def generate_topic(self, prompt, keyword):
            logging.info("TopicAgent: generating topic using prompt and keyword")
            # Example: use prompt and keyword to come up with a blog topic
            return f"Sample Topic related to {keyword}"
    class BlogWriterAgent:
        def write_blog(self, topic):
            logging.info("BlogWriterAgent: generating blog content for topic")
            # Example: generate blog content based on the topic
            return f"Blog content about {topic}..."
    class EmailAgent:
        def send_email(self, content):
            logging.info("EmailAgent: sending email with content preview: %.50s", content)
            # Example: send email with the content
            return True

logging.basicConfig(level=logging.INFO)

def main():
    """Perform one cycle of blog generation and emailing."""
    logging.info("Starting blog generation cycle")
    try:
        # Step 1: Fetch prompt
        prompt_agent = PromptAgent()
        prompt = prompt_agent.get_prompt()
        logging.info("Fetched prompt: %s", prompt)

        # Step 2: Determine keyword or category from the prompt
        keyword_agent = KeywordAgent()
        keyword = keyword_agent.get_keyword(prompt)
        logging.info("Determined keyword: %s", keyword)

        # Step 3: Generate a blog topic
        topic_agent = TopicAgent()
        topic = topic_agent.generate_topic(prompt, keyword)
        logging.info("Generated blog topic: %s", topic)

        # Step 4: Write the blog content
        writer_agent = BlogWriterAgent()
        blog_content = writer_agent.write_blog(topic)
        logging.info("Generated blog content (%d characters)", len(blog_content))

        # Step 5: Send the blog content via email
        email_agent = EmailAgent()
        email_agent.send_email(blog_content)
        logging.info("Email sent successfully")

        logging.info("Blog generation cycle completed successfully")
    except Exception as e:
        logging.exception("Error during blog generation cycle: %s", e)
        # Propagate the exception to indicate failure to the caller
        raise

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/generate":
            logging.info("Received request: POST %s", self.path)
            try:
                main()
                # Respond with success
                self.send_response(200)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write(b"Blog generation completed successfully")
            except Exception as e:
                # Respond with error status and message
                self.send_response(500)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.end_headers()
                error_msg = f"Blog generation failed: {e}"
                self.wfile.write(error_msg.encode("utf-8"))
        else:
            # Invalid endpoint
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Not Found")

    def do_GET(self):
        if self.path == "/":
            # Health check endpoint
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/generate":
            # Method not allowed for GET on /generate
            self.send_response(405)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Method Not Allowed")
        else:
            # Endpoint not found
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Not Found")

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """HTTP server that handles each request in a separate thread."""
    daemon_threads = True

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    server_address = ("", port)
    httpd = ThreadedHTTPServer(server_address, RequestHandler)
    # Setup signal handler for graceful termination
    signal.signal(signal.SIGTERM, lambda signum, frame: httpd.shutdown())
    logging.info("Starting server on port %d", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("Server stopping...")
        httpd.server_close()
