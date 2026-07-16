# Flutter Art Direction Principle Bank

Use this reference to choose a direction, interpret references, or repair a design that feels generic. Select a small set of relevant principles. Do not apply every principle to every app.

## Contents

- Product truth and authorship
- Emotional and behavioral fit
- Composition and material
- Reference-inspired lessons
- Category lenses
- Reference translation method

## Product Truth and Authorship

### Start with the user's world

Art direction begins with the product's actual content, not a palette.

Identify:

- objects the user manipulates
- units of progress or value
- environmental context: commute, gym, bed, field work, desk, bright outdoors
- emotional risk: shame, urgency, uncertainty, boredom, delight
- domain language and visual artifacts

Turn those facts into a product world. A cultural archive might use field notes, catalog labels, material textures, and spatial discovery. A budgeting tool might use ledgers, envelopes, thresholds, and calm precision. The metaphor should clarify behavior, not merely decorate it.

### Create one ownable rule

Choose one recurring visual or interaction rule that would still identify the product without its logo:

- entries unfold from a time spine
- recovery is shown as a breathable range rather than a score
- artifacts retain their physical scale while context moves around them
- tasks compress into a visible daily horizon
- spending categories behave like bounded containers

Repeat the rule with variation. Authorship comes from consistency under changing content, not from a collection of unrelated effects.

### Let real content shape composition

Do not decide on a card grid before inspecting the content. Use the information's natural differences:

- one dominant item and several supporting items
- a chronological sequence
- comparison between two states
- continuous range
- collection for browsing
- action followed by confirmation

Different information structures deserve different compositions. Repeating one component shape for all of them makes a screen feel generated.

### Preserve useful irregularity

A design system should make decisions coherent, not mathematically identical. Keep repeated roles consistent while allowing product-specific elements to break the grid intentionally.

Tokenize semantic repetition:

- surface roles
- text roles
- standard insets
- component states
- motion families

Keep bespoke geometry local:

- illustration offsets
- custom paths
- one-off hero composition
- asset-specific crop and focal point

## Emotional and Behavioral Fit

### Give the app a stance

Define how the product behaves toward the user.

| Stance | Behavioral expression | Avoid |
|---|---|---|
| Calm | quiet hierarchy, gradual disclosure, stable motion | excessive celebration or urgency |
| Encouraging | progress acknowledged without judgment | shame, manipulative streak pressure |
| Precise | crisp feedback, transparent values, undo | ornamental ambiguity |
| Protective | explicit consent, local recovery, clear boundaries | surprise permissions or destructive shortcuts |
| Playful | discovery, tactile response, controlled surprise | motion on every routine action |
| Candid | plain language, visible tradeoffs, honest empty states | inflated claims and fake confidence |

Color and typography alone cannot create this stance. Copy, errors, defaults, haptics, motion, and recovery paths must agree with it.

### Design visceral, behavioral, and reflective layers together

- **Visceral:** the immediate material, color, image, type, and motion impression.
- **Behavioral:** whether interaction is understandable, responsive, forgiving, and efficient.
- **Reflective:** what the product communicates about identity, progress, trust, or meaning over time.

A polished surface with a confusing flow is not authored. A useful flow with no emotional position may be generic. A memorable concept without stable behavior is theatre.

### Make data humane

For health, finance, education, productivity, and wellbeing:

- pair numbers with interpretation
- disclose uncertainty and data freshness
- use ranges when a point estimate would imply false precision
- avoid turning every value into a score
- avoid color-only judgment
- design sparse, missing, delayed, and contradictory data
- let users recover from destructive or high-stakes actions

## Composition and Material

### Use hierarchy before containment

Group content first with alignment, spacing, typography, and dividers. Add a card or elevated surface only when it communicates a real boundary, interaction, or layer.

Avoid nested cards, every-row pills, and one container per fact. They flatten hierarchy because everything receives equal emphasis.

### Choose a shape grammar

Define why shapes differ:

- containers versus controls
- selected versus resting
- foreground versus background
- expressive feature versus routine utility

Material 3 Expressive allows more shape and motion range, but expressive does not mean random. A morph is strongest when it explains a state change.

### Treat imagery as interface

For image-led products, decide:

- focal point and crop behavior
- whether imagery is documentary, illustrative, symbolic, or atmospheric
- how image color influences surrounding surfaces
- loading and failure treatment
- semantic description
- memory and decode cost

Do not use generic stock imagery as proof that a screen is designed. The image must reveal the subject, state, place, or object the user cares about.

### Use material effects sparingly

Blur, glass, shaders, texture, noise, shadows, and particles are valid when they support the product world or focus hierarchy.

Ask:

1. What information does the effect communicate?
2. Is it readable without the effect?
3. Does it remain coherent in light, dark, high-contrast, and reduced-motion modes?
4. Can it run smoothly on the target device?

## Reference-Inspired Lessons

These are principles, not templates.

### Wonderous

Extract:

- a complete product world built from typography, layered art, sound, motion, copy, and interaction
- foreground, middle-ground, and background assets that move at different rates
- direct drag progress that changes zoom, gradient, and route intent together
- Hero continuity between overview and detail
- editorial content built with slivers, pinned structure, and scroll-reactive transforms
- finite celebration effects isolated from the rest of the scene
- explicit reduced-motion and high-contrast policy
- rendering work avoided when an illustration is fully invisible

Do not extract:

- ancient-world motifs
- the exact home composition
- decorative type, textures, or gestures without a matching product reason

### Reflectly

Extract:

- emotional tone as a system, not a single friendly illustration
- guided reflection that reduces blank-page pressure
- soft pacing and approachable language
- focused input moments instead of dense dashboards

Avoid copying its palette, mascot language, or onboarding structure.

### Gentler Streak

Extract:

- a non-punitive stance toward health data
- ranges, readiness, and recovery context instead of shame-driven goals
- readable charts that support a decision
- warmth without hiding precision

### Flighty

Extract:

- dense operational information with clear urgency levels
- live state communicated through hierarchy and timely motion
- information that becomes richer as disruption increases

The lesson is not to make every status screen dark or map-heavy.

### Halide

Extract:

- direct manipulation and tactile controls
- visual restraint around a content-first canvas
- specialist capability revealed progressively
- product-specific controls rather than generic settings forms

### Not Boring, Any Distance, and playful consumer tools

Extract:

- a small number of memorable metaphors
- haptics and motion synchronized with a meaningful event
- expressive visuals that do not block the core task
- celebration proportional to rarity

### Rive and interactive illustration systems

Extract:

- state-driven animation instead of a passive looping movie
- authored transitions between named states
- designer/developer collaboration around a shared motion artifact

Use only when the runtime, asset workflow, accessibility fallback, and maintenance cost fit the project.

## Category Lenses

Use these questions to start, not as visual presets.

### Culture, education, and travel

- What does discovery feel like?
- Can navigation express chronology, geography, or collection?
- Which assets carry authority and provenance?
- What remains usable when imagery fails?

### Journaling and emotional wellbeing

- How does the app lower pressure?
- What does privacy feel like in interaction, not just copy?
- How are difficult days represented without false positivity?
- Can the user enter quickly without completing a ritual?

### Health and fitness

- Does data guide rather than judge?
- Are uncertainty, recovery, and missing readings visible?
- Is celebration proportional and optional?
- Can users understand the next action without decoding a chart?

### Productivity and tools

- What must be scanned in three seconds?
- Which action deserves persistent reach?
- Can density increase without adding containment?
- Does motion preserve position and causality during reordering or filtering?

### Finance

- Can the user distinguish available, pending, projected, and historical values?
- Are destructive and irreversible actions explicit?
- Is precision real and traceable?
- Does the interface remain calm under bad news?

### Commerce and collections

- Does media let the user inspect the actual object?
- Are variants, price, delivery, and availability easy to compare?
- Does motion preserve the selected object across browse and detail?
- Are recommendations visibly grounded rather than fabricated?

## Reference Translation Method

When the user supplies an app, website, or screenshot:

1. Name the specific quality they respond to: depth, pacing, typography, directness, warmth, density, or another property.
2. Identify the mechanism that produces it.
3. Separate mechanism from branding and subject matter.
4. Map the mechanism to the current product's content and emotional stance.
5. Change at least the composition, asset language, and interaction metaphor.
6. Verify that the result still works without the reference beside it.

The goal is recognizable authorship for the new product, not recognizable imitation of the old one.

## Optional Image-Concept Exploration

Use image concepts when the product depends on an unfamiliar visual world, authored illustration, spatial composition, texture, or cinematic atmosphere that is expensive to discover directly in widgets.

Skip them for routine utilities, dense operational screens, minor redesigns, or any task where real data hierarchy is the main design problem.

When concepts help:

1. Generate a small number of meaningfully different directions, not cosmetic color variants.
2. Judge product fit, hierarchy, asset feasibility, accessibility, and mobile reachability before visual novelty.
3. Select transferable decisions: composition, palette roles, material behavior, type relationship, asset treatment, and motion premise.
4. Rebuild with Flutter widgets and real constraints. Do not trace generated text, controls, unsafe spacing, or impossible effects.
5. Verify the implementation against the product brief, not only against the concept image.
