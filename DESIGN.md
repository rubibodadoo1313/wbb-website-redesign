---
name: Work Beyond Borders
description: Warm editorial paper, one hot orange, and a Playfair italic that carries the accent of every headline.
colors:
  orange: "#d14a22"
  orange-deep: "#b93d18"
  orange-bright: "#ff7342"
  ink: "#1a1817"
  ink-2: "#4a4643"
  ink-3: "#77716c"
  paper: "#f2f1f1"
  cream: "#f2efe5"
  white: "#fff"
  line: "rgba(26,24,23,.12)"
typography:
  display:
    fontFamily: "Playfair Display, Georgia, Times New Roman, serif"
    fontSize: "clamp(30px, 4.47vw, 66px)"
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Playfair Display, Georgia, Times New Roman, serif"
    fontSize: "clamp(27px, 4.2vw, 58px)"
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Playfair Display, Georgia, Times New Roman, serif"
    fontSize: "clamp(18px, 2.02vw, 28px)"
    fontWeight: 500
    lineHeight: 1.05
  lede:
    fontFamily: "Figtree, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "clamp(14px, 1.34vw, 19px)"
    fontWeight: 400
    lineHeight: 1.45
  body:
    fontFamily: "Figtree, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "clamp(13px, 1.17vw, 16.5px)"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Figtree, Segoe UI, Helvetica, Arial, sans-serif"
    fontSize: "clamp(10px, 0.81vw, 12px)"
    fontWeight: 600
    letterSpacing: "0.16em"
  figure:
    fontFamily: "Playfair Display, Georgia, Times New Roman, serif"
    fontSize: "clamp(46px, 8.2vw, 118px)"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "-0.035em"
    fontFeature: "tabular-nums"
rounded:
  sm: "10px"
  md: "18px"
  lg: "28px"
  xl: "40px"
  pill: "999px"
spacing:
  gut: "clamp(20px, 5vw, 48px)"
  section: "clamp(44px, 5.6vw, 74px)"
  section-tight: "clamp(34px, 4vw, 54px)"
  header: "88px"
  shell: "1160px"
components:
  button-primary:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "0.82em 1.5em"
    typography: "{typography.label}"
  button-primary-hover:
    backgroundColor: "{colors.orange-deep}"
    textColor: "{colors.white}"
  button-ghost:
    backgroundColor: "rgba(255,255,255,.94)"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0.82em 1.5em"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "0.82em 1.5em"
  button-sm:
    rounded: "{rounded.pill}"
    padding: "0.62em 1.15em"
  card:
    backgroundColor: "linear-gradient(180deg,#fffefb,#faf7f0)"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "14px 14px 22px"
  card-cream:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "20px 20px 24px"
  card-feature:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "clamp(26px,3.4vw,52px)"
  chip-outline:
    backgroundColor: "transparent"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "0.42em 1em"
  tag-solid:
    backgroundColor: "{colors.orange}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "0.34em 1em"
  input-text:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "12px"
    padding: "0.78em 0.95em"
    typography: "{typography.body}"
  nav-link:
    backgroundColor: "transparent"
    textColor: "rgba(255,255,255,.94)"
    padding: "6px 0"
---

# Design System: Work Beyond Borders

## Overview

**Creative North Star: "The Warm Paper Press"**

This is a print-room world rendered in a browser: a slightly warm off-white sheet, one
hot orange that behaves like a second ink rather than a UI accent, and a Playfair
Display headline whose accent word is always set in italic. Density is editorial, not
dashboard. Figures are set as type at Playfair scale with tabular figures, so a number
reads as a sentence's loudest word rather than as a tile in a grid. Photography and
cut-out halftone props (megaphone, calculator, laptop, paper plane) are collaged into
the margins at a slight rotation with a slow float, which is what keeps the paper from
reading as a flat template.

Depth is warm and shallow. Shadows are tinted by the surface they fall on — ink-brown
on paper, orange under an orange button — and every interactive surface lifts a few
pixels rather than scaling or glowing. Glass (backdrop-filter blur plus a saturation
boost) appears only where content must sit over photography: the stuck header, the
footer panel, the careers role accordion, and the two modal surrounds.

The orange is the system's one voice, and it is deployed as a field rather than as
trim: whole sections carry a peach-to-orange radial wash, while individual cards stay
cream or near-white. The newest surface (the Eve Sleep case study) extends this world
without reopening it — same type, same tokens, same pill buttons — and adds exactly one
component, the creator video rail.

**Key Characteristics:**
- Warm off-white paper (`#f2f1f1`) and cream panels (`#f2efe5`), never pure grey
- One orange working as a second ink, often as a section-wide radial wash
- Playfair Display display type with exactly one italic phrase per heading
- Figures set as display type with tabular figures, never as stat tiles
- Collaged halftone props, rotated, slowly floating, always decorative
- Pills for actions, slabs and soft rectangles for content
- Full-bleed or single-edge bleed media; radius dropped on the bleeding edge

## Colors

A warm neutral paper with a single orange family and a three-step ink ramp; there is no
second hue anywhere in the system.

### Primary
- **Campaign Orange** (`colors.orange`): The system's one voice. It is a *fill*, not a
  text color — the primary button, solid tags, the takeaway bullets, the unmuted sound
  toggle, the rail arrow fills, the focus ring, and the selection highlight at 22%
  alpha. Measured 3.95:1 on paper, so as type it is only legible at display scale.
- **Press Orange** (`colors.orange-deep`): The text-safe member of the family (4.98:1
  on paper). It carries orange *type*: the chain numbers on the case study and the
  "read the case study" link on the home card. Also the primary button's hover fill and
  the video player's letterbox base.
- **Hot Orange** (`colors.orange-bright`): Reserved for large saturated planes and
  marks on dark — the strengths slab, the checkmark bullets in the careers accordion,
  the orange jump-list triangle. Never used as body type.

### Neutral
- **Ink** (`colors.ink`): All primary type on paper, the dark case-study band, the dark
  button, and the video-thumbnail backing.
- **Ink 2** (`colors.ink-2`): Secondary and supporting copy — ledes, card body, table
  cells, form labels, figure captions, stuck-state nav links.
- **Ink 3** (`colors.ink-3`): Quiet metadata — the `.eyebrow` label, footer legal row,
  scroll hints, input placeholders, the optional-field marker. Measured 4.27:1 on
  paper, which is **below AA for small text**. This is a pre-existing site-wide
  condition, recorded here as-is and not repaired.
- **Paper** (`colors.paper`): The page ground on every surface.
- **Cream** (`colors.cream`): The panel ground that separates content from the page —
  case cards and the home case feature.
- **Hairline** (`colors.line`): The only divider stroke in the system. On the dark band
  and over photography the same idea is expressed as `rgba(255,255,255,.16)` and
  `rgba(255,255,255,.32)`.

### Named Rules
**The Deep-Orange-For-Type Rule.** Orange type below display scale is always
`colors.orange-deep` (4.98:1). `colors.orange` is a fill behind white, or type at
24px+. The case-study chain numbers and the home-card link both obey this; the footer
link hover (`colors.orange` on small text) is incumbent drift that does not.

**The One Hot Field Rule.** Orange washes belong to the *section*, as a layered radial
gradient on the section background or a blurred `.glow` circle behind it. A card, a
panel, or a form never carries the wash itself — it stays cream or near-white so the
field reads behind it.

**The Second-Ink Rule.** There is no third hue. Where a state needs a color the palette
does not have, the build reaches for raw hexes (`#c0392b` invalid, `#1e7a4d` success,
`#f0a68c` for italic accents on the dark band). These are real, untokenized one-offs,
not a secondary palette.

## Typography

**Display Font:** Playfair Display (with Georgia, Times New Roman, serif)
**Body Font:** Figtree (with Segoe UI, Helvetica, Arial, sans-serif)
**Mono:** `ui-monospace, SFMono-Regular, Menlo, monospace` — one use only, the email
subject line in the careers accordion.

Both faces load from Google Fonts as variable ranges including italics (Figtree
300–800, Playfair Display 400–700). Playfair is held at weight 500 everywhere — the
system never uses its bold. The pairing reads as a magazine feature: a high-contrast
serif at tight line-height over a neutral geometric sans set generously at 1.6.

**Character:** Editorial and confident, with the warmth coming from the paper rather
than from the letterforms. Every display size is a `clamp()` derived from the original
1162px canvas, so proportions hold rather than stepping at breakpoints.

### Hierarchy
- **Display** (`typography.display`): Section headings via `.display`; the landing hero
  pushes further to `clamp(2.4rem, 6.43vw, 5.6rem)` and the case-study statement to
  `clamp(38px, 7.4vw, 104px)` at `max-width: 14ch`.
- **Headline** (`typography.headline`): Case-study chain headings and dark-band
  headings, capped at `18ch` so a headline always breaks into two or three lines.
- **Title** (`typography.title`): Card and case-card titles; the careers role title runs
  smaller (`clamp(15px, 1.6vw, 23px)`).
- **Lede** (`typography.lede`): The sentence under a heading, and the chain's body
  passages, in ink-2 at 1.45–1.55.
- **Body** (`typography.body`): Card copy, table cells, form fields, caveat panels. Body
  measure is capped by `ch`: 46ch on the home feature, 52ch under the ratio line, 60–66ch
  on dark-band copy and caveats, 62ch on chain passages, 70ch on takeaways.
- **Label** (`typography.label`): Uppercase 0.16em metadata. Variants at 0.14em (footer
  column heads, client credit, careers field labels), 0.1em (table caption, case tag),
  0.08em (table column heads), 0.06em (form labels).
- **Figure** (`typography.figure`): Numbers set as display type — the 8.60x ratio line,
  the ruled figure column on the home card, the inline figures inside a chain passage,
  the 280M results band (`clamp(72px, 14.49vw, 205px)`, italic, weight 400 — the one
  place Playfair drops below 500).

### Named Rules
**The One Italic Word Rule.** Every display heading carries exactly one italicised
phrase, marked with `<em>`, and nothing else in the heading is italic. It is the
system's signature and it is load-bearing: hero, footer headline, quote, case feature,
case-study statement, every chain heading, the close, and both modal titles all follow
it. On the case-study statement the italic phrase also takes `colors.orange`; on the
dark band it takes `#f0a68c`.

**The Tabular Figure Rule.** Any number set in Playfair at figure scale carries
`font-variant-numeric: tabular-nums`, so a column of figures aligns and a changing
number does not jitter.

**The Measure Rule.** No prose block runs without a `ch` cap. Headings cap at 14–18ch,
ledes and passages at 52–66ch, lists at 70ch.

## Layout

A single centred shell of 1160px with a fluid gutter (`spacing.gut`, 20→48px) is the
only container. Vertical rhythm comes from `padding-block` on `.section`
(`spacing.section`) with a tighter variant (`spacing.section-tight`); internal gaps are
`clamp()` pairs rather than steps off a fixed scale. There is no numeric spacing scale
in the build — gaps are authored per component (24px card grid, 14px rail, 2px role
stack), and that is recorded here as the actual state rather than smoothed into a ramp.

The fixed header reserves `spacing.header` (88px, dropping to 76px under 900px) and
every hero adds it back into its own top padding.

Grids: three equal columns for service cards and case cards; asymmetric two-column
splits elsewhere (`.86fr/1.14fr` strengths, `.92fr/1.08fr` meetups, `1.15fr/1fr` case
feature, `1fr/1fr` approach and page hero). The case-study chain is a two-column grid of
a `4.5rem` number gutter beside the passage.

Breakpoints, in the order the stylesheet applies them: 1320px and 1100px (hero cut-out
geometry only), 1080px (strengths and footer collapse), 900px (nav becomes a drawer,
all card grids go single-column, loose props and hero cut-outs hide, two-column splits
stack), 860px (case feature stacks), 760px (chain stacks, wide table scrolls), 640px
(footer to two columns, rail buttons hide, modal titles shrink), 400px (brand wordmark
hides).

### Named Rules
**The Leading-Edge Bleed Rule.** Media and panels break the shell on *one* edge, out to
the viewport, and drop the two corner radii on that edge
(`margin-right: calc((100vw - min(100vw, var(--shell)))/-2 - var(--gut))`). Flipped rows
mirror it. Full-bleed bands use `margin-inline: calc(50% - 50vw)` — the footer art, the
dark case-study band, and the creator rail.

**The Edge-Padded Rail Rule.** Horizontal rails pad their track by
`max(var(--gut), calc((100vw - var(--shell))/2 + var(--gut)))` and set
`scroll-padding-inline` to match, so the first card starts on the shell's left edge
while the track itself runs to the viewport.

## Elevation & Depth

Hybrid, and warm. Surfaces are tonally layered (paper → cream → near-white card → ink
band) and then lifted with a large, soft, *tinted* shadow. Shadows are never neutral
black on paper: they are ink-brown `rgba(26,24,23, .08–.24)`, orange
`rgba(209,74,34, .28–.36)` under the primary button, and `rgba(255,115,66,.24)` under
the hot-orange slab. Glass is the third depth device: `backdrop-filter: blur() saturate()`
on the stuck header, the footer panel, the open careers role, the mobile nav drawer, and
both modal surrounds.

### Shadow Vocabulary
- **Card rest** (`box-shadow: 0 18px 44px rgba(26,24,23,.09)`): Service cards and the
  home case feature at rest.
- **Card lift** (`box-shadow: 0 28px 60px rgba(26,24,23,.14)`): The same card on hover,
  paired with `translateY(-6px)`.
- **Panel** (`box-shadow: 0 30px 70px rgba(26,24,23,.16)`): The footer glass panel and
  the explainer player frame.
- **Media** (`box-shadow: 0 28px 66px rgba(26,24,23,.18)`): Meetup photography and the
  video rails; rail thumbnails use the lighter `0 12px 30px rgba(26,24,23,.12)`.
- **Action warm** (`box-shadow: 0 8px 22px rgba(209,74,34,.28)` → `0 12px 28px rgba(209,74,34,.36)`):
  Primary button rest → hover.
- **Floating control** (`box-shadow: 0 8px 22px rgba(0,0,0,.1–.14)`): Circular rail and
  carousel arrows, ghost buttons.
- **Modal** (`box-shadow: 0 40px 90px rgba(0,0,0,.4–.5)`): Both dialog surfaces.
- **Prop drop** (`filter: drop-shadow(0 12px 22px rgba(26,24,23,.18))`): Halftone
  stickers and the hero cut-outs (`0 22px 40px rgba(0,0,0,.3)`) — a filter, not a
  box-shadow, because the art has a cut-out silhouette.
- **Stuck header** (`box-shadow: 0 1px 0 var(--line), 0 10px 30px rgba(0,0,0,.06)`): A
  hairline plus a whisper, never a hard bar.

### Named Rules
**The Warm Shadow Rule.** A shadow takes the hue of what casts it. Ink-brown on paper,
orange under orange. A neutral `rgba(0,0,0,…)` shadow is reserved for controls that
float over photography or video.

**The Lift Rule.** Interactive surfaces respond by moving up, not by growing:
`translateY(-2px)` for buttons and circular controls, `-5px`/`-6px` for cards. Only
media inside a frame scales (`1.02`–`1.06`), and only behind `overflow: hidden`.

## Shapes

Two form languages coexist deliberately. **Actions are pills** — `rounded.pill` (999px)
for every button, solid tag, outline chip, and the "tap for sound" nudge; `50%` for the
twelve circular controls (nav toggle, rail arrows, carousel arrows, play buttons, sound
toggles, modal closes). **Content is a soft rectangle** — `rounded.md` (18px) for cards,
case cards, reels, creator videos, and caveat panels; `rounded.lg` (28px) for the big
surfaces: footer panel, meetup media, video player frames, the home case feature, and
the contact dialog.

The one hard-edged element is the strengths slab, at 6px — a flat slab rather than a
pill, matching the source design.

Borders are hairlines only: 1px at 6–22% ink on light surfaces, 1px at 16–70% white over
photography and glass. The chain's vertical connector is a 1px orange rule at 30% alpha
dropping from the number. Masks do the work that a border would otherwise do: the hero
background, the footer art, and the mobile wide-table edge all dissolve with a
`linear-gradient` mask instead of ending on a line.

### Named Rules
**The Pill-Or-Slab Rule.** A thing you click is a pill or a circle. A thing you read sits
in a soft rectangle. Nothing in the system is both.

**The Dropped-Corner Rule.** When a surface bleeds past the shell, the two corners on the
bleeding edge go to 0. The radius marks where the shell is, so it never floats on an edge
that has no edge.

**The Dead-Token Note.** `rounded.sm` (10px) and `rounded.xl` (40px) are declared in
`:root` and used nowhere. Four raw radii are in use instead (14px on the glass box, rail
thumbnails and role rows; 12px on form inputs; 8px on card media and jump-list rows; 6px
on the slab and inline code). Recorded as incumbent drift, not repaired.

## Components

### Buttons
Confident and compact: a tight pill that lifts.
- **Shape:** Full pill (`rounded.pill`), `inline-flex` with a `.5em` gap for an icon.
- **Primary:** Orange fill, white text, warm orange shadow; `0.82em 1.5em` padding,
  weight 600, `line-height: 1`, `white-space: nowrap`.
- **Hover / Focus:** `translateY(-2px)` with the shadow deepening; hover fill becomes
  `colors.orange-deep`. Transitions run 0.25s on background, color, transform, shadow.
  Focus is global: `2px solid var(--orange)` at `3px` offset.
- **Ghost:** 94%-white fill, ink text, neutral float shadow; hover goes to solid white.
  Used over photography.
- **Dark:** Ink fill, white text; hover to `#000`. Used inside the careers accordion.
- **Small:** `0.62em 1.15em` at `0.83rem` — the one place the system steps outside its
  `clamp()` type ramp.

### Chips
- **Outline chip** (`.case__tag`): Transparent with a 22%-ink hairline, uppercase
  0.1em label in ink-2, full pill. The "Case Study" marker.
- **Solid tag** (`.tag`): Orange fill, white text, full pill — and set in *Playfair*,
  not Figtree, which is unusual for a label and is a real characteristic of the
  activities page.

### Cards / Containers
- **Corner Style:** `rounded.md` (18px); the home case feature and footer panel use
  `rounded.lg` (28px).
- **Background:** Service cards take a near-white vertical gradient
  (`#fffefb → #faf7f0`, also used by the contact dialog, untokenized); case cards and
  the case feature take `colors.cream`.
- **Shadow Strategy:** Card rest → card lift (see Elevation).
- **Border:** Service cards carry a 6%-ink hairline; cream cards carry none.
- **Internal Padding:** `14px 14px 22px` (service card, media flush to three edges),
  `20px 20px 24px` (case card), `clamp(26px, 3.4vw, 52px)` (case feature).
- **Media:** 8px radius inside the card, `3/2` aspect, image scales to 1.06 on card
  hover behind `overflow: hidden`.

### Inputs / Fields
- **Style:** White fill, 18%-ink hairline, 12px radius, `0.78em 0.95em` padding, body
  type inherited from the form. Labels are uppercase 0.06em in ink-2; the optional
  marker drops to ink-3 sentence case.
- **Focus:** Border becomes `colors.orange` and a `3px` orange glow ring at 14% alpha
  replaces the default outline.
- **Error:** `#c0392b` border with a matching 12% ring, and a small `#c0392b` message
  row that collapses when empty. Success status is `#1e7a4d`. Both hexes are
  untokenized.
- **Disabled:** Submit drops to `0.6` opacity with pointer events off.

### Navigation
- **Style:** Fixed 88px header that starts transparent over a dark-to-clear gradient
  with white links, then flips on scroll (`.is-stuck`) to 92%-white glass with
  `saturate(160%) blur(14px)`, ink links, and a hairline-plus-whisper shadow.
- **Links:** Figtree 500 at `typography` nav size, with a 1.5px `currentColor`
  underline that scales in from the left over 0.28s on hover and stays scaled for
  `[aria-current="page"]`, which also goes weight 700.
- **Mobile (≤900px):** The underline is dropped, the nav becomes a fixed full-width
  98%-white blurred drawer under the header, links become 1.05rem rows separated by
  hairlines, and a 44px circular hamburger morphs into an X with two rotated 1.6px bars.

### The Halftone Prop System
Cut-out props from the source design, placed absolutely against a section or a grid,
rotated 3–22° using the `rotate` property (so `transform` stays free for motion), and
floated with a `wbb-float` keyframe that translates ±`--float` (6–11px) over a
6.2–9.4s alternating cycle with negative delays so no two props are in phase. Every prop
is `aria-hidden` in markup and `pointer-events: none` in CSS. Props above a grid are
sized by a `--prop` variable and the grid's top margin is derived from
`calc(var(--prop) * 1.3 + gap)` — the 1.3 budgets a rotated element's diagonal plus the
float, so a prop can never reach into the copy. Below 900px the loose props and hero
cut-outs hide, and the strengths collage reflows from a free scatter into a two-up grid.

### The Chain (case-study passage)
The signature of the newest surface. Each link is a two-column grid: a `4.5rem` gutter
carrying the sequence number in Playfair 500 at `colors.orange-deep` with tabular
figures, and a 1px orange rule at 30% alpha dropping from it to the next link; beside
it a headline capped at `18ch` and a passage capped at `62ch`. Links are separated by a
14%-ink hairline, with the last link's border and connector removed. Figures appear
*inside* a passage as a flex row of label-under-number pairs, so they read as prose
rather than as a tile grid. Below 760px the grid collapses to one column and the
connector hides.

### Creator / Reels Video Rail
Portrait video cards in a snapping horizontal scroller. `9/16` aspect, `rounded.md`,
ink backing, scrollbar hidden on both engines, `scroll-snap-type: x mandatory`,
`scroll-snap-align: start`. A play overlay sits over a bottom-weighted scrim and is
removed from the tab order with `visibility` (not opacity alone) once playing; a 34–38px
circular sound toggle fades in bottom-right and takes an orange fill when unmuted. Cards
lift 5px on hover. The reels variant on the home page keeps a fixed height and lets
width follow each clip's own `--ar`, so a landscape clip cannot overflow a phone.

### Modals
Both dialogs share one surround: fixed full-viewport, `rgba(20,16,14,.74)` with a 10px
backdrop blur, opened by toggling `.is-open` with the visibility transition delayed so
the dialog is non-interactive while fading, and `overflow: hidden` latched onto both
`html` and `body`. The dialog enters from `translateY(20px) scale(.97)` on a
`cubic-bezier(.22,1,.36,1)` spring over 0.42–0.45s, and every transition is removed
under `prefers-reduced-motion`. The video popup sits at `z-index: 120`, the contact
popup at 130, above the header's 80.

### Reveal
A single scroll-reveal primitive: `.reveal` starts at `opacity: 0` and
`translateY(26px)`, and `.is-in` releases both over 0.7s on
`cubic-bezier(.4, 0, .2, 1)`. Under `prefers-reduced-motion` the reveal is shown
outright and all animation and transition durations collapse to 0.01ms.

### Browser Surfaces
Site-wide, added with the case-study build: selection is `rgba(209,74,34,.22)` behind
ink text, and the scrollbar is themed to the system — an 11px track, a 26%-ink thumb at
99px radius inset by a 3px `colors.paper` border, going to 42% on hover, with
`scrollbar-color` set for Firefox. The one consequence to remember: because the
scrollbar is quiet, any horizontally scrolling region needs its own cue — the wide
comparison table adds both a masked fading right edge and a visible scroll hint below
760px.

## Do's and Don'ts

### Do:
- **Do** use `colors.orange` as a fill behind white and `colors.orange-deep` for orange
  type below 24px (4.98:1 on paper).
- **Do** give every display heading exactly one `<em>` italic phrase — the One Italic
  Word Rule — and nothing else in italic.
- **Do** set every figure in Playfair 500 with `font-variant-numeric: tabular-nums`,
  and let it live inside a sentence, a ruled column, or an inline row rather than a
  stat tile.
- **Do** cap every text block with a `ch` measure: 14–18ch headings, 52–66ch prose,
  70ch lists.
- **Do** drop the two corner radii on any edge where a surface bleeds past the 1160px
  shell.
- **Do** tint shadows to their caster — ink-brown on paper, orange under orange — and
  keep them large and soft.
- **Do** answer interaction with a 2–6px upward lift; scale only media inside a clipped
  frame.
- **Do** mark every decorative prop `aria-hidden` and `pointer-events: none`, and
  budget its band at `calc(var(--prop) * 1.3 + gap)` so it cannot reach the copy.
- **Do** honour `prefers-reduced-motion` in every new component: the stylesheet already
  zeroes durations globally, so new transitions must not reintroduce motion through
  inline styles or JS.
- **Do** give a horizontally scrolling region its own visual cue, because the themed
  scrollbar is deliberately quiet.
- **Do** derive new type sizes as `clamp()` off the same proportions (design px ÷ 1162px
  canvas) rather than adding fixed sizes.

### Don't:
- **Don't** set small text in `colors.ink-3` on paper. It measures 4.27:1 and fails AA.
  The incumbent `.eyebrow`, footer legal row, scroll hints and placeholders all do this;
  new surfaces should not extend it.
- **Don't** put an eyebrow or kicker label above a heading. The heading carries its own
  weight, and the newest surface opens on the statement with only the client mark above
  it.
- **Don't** ship an arrow or icon as a text glyph or HTML entity. Inline SVG, as the
  case-study link and the creator rail do.
- **Don't** introduce a fourth hue. If a state needs a color, derive it from the orange
  or ink families rather than adding a semantic palette.
- **Don't** add a new corner radius. Pill, 50%, 18px, 28px and the 6px slab cover the
  whole system.
- **Don't** put the orange wash on a card, panel, or form. The wash belongs to the
  section behind them.
- **Don't** set Playfair above weight 500. The variable font loads to 700 and the system
  never uses it.
- **Don't** let a modal open without latching `overflow: hidden` on both `html` and
  `body` and delaying the visibility transition — opacity alone leaves the dialog
  clickable while invisible.
- **Don't** use `overflow: hidden` on `html`/`body` for horizontal clipping; the system
  uses `overflow-x: clip` with a `@supports` fallback, because `hidden` would make
  `<body>` a scroll container and break the fixed header.
