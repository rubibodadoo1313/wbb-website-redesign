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
| `index.html` | Landing page — hero, What We Do, case studies, 280M results band, strengths, approach, testimonial, footer |
| `activities.html` | Davao, Iloilo and Gensan meetups, each with a scrollable photo rail |
| `careers.html` | Six roles in an accordion, each with qualifications, subject line and an apply button |

Every page shares the header (with the **Contact us** button) and the footer.

## Email links

All email buttons open a **Gmail compose window** in a new tab, addressed to
`info@workbeyondborder.com`.

- **Contact us** (header, on all three pages), plus *Book a free strategy call*,
  *Inquire now*, *Get started* and the footer *Contact* link — recipient only, no subject.
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
assets/js/main.js         sticky header, mobile nav, accordion, photo rails, scroll reveals
assets/img/               web-optimised images (resized + compressed)
new imgs/                 your original, full-resolution source images (untouched)
landingpage.psd           the hero artwork the landing page hero is built from
```

Images in `assets/img/` are generated from `new imgs/`: photos resized and saved as
progressive JPEG, cut-out people and props kept as transparent PNG. Re-drop a
replacement into `assets/img/` under the same filename to swap any picture.

The footer on each page uses a cut-out of the team (`footer asset 1/2/3`) standing on a
warm gradient, with the frosted panel pulled up over their lower half by a negative
margin. The art is **full-bleed** — `width:100vw` with `margin-inline:calc(50% - 50vw)`
to break out of the shell — because capped at the content width it read as a photo
floating in the middle of the footer. The overlap is expressed in `vw` so it tracks the
image height (which is now a fraction of the viewport width) and keeps a constant bite
at any size, and a mask gradient dissolves the cut-out bottom edge, which the panel no
longer fully covers now that the art is wider than it is.

The footer `<img>` tags carry explicit `width`/`height`. Without them the browser
reserves no space for a lazy-loaded image, so the page height is wrong until it
arrives — which truncated the footer entirely in full-page captures and would cause
layout shift for a real visitor.

`landing page asset 5` is the cut-out in *Our approach*.

### The hero cut-outs

The four people in the landing hero are positioned to match the layer geometry in
`landingpage.psd` — two crowding in from the left edge, two from the right. They're
sized by **height** (`.hero__cut--tl / --bl / --tr / --br` in the stylesheet) so each
keeps its own proportions at any screen width. They fade back on tablets and are hidden
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

## Notes

- Fonts (Playfair Display + Figtree) load from Google Fonts, so the first load needs
  internet. Without it the page falls back to Georgia and a system sans.
- `overflow-x: clip` on `html, body` is deliberate — `hidden` turns `<body>` into a
  scroll container and stops the fixed header and everything below the fold from painting.
