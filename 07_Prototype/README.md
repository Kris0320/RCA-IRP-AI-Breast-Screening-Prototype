# AI-Human Disagreement Support Prototype

Static interactive prototype for an AI-human disagreement support layer in breast screening.

## Run Locally

From this folder:

```bash
python3 -m http.server 8002
```

Then open:

```text
http://localhost:8002/
```

Use a local server rather than opening `index.html` with `file://`, so browser asset loading matches deployment.

## Deploy to Vercel

1. Create a new Vercel project.
2. Set the project root to this folder: `07_Prototype`.
3. Use the default static site settings.
4. No build command is required.
5. The output directory can be left blank.

Vercel will serve `index.html` as the site entry point.

## Files

- `index.html` - main prototype page
- `assets/` - required mammography image assets
