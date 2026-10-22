# Motion and scroll — what we can and cannot infer

## Visible in supplied images
The screenshots show long-form product storytelling, compact product navigation, horizontally scrolling media rails, and sections with substantial vertical spacing. Static images do not prove the exact scroll animation or easing.

## Implementation hypotheses to test
- Keep native browser scrolling; do not hijack wheel/touch scroll.
- Use scroll-triggered reveal only when it adds narrative value. Prefer small opacity/transform changes.
- Avoid many elements animating simultaneously.
- Use horizontal carousels with native overflow or a proven accessible carousel, buttons, keyboard support, and visible focus.
- Keep sticky sub-navigation short, stable, and non-obstructive.
- Use short interaction transitions for buttons and accordions; avoid long entrance animations.
- Honor `prefers-reduced-motion`.
- Test fast wheel scrolling, trackpad, touch, keyboard, and mobile.
- Do not claim "Apple-like smoothness" until the rendered implementation is tested on actual devices/browsers.


## Additional interaction hypotheses from REF-11–REF-20
- Media frames show pause/play affordances; the screenshots do not prove autoplay, looping, or transition timing.
- Segmented controls likely switch the showcased story; implement a stable active state and avoid unexpected layout jumps.
- Feature explorers pair a selected option with a demonstration. If animated, cross-fade or replace content without moving the surrounding layout unnecessarily.
- Carousel arrows and pagination imply discrete navigation. Preserve scroll position and avoid abrupt snapping; test fast repeated navigation and reduced-motion settings.
- Do not infer Apple’s actual easing curves or scroll physics from still screenshots. Capture live video or inspect behavior before matching motion.


## Dark-theme motion cues — REF-21–REF-30
Static screenshots suggest video playback controls, carousel pagination, selectable camera parameters, and a dismissible feature explorer. They do not establish actual timing, autoplay, easing, or scroll behavior. Implement controls with explicit states, avoid forced scroll effects, and test contrast and focus visibility on black surfaces. Use reduced-motion preferences and preserve native scrolling.
