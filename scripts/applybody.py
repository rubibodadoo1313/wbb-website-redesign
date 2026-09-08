"""Rewrite the six 'Apply for this role' Gmail links with the new letter body."""
import os, re, urllib.parse
os.chdir(r"D:\Ruby Jane Files\Job Related\Work beyond borders\AI files\new wbb website\wbb-redesign 2")

TO = "info@workbeyondborder.com"

BODY = """Hello Work Beyond Borders Team,

I am writing to express my interest in applying for the {position} position at Work Beyond Borders.

I believe my skills, experience, and willingness to learn would allow me to contribute positively to your team. I am particularly interested in this opportunity because it aligns with my strengths and my interest in developing my skills in a professional, fast-paced, and collaborative environment.

I have attached my cover letter and resume/CV for your review. I would appreciate the opportunity to discuss my qualifications further and learn more about the role during an interview.

<attach your resume/CV here> <attach your cover letter here>
Thank you for considering my application. I look forward to hearing from you.

Best regards,
<Your Full Name>"""

# panel id -> (position name used in the letter, subject line)
ROLES = {
    "role-intern": ("Intern",                         "WBB_intern2026"),
    "role-ma":     ("Marketing Assistant",            "WBB_MA2026"),
    "role-sms":    ("Sales and Marketing Specialist", "WBB_S&MS2026"),
    "role-ea":     ("Executive Assistant",            "WBB_ES2026"),
    "role-grs":    ("Growth and Revenue Specialist",  "WBB_G&RS2026"),
    "role-am":     ("Account Manager",                "WBB_AM2026"),
}

def gmail_url(position, subject):
    q = urllib.parse.urlencode(
        {"view": "cm", "fs": "1", "tf": "1", "to": TO,
         "su": subject, "body": BODY.format(position=position)},
        quote_via=urllib.parse.quote)
    return "https://mail.google.com/mail/?" + q

html = open("careers.html", encoding="utf-8").read()

# Each panel holds exactly one apply link; swap the href inside that panel only.
changed = 0
for panel_id, (position, subject) in ROLES.items():
    # the panel opens at id="<panel_id>" and ends at the next </article>
    start = html.index(f'id="{panel_id}"')
    end = html.index("</article>", start)
    block = html[start:end]
    m = re.search(r'href="(https://mail\.google\.com[^"]*)"', block)
    assert m, panel_id
    new_href = gmail_url(position, subject).replace("&", "&amp;")
    html = html[:start] + block.replace(m.group(1), new_href) + html[end:]
    changed += 1

open("careers.html", "w", encoding="utf-8").write(html)
print(f"rewrote {changed} apply links")

# ---- verify by decoding straight back out of the file ----
print()
for m in re.finditer(r'href="(https://mail\.google\.com[^"]*)"', open("careers.html", encoding="utf-8").read()):
    q = urllib.parse.parse_qs(urllib.parse.urlsplit(m.group(1).replace("&amp;", "&")).query,
                              keep_blank_values=True)
    body = q.get("body", [""])[0]
    if not body:
        continue
    first = [l for l in body.splitlines() if "applying for the" in l]
    print("su=%-16s len=%4d  %s" % (q["su"][0], len(m.group(1)),
                                    first[0].strip() if first else "?"))
