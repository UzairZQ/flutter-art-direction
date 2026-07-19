# Mobile Visual Direction and Image Concepts

Use this reference for image-only mobile concepts, concept-then-build exploration, multi-screen flows, or any Flutter task where the visual system needs stronger taste, imagery, texture, or presentation discipline.

## Contents

- Output contract
- Platform mode
- Visual-direction profile
- Screen count and flow
- Multi-screen consistency
- Device presentation
- Composition and readability
- Imagery, texture, and decorative assets
- Navigation and mobile reality
- Prompt construction
- Concept-to-Flutter translation
- Regeneration and delivery gate

## Output Contract

Choose one mode before working:

### Concept

Generate the requested mobile screen images. Do not replace the deliverable with prose or code. Keep concepts believable enough to guide implementation, but do not claim that generated controls, text, or geometry are production-ready.

### Build

Implement in Flutter and verify rendered output. Do not spend the task on image concepts unless visual uncertainty makes a small exploration materially useful.

### Concept then build

Generate the smallest useful set of directions, select transferable decisions, and rebuild them in Flutter. Concepts supply art-direction evidence; the Flutter render, states, accessibility, and performance determine completion.

## Platform Mode

Choose one dominant mode and preserve it across the set.

### iOS-native premium

- restrained chrome and calm top areas
- clear tab bars, sheets, safe areas, and back behavior
- elegant spacing and native-feeling hierarchy
- custom identity in content, material, imagery, and signature interaction rather than unfamiliar system behavior

### Android-native premium

- explicit app-bar and navigation behavior
- clear component rhythm, sheets, lists, and state feedback
- Material as a behavioral base, not the complete identity
- predictive back, system bars, and platform reachability preserved

### Cross-platform premium

- shared product identity with adaptive system behavior
- universal mobile hierarchy and safe-area discipline
- platform-specific back, text input, scrolling, selection, and sheets where expectations are strong
- no careless mixture of iOS and Android ornament

## Visual-Direction Profile

Lock a compact profile before producing multiple screens. Choose only what serves the product; the lists are variation tools, not mandatory aesthetics.

### Theme paradigm: choose one

- pristine light
- deep dark
- soft neutral
- premium monochrome
- rich accent-driven
- editorial luxe
- playful consumer color
- calm productivity

### Typography character: choose one

- clean system-like sans
- refined grotesk
- expressive display with quiet body
- soft humanist sans
- sharp product sans with disciplined hierarchy

### Structure bias: choose one primary bias

- list-led utility
- modular overview
- dashboard-led decision support
- media-led storytelling
- profile-led identity
- commerce browse-and-detail
- conversation-led flow
- calm block rhythm

Do not force every screen into the same structure. The bias supplies a home rhythm, not a cloned template.

### Image direction: choose one when imagery matters

- editorial photography
- cinematic lifestyle
- soft illustration
- tactile abstract composition
- premium product imagery
- mixed photo and vector
- atmospheric backdrop
- restrained layered collage

### Texture and surface: choose one dominant treatment

- ultra-subtle grain
- matte paper
- foggy tonal atmosphere
- soft noise wash
- blurred image haze
- flat system with one textured focal area
- tactile monochrome
- low-opacity product-specific pattern

### Palette logic: choose one

- restrained monochrome plus one accent
- warm neutral plus sharp dark contrast
- cool mineral plus clean highlight
- cream, charcoal, and one muted accent
- rich dark base plus refined warm accent
- soft low-saturation family
- bright consumer color with disciplined balance
- desaturated field plus one bold hit

Define semantic roles after choosing the logic: base, raised surface, primary text, quiet text, main action, selection, attention, destructive, success, and focus. Color must not be the only state signal.

### Signature components: choose one to four

Choose components that belong to the product's repeated jobs, such as a route spine, recovery arc, journal block, collection shelf, message system, progress range, bottom action sheet, segmented control, or product-specific detail panel. Do not select a component merely because it looks impressive.

### Decorative assets: choose zero to two

Examples include dotted guide arcs, a fine product-specific grid, a tiny directional marker system, a restrained line-art cluster, an abstract orbit, or a soft waveform. Decorative assets must reinforce the product world or spatial model.

### Motion-implied language: choose one or two

Concept images may imply sheet rise, calm tab continuity, staggered list orientation, direct drag progress, carousel glide, or parallax depth. Record the real Flutter motion purpose and reduced-motion result before implementation.

## Screen Count and Flow

- Generate the number of screens requested. Do not compress a multi-screen request into one unreadable board.
- For an open-ended app concept, choose the smallest set that proves the core journey, usually entry or home, primary task, and result or management state.
- Generate each screen as a fresh standalone image when readability matters.
- Add a detail render when it clarifies a form, sheet, interaction, or component that a full-screen view cannot show clearly.
- Never crop a small screen or control out of a larger concept and present it as a new render.
- Carry state logically: selected item, draft, route stop, cart, filter, permission, or progress should persist into the next screen.
- Make every transition answer why the next screen exists and how the user reached it.

## Multi-Screen Consistency

Keep these fixed unless the brief explicitly changes mode:

- platform stance and system behavior
- device style, scale, and presentation background
- palette roles and contrast logic
- typography family and role scale
- spacing rhythm and touch-target policy
- corner and shape grammar
- icon family, stroke or fill logic, and optical weight
- image crop and treatment
- texture intensity
- navigation model
- button hierarchy
- shadow and elevation language

Vary these to avoid cloned screens:

- top-area composition
- density and whitespace
- list, form, media, or detail emphasis
- image-to-text balance
- CTA location
- background treatment within the locked material system
- visual tempo and information grouping

Consistency means one product under changing content, not identical layouts.

## Device Presentation

For presentation concepts, default to one subtle premium phone frame that supports the screen.

- keep the full frame visible and uncropped
- use even top, bottom, left, and right canvas margins
- keep scale and bezel style identical across the set
- use a restrained shadow and quiet background
- keep the screen content larger and more important than the hardware
- avoid hands, desks, props, or multiple devices unless the user asks for a marketing composition
- use one device per image when text readability matters

Use raw screen output instead when:

- the user requests it
- the image is a direct implementation reference
- device chrome would reduce useful resolution
- the deliverable is a UI sheet or asset rather than a presentation mockup

Never trace a generated status bar, home indicator, notch, or bezel into Flutter app content.

## Composition and Readability

- Give the first screen one primary focal point, one dominant action, and a controlled top region.
- Use hierarchy through alignment, spacing, typography, dividers, image scale, and contrast before adding containers.
- Keep body copy, field labels, navigation, and actions comfortably readable at normal image size.
- Split content across screens before shrinking type.
- Use cards only for real boundaries, repeated objects, interaction, or elevation.
- Keep the primary action reachable and visually stable.
- Respect status, safe-area, keyboard, bottom-navigation, home-indicator, and gesture regions.
- Make a screen understandable without texture, imagery, or motion.
- Inspect at thumbnail size for hierarchy and full size for type, alignment, crop, icon weight, and state clarity.

## Imagery, Texture, and Decorative Assets

Use imagery when it reveals a person, product, place, state, collection, or atmosphere the user cares about. Operational tools may need tactile maps, diagrams, product artifacts, or restrained patterns more than lifestyle photography.

When imagery sits behind text:

- protect readability with a deliberate fade, mask, scrim, or quiet image region
- preserve the meaningful focal point
- avoid muddy overlays and raw opacity tricks
- keep text contrast valid when the image changes or fails

For repeated media:

- define a stable aspect ratio and crop policy
- use consistent radii and loading geometry
- provide failure and semantic-description behavior
- control decode size and memory cost in Flutter

Texture should support material and mood. Keep it subtle enough that text, focus, and state remain clear. Prefer one dominant material idea over several unrelated effects.

Use custom-feeling iconography through coherent geometry, weight, corner logic, and product-specific symbols. Do not reject an icon library automatically; adapt or supplement it when default symbols make the product interchangeable.

## Navigation and Mobile Reality

- Use bottom navigation for a small number of stable top-level destinations.
- Use stack navigation for drill-down tasks and preserve back behavior.
- Use sheets for bounded secondary work, not as a universal container.
- Use segmented controls for local mode changes with a visible selected state.
- Keep one primary gesture per region and provide a visible alternative for custom gestures.
- Do not place a website hero, desktop dashboard, hover model, or scroll hijack inside a phone frame.
- Keep generated navigation labels and screen order believable even when the concept is not executable.

## Prompt Construction

For image generation, write one prompt per distinct screen. Keep a shared design-bible block verbatim across prompts, then describe the screen-specific job and composition.

Include:

1. use case and screen number
2. platform mode
3. exact presentation contract: raw screen or full device, device style, scale, background, and margins
4. locked design bible: palette, type, spacing, radii, iconography, imagery, texture, navigation, and surface logic
5. screen job, primary action, state, and connection to the previous or next screen
6. exact visible copy when text matters
7. hierarchy and composition
8. trust, safety, data, and accessibility constraints
9. explicit anti-generic avoid list relevant to the product

Do not ask one image to contain several small phone screens when the user needs readable screens. Repeat invariants across prompts to reduce drift.

## Concept-to-Flutter Translation

Extract only transferable decisions:

- palette roles, not sampled noise from every pixel
- typography relationship, not necessarily a generated font
- hierarchy and spacing rhythm, not impossible measurements
- shape grammar and component roles
- image crop and texture strategy
- signature interaction and continuity model
- navigation and state intent

Rebuild with real Flutter constraints:

- use semantic controls and adaptive platform behavior
- test text scaling, localization, keyboard, safe areas, and small widths
- implement loading, empty, error, offline, permission, focus, pressed, selected, disabled, and success states where relevant
- size and cache images correctly
- profile blur, filters, clipping, opacity groups, custom painting, shaders, and particles
- add reduced-motion behavior before declaring motion complete

Generated text, exact spacing, device chrome, shadows, and decorative artifacts are not production truth.

## Regeneration and Delivery Gate

Regenerate a concept when:

- text is too small, malformed, or crowded
- the first screen lacks a clear focal point
- safe areas or navigation look implausible
- the phone frame is cropped, uneven, oversized, or inconsistent
- a screen drifts in palette, typography, icon family, material, or device style
- the flow is random or state does not carry forward
- the layout looks like a website or generic dashboard
- cards, pills, badges, charts, or gradients appear without a product reason
- imagery is filler, texture is noisy, or decorative assets lack meaning
- the concept is boring because product-specific visual evidence is absent

Before delivery, verify:

- requested screen count and one image per readable screen
- logical flow and state continuity
- consistent design bible and device presentation
- comfortable text and control size
- purposeful imagery, texture, and decorative assets
- controlled, non-generic palette
- believable mobile navigation and safe areas
- no fabricated data, testimonials, precision, claims, or user information
- full-size and thumbnail inspection
- honest distinction between concept quality and production Flutter readiness
