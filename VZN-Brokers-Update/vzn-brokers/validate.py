import asyncio
from playwright.async_api import async_playwright
import os

async def validate_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        errors = []

        # Listen for console errors
        page.on("console", lambda msg: errors.append(f"Console {msg.type}: {msg.text}") if msg.type == "error" else None)

        # Listen for page errors
        page.on("pageerror", lambda exc: errors.append(f"Page error: {exc}"))

        # Load the local HTML file
        html_path = f"file://{os.path.abspath('index.html')}"

        try:
            response = await page.goto(html_path, wait_until="networkidle", timeout=30000)

            # Check if page loaded
            title = await page.title()
            print(f"✓ Page loaded successfully")
            print(f"✓ Title: {title}")

            # Check for hero video
            video = await page.query_selector("video.hero-video")
            if video:
                print(f"✓ Hero video element found")
            else:
                print(f"⚠ Hero video element not found")

            # Check for main sections
            sections = ["hero", "trust-bar", "services", "why-us", "industries", "cta-section", "footer"]
            for section in sections:
                el = await page.query_selector(f".{section}, #{section}")
                if el:
                    print(f"✓ Section '{section}' found")
                else:
                    print(f"⚠ Section '{section}' not found")

            # Report errors
            if errors:
                print(f"\n⚠ Console/Page Errors:")
                for err in errors:
                    print(f"  - {err}")
            else:
                print(f"\n✓ No console errors detected")

        except Exception as e:
            print(f"✗ Error loading page: {e}")

        await browser.close()

asyncio.run(validate_page())