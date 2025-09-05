# CI/CD Practice Pipelines

This repo is where I practised setting up GitHub Actions pipelines for different languages. The goal was simple: learn how to automate versioning, tagging, releases, and publishing (all key parts of modern software delivery) for libraries in `Java`, `JavaScript`, and `Go`.

## What it does
- It lets me pick a language (Java, JavaScript, Go) and version type (major, minor, patch) when triggering the workflow.
- Figures out the current version (from pom.xml, package.json, or git tags).
- Bumps the version number automatically.
- Commits the change, creates a git tag, and pushes it.
- Builds the project and (optionally) publishes to GitHub Packages.
- Creates a GitHub Release.
  
### Why I built this
I wanted to get comfortable with:
- Writing conditional jobs in GitHub Actions
- Automating semantic versioning
- Publishing packages (Maven, npm, Go modules)
- The overall flow of “code → version → release”

### Repo Structure
```bash
cicd-go/   → sample Go project
cicd-java/   → sample Java project
cicd-js/     → sample JavaScript project
.github/workflows/ → pipeline configs
```



