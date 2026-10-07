# Work Beyond Borders — local site


## Run it

Double-clicking `index.html` works, but the pages look best over a local server
(some browsers restrict things on `file://`). From this folder:

```bash
python -m http.server 5173
```

Then open <http://localhost:5173/index.html>.

## Pages

| File | What it is |
| --- | --- |
| `index.html` | Landing page — hero, **video explainer**, What We Do, case studies, 280M results band, strengths, **reels**, approach, testimonial, footer |
| `activities.html` | Davao, Iloilo and Gensan meetups, each with a scrollable photo rail |
| `careers.html` | Six roles in an accordion, each with qualifications, subject line and an apply button |

Every page shares the header (with the **Contact us** button) and the footer.

## Contact form

The **Contact us** button in the header of all three pages opens a popup with the
form: name, email, phone (optional) and *What can we help you with?*

Delivery is **Netlify Forms**, so this only works once the site is deployed to
Netlify. Netlify finds the form by scraping the deployed HTML, which is what these
attributes on the `<form>` are for:

```html
<form name="contact" method="POST" data-netlify="true" data-netlify-honeypot="botcheck">
  <input type="hidden" name="form-name" value="contact">
```

The same form appears on all three pages under one name, so Netlify records them as a
single form called **contact**.

### Turning it on after the first deploy

Netlify does not know where to send submissions until you tell it:

1. Deploy the site to Netlify.
2. **Site settings → Forms → Form notifications → Add notification → Email notification**
3. Set the address to `itwbb@gmail.com` and pick the **contact** form.

Submissions are also listed in the Netlify dashboard under **Forms**, so nothing is
lost if the email notification is ever misconfigured. The free tier covers 100
submissions a month.

### What happens when it cannot send

`fetch('/')` has nothing to answer it on a local preview, or if Netlify is unreachable.
Rather than lose the enquiry, the catch opens a **Gmail compose window to
`itwbb@gmail.com`** with every answer already filled in, and says so on screen. The
popup stays open so nothing typed is thrown away.

That is why the form appears "broken" when you open it locally — it is the fallback
doing its job. Deployed to Netlify, it sends silently.

### Spam

`botcheck` is a hidden checkbox that people never see and bots tick. Netlify drops any
submission where it is filled, and the JS bails out too.

## Email links

The remaining email buttons open a **Gmail compose window** in a new tab, addressed to
`info@workbeyondborder.com`.

- *Inquire now*, *Get started* and the footer *Contact* link — recipient only, no subject.
- **Apply for this role** (careers) — recipient, the role's subject line, and a full
  draft cover note. The role name is filled into the opening sentence automatically
  ("applying for the Account Manager position"), so each of the six buttons carries its
  own body. The applicant fills in `<Your Full Name>` and attaches their files.

| Role | Subject line |
| --- | --- |
| Intern | `WBB_intern2026` |
| Marketing Assistant | `WBB_MA2026` |
| Sales and Marketing Specialist | `WBB_S&MS2026` |
| Executive Assistant | `WBB_ES2026` |
| Growth and Revenue Specialist | `WBB_G&RS2026` |
| Account Manager | `WBB_AM2026` |

To change an address or subject, edit the `mail.google.com` links directly in the HTML.
Everything after `?` is URL-encoded: `&` in a subject becomes `%26` (so `WBB_S&MS2026` →
`su=WBB_S%26MS2026`), spaces become `%20` and line breaks in the body become `%0A`.

Because of that encoding the apply links are long (~1,200 characters) and awkward to edit
by hand. To reword the letter, edit `BODY` in
`scripts/applybody.py` and re-run it — it rebuilds all six links and prints the decoded
result back so you can check it.

## Files

```
index.html  activities.html  careers.html
assets/css/styles.css     all styling, design tokens at the top
assets/js/main.js         sticky header, mobile nav, accordion, photo rails, scroll reveals, video explainer + popup, reels, contact form
netlify.toml              tells Netlify to publish the repo root as-is (no build step)
assets/img/               web-optimised images (resized + compressed)
assets/video/             web-optimised video (see Video explainer)
reels/                    the 11 home-page reels (see Reels)
wbb video explainer/      the original explainer export (source, not served, not in git)
new imgs/                 your original, full-resolution source images (untouched)
landingpage.psd           the hero artwork the landing page hero is built from
```

Images in `assets/img/` are generated from `new imgs/`: photos resized and saved as
progressive JPEG, cut-out people and props kept as transparent PNG. Re-drop a
replacement into `assets/img/` under the same filename to swap any picture.

The footer on each page uses a photo of the team (`footer asset 1/2/3`), with the
frosted panel pulled up over its lower half by a negative margin. The art is **full-bleed** — `width:100vw` with `margin-inline:calc(50% - 50vw)`
to break out of the shell — because capped at the content width it read as a photo
floating in the middle of the footer. The overlap is expressed in `vw` so it tracks the
image height (which is now a fraction of the viewport width) and keeps a constant bite
at any size, and a mask gradient dissolves the photo's bottom edge, which the panel no
longer fully covers now that the art is wider than it is.

The footer `<img>` tags carry explicit `width`/`height`. Without them the browser
reserves no space for a lazy-loaded image, so the page height is wrong until it
arrives — which truncated the footer entirely in full-page captures and would cause
layout shift for a real visitor.

`landing page asset 5` is the cut-out in *Our approach*. `landing page asset 6` is the
photo behind the **280M** results band (`results-band.jpg`).

**The footer art is a full photo, not a cut-out.** It used to be the team cut out of
their background and standing on a warm gradient. `footer asset 1/2/3` are now supplied
with their backgrounds intact and used as-is — the trees, the garden and the diner
floor are meant to be there. Resize to 1600px wide and save as progressive JPEG;
nothing else is done to them. Do **not** run a background remover over them.

### The hero cut-outs

The people in the landing hero are positioned to match the layer geometry in
`landingpage.psd`. They're sized by **height** (`.hero__cut--tl / --bl / --br` in the
stylesheet) so each keeps its own proportions at any screen width. There were four;
`landing page asset 4` was deleted from the source folder, so the top-right figure and
its `.hero__cut--tr` rules came out with it and three remain. They fade back on tablets and are hidden
on phones, where four people would crowd out the headline.

`mascot.png` (from `careerspage asset.png`) is the WBB giraffe, sitting at the
bottom-left of the Careers hero. Being an illustration rather than a photo cut-out, it
sits fully in frame instead of cropping off the edge.

### The halftone stickers

`sticker 1`–`11` are in `assets/img/` under readable names (`st-megaphone.png`,
`st-calculator.png`, `st-writing.png` …). All eleven are placed, each used once:

| Section | Stickers |
| --- | --- |
| Case studies | megaphone, papers (above the card row), calculator, laptop (below it) |
| More than an agency | paper plane, notes, iMac, handshake — a collage in the left column, standing in for a photo the way the Canva design does |
| Our approach | pen, bulb, writing hand |

They drift slowly up and down on a shared `wbb-float` keyframe, each with its own
amplitude, duration (6–9s) and negative delay so they never move in lockstep. `rotate`
is set as its own property rather than inside `transform`, which is what lets the tilt
and the float coexist.

**Keeping them off the text.** The two props above the case-study cards are the fiddly
ones. Their size comes from `--prop` on `.cases`, and the row's top margin is derived
from that same value — so the band they sit in is always tall enough and they can
neither reach up into the lede nor drop onto the "Case Study" tags. The `1.3` multiplier
in that margin is not padding for taste: a rotated element's real footprint is its
diagonal, not its height, and the float adds a few pixels more. Budget only for the
height and they creep onto the copy at some widths.

If you move a sticker, re-check it at several widths rather than just the one you are
looking at — most of the overlaps in this build only appeared at 960–1280px.

They're decorative: `aria-hidden` in the markup and `pointer-events:none` in CSS, so
they never block a click or get read out by a screen reader.

### Below 900px

Every section stacks into one column there, which leaves no margin for decoration to
live in. So the loose stickers, the four hero figures and the careers mascot are all
hidden, and the strengths collage becomes a tidy two-up grid instead of a free scatter
that would spill onto the orange panel. This is deliberate — those elements sat on the
headline, the buttons and the stats row at tablet widths.


The layout is calibrated against the Canva file rather than eyeballed. Every type
size in `:root` is expressed as **the design px size / 1162 (the canvas width) as a
vw figure**, so the page keeps the design proportions at any viewport:

| | design @1162 | token |
| --- | --- | --- |
| Section heading | 51.9px | `--fs-display` 4.47vw |
| Lede | 15.6px | `--fs-lede` 1.34vw |
| Body | 13.6px | `--fs-body` 1.17vw |
| Nav | 13.5px | `--fs-nav` 1.16vw |
| 280M | 168.4px | 14.49vw |

The clamps around each are a deliberate departure: the design sets footer links at
9.7px and column headings at 8.4px, which is too small to read comfortably on a real
screen, so those floor at 12px and 10px. Everything else follows the design.

Other things taken from the file rather than guessed: the peach-to-orange washes on
*What We Do* and *Case Studies*, the flat (6px radius) orange slab in *More than an
agency*, the deep gap under the case-study cards that the calculator and laptop hang
into, the meetup photo bleeding off the outer edge with the thumbnail rail running
past the opposite one, the hairline-outline jump box on Activities, and the Careers
rows being plain triangle-and-name until one is opened.

The hero photo carries `filter: brightness(1.26)`. The supplied `bg.png` is genuinely
dark (mean RGB ~53); Canva lifts it in the design, so the CSS does the same.

## Video explainer

The explainer plays in two places, both driven by the same file and the same code
(`wirePlayer` in `assets/js/main.js`):

1. **A popup on the first visit.** 1.2s after the page settles, a dialog opens over
   the site with the video already rolling. It closes on the X, the Esc key, a click
   on the dark surround, or *Skip and explore the site*.
2. **A section on the home page**, between the hero and What We Do, so the video is
   still there once the popup is gone (or for anyone who never saw it).

### Things worth knowing

- **It only pops up once per browser.** The flag is `wbb:explainer-seen` in
  `localStorage`, written the moment the popup opens. To see it again, clear site data
  or run `localStorage.removeItem('wbb:explainer-seen')` in the console.
- **Sound.** The popup asks to start *with* sound. Most browsers refuse audio that no
  click asked for, so it falls back to a muted run and shows a **Tap for sound** button.
  Clicking play in the page section is a real click, so that one always has sound.
- **Reduced motion.** If the visitor's system asks for less motion, the popup still
  opens but waits behind its play button instead of auto-rolling.
- **The video is re-encoded for the web**, not served from `wbb video explainer/`:

  | | Source | Served |
  | --- | --- | --- |
  | File | `wbb video explainer/1st Version.mp4` | `assets/video/wbb-explainer.mp4` |
  | Size | 7.8 MB | 3.3 MB |
  | Layout | metadata at the end | `faststart` — metadata first |

  The `faststart` part matters: in the source file the browser had to pull all 7.8 MB
  before it could show a frame, which would have left the popup blank. Re-encoded at
  CRF 23 the text stays as crisp as the original.

- **The poster** (`assets/img/explainer-poster.jpg`) is the closing brand frame at
  16s, so the box is never empty while the video streams in.

To regenerate either after a new cut of the video:

```bash
ffmpeg -i "wbb video explainer/1st Version.mp4" -c:v libx264 -crf 23 -preset slow   -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart assets/video/wbb-explainer.mp4
ffmpeg -ss 16 -i "wbb video explainer/1st Version.mp4" -frames:v 1 assets/img/explainer-poster.jpg
```

## Reels

A horizontal strip of short videos on the home page, straight after *More than an agency*.

- **Files** live in `reels/` and are listed one by one in `index.html` (newest first).
  To add or remove a reel, add or delete its `<figure class="reel">` line there.
- **Mixed shapes are fine.** Every card is the same height and takes its width from the
  video itself, so portrait and landscape reels both show uncropped. On phones the
  landscape ones shrink to fit the screen.
- **Playback.** Reels play muted while they are on screen and pause when they scroll
  away. Tapping a reel pauses or resumes it. The corner button turns sound on for that
  reel only. Visitors who ask for reduced motion get no autoplay.
- **Weight.** The folder is ~19 MB. Each video only loads its metadata until it is
  needed, but the two largest (5.3 MB and 3.8 MB) are worth compressing if the section
  feels slow on mobile data.

## Notes

- Fonts (Playfair Display + Figtree) load from Google Fonts, so the first load needs
  internet. Without it the page falls back to Georgia and a system sans.
- `overflow-x: clip` on `html, body` is deliberate — `hidden` turns `<body>` into a
  scroll container and stops the fixed header and everything below the fold from painting.
