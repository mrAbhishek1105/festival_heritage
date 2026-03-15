import urllib.request
import re
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://texttohandwriting.in/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        html = response.read().decode('utf-8')
        headers = response.info()
        
        with open('output_utf8.txt', 'w', encoding='utf-8') as f:
            f.write("--- HEADERS ---\n")
            for k, v in headers.items():
                f.write(f"{k}: {v}\n")
                
            f.write("\n--- TECH STACK GUESSES ---\n")
            techs = []
            if 'bootstrap' in html.lower(): techs.append('Bootstrap')
            if 'jquery' in html.lower(): techs.append('jQuery')
            if 'react' in html.lower() or 'data-reactroot' in html.lower(): techs.append('React')
            if 'vue' in html.lower() or 'data-v-' in html.lower(): techs.append('Vue.js')
            if 'angular' in html.lower() or 'ng-' in html.lower(): techs.append('Angular')
            if 'tailwind' in html.lower(): techs.append('Tailwind CSS')
            if 'next' in html.lower() or '_next' in html.lower(): techs.append('Next.js')
            if 'nuxt' in html.lower(): techs.append('Nuxt.js')
            if 'google-analytics' in html: techs.append('Google Analytics')
            if 'cloudflare' in html.lower() or 'cf-ray' in headers: techs.append('Cloudflare')
            if 'wordpress' in html.lower() or 'wp-content' in html.lower(): techs.append('WordPress')
            if 'php' in html.lower() or 'PHPSESSID' in headers.get('Set-Cookie', ''): techs.append('PHP')
            
            f.write(f"Found clues for: {', '.join(techs) if techs else 'None obvious'}\n")
            
            f.write("\n--- LINKS & SCRIPTS ---\n")
            scripts = re.findall(r'<script.*?(?:src=["\'](.*?)["\']).*?>', html, re.IGNORECASE)
            links = re.findall(r'<link.*?(?:href=["\'](.*?)["\']).*?>', html, re.IGNORECASE)
            f.write(f"Scripts: {scripts[:15]}\n")
            f.write(f"Styles & Links: {links[:15]}\n")
            
            f.write("\n--- CONTENT SNIPPET ---\n")
            f.write(html[:500])
except Exception as e:
    print(f"Error: {e}")
