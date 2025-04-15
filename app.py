import os
import base64
import uuid
from pathlib import Path
from dotenv import load_dotenv
import chainlit as cl
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are an elite software engineering assistant helping a highly-skilled developer (Luciana Ferreira). You must produce clean, production-ready code, optimized for modern architectures and best practices. Prioritize:
- Efficient use of compute and memory
- Clear abstraction boundaries and modularity
- Security and compliance
- Developer experience (DX)

Luciana prefers:
- Vim commands for all terminal instructions
- High-level reasoning before proposing implementations
- Academic-quality explanations, aligned with PhD-level CS knowledge
- Output aligned with practices from FAANG and billion-dollar tech startups

Only suggest cutting-edge tools and libraries. Default to TypeScript, Python, or Rust unless specified. When integrating with frameworks, ensure compatibility with scalable deployments (e.g., Docker, Kubernetes, serverless).

When generating code:
- Avoid unnecessary comments or placeholder variables
- Include complete, executable examples when possible
- Use industry-standard linters and formatters (e.g., Black, Prettier, Clippy)
- Version-control everything with Git-friendly practices

If the scope is ambiguous, use your best effort to maximize ROI.
"""

MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".gif": "image/gif"
}

@cl.on_message
async def main(message: cl.Message):
    try:
        if not hasattr(cl.user_session, "custom_id"):
            cl.user_session.custom_id = str(uuid.uuid4())
        session_id = cl.user_session.custom_id

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        content = []
        if message.content:
            content.append({"type": "text", "text": message.content})

        for element in message.elements:
            try:
                file_path = Path(element.path).resolve()
                if not file_path.is_file():
                    continue

                with open(file_path, "rb") as f:
                    image_bytes = f.read()
                    base64_image = base64.b64encode(image_bytes).decode("utf-8")
                    ext = os.path.splitext(element.name.lower())[1]
                    mime_type = MIME_TYPES.get(ext, "image/jpeg")
                    content.append({
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{mime_type};base64,{base64_image}",
                            "detail": "high"
                        }
                    })
            except Exception as e:
                await cl.Message(content=f"Error reading image: {str(e)}").send()
                return

        messages.append({"role": "user", "content": content})

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-2025-04-14",
                messages=messages,
                max_tokens=1000
            )
            reply = response.choices[0].message.content
        except Exception as e:
            await cl.Message(content=f"Error with OpenAI API: {str(e)}").send()
            return

        await cl.Message(content=reply).send()
    finally:
        pass
