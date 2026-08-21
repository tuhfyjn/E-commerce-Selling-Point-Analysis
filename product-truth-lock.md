# Product Truth Lock

The Product Truth Lock prevents AI-generated commerce images from drifting away from the actual SKU.

## Capture

### Geometry
- overall silhouette
- proportions
- curvature
- thickness
- relative dimensions

### Components
- buttons
- ports
- cameras
- displays
- hinges
- openings
- straps
- detachable parts

### Brand
- logo location
- label location
- packaging identity

### Surface
- primary color
- accent color
- matte / gloss / translucent / metallic finish
- visible texture

### Verified facts
- size
- weight
- capacity
- runtime
- performance
- compatibility
- package contents

## Forbidden mutations

Explicitly list what the image generator must not change.

Example:

```text
Do not:
- move the camera module
- change the ear-hook geometry
- add LED strips
- remove the charging port
- alter the apricot-white silicone color
- invent accessories
```

## Missing-view rule

If a hidden side of the product is not visible in any reference:
- do not invent a detailed structure
- prefer angles that preserve known geometry
- request another reference image when accuracy matters
