# Pull Request How-To Guide

This guide explains how to create a pull request for the django-ace project.

## Prerequisites

- Fork the repository on GitHub
- Clone your fork locally
- Install GitHub CLI: `brew install gh` (or see [GitHub CLI installation](https://cli.github.com/))
- Authenticate with GitHub: `gh auth login`

## Manual Process

### 1. Create a Feature Branch
```bash
git checkout -b feature-name
```

### 2. Make Your Changes
- Edit the necessary files
- Test your changes
- Update examples if needed

### 3. Commit Your Changes
```bash
git add .
git commit -m "Your commit message"
```

### 4. Push and Create PR
```bash
# Push your branch
git push -u origin feature-name

# Set default repo (only needed once)
gh repo set-default django-ace/django-ace

# Create the PR
gh pr create --title "Your PR Title" --body "Your PR description"
```

## Automated Process

Use the provided script for a streamlined workflow:

```bash
./create-pr.sh "feature-name" "Your PR title" "Your commit message"
```

## PR Best Practices

### Commit Messages
- Use present tense: "Add feature" not "Added feature"
- Be descriptive but concise
- Reference issues if applicable: "Fixes #123"

### PR Titles
- Clearly describe what the PR does
- Use imperative mood: "Add vim keybinding support"
- Be specific and concise

### PR Description
- Explain what changes were made and why
- Include usage examples for new features
- Mention any breaking changes
- Add testing instructions if relevant

### Code Quality
- Follow existing code style
- Add tests for new features
- Update documentation
- Ensure backward compatibility

## Common Commands

```bash
# Check current branch
git branch --show-current

# Check status
git status

# See what files changed
git diff --name-only

# View PR status
gh pr status

# Check out someone else's PR for testing
gh pr checkout 123
```

## Troubleshooting

### "No default remote repository"
```bash
gh repo set-default django-ace/django-ace
```

### "Branch already exists"
```bash
git checkout main
git branch -D old-branch-name
git checkout -b new-branch-name
```

### "Nothing to commit"
Make sure you've made changes and added them:
```bash
git add .
git status
```

## Example Workflow

```bash
# 1. Start from main branch
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b add-new-feature

# 3. Make changes
# ... edit files ...

# 4. Commit changes
git add .
git commit -m "Add new feature with examples"

# 5. Create PR using script
./create-pr.sh add-new-feature "Add new feature support" "Add new feature with examples"
```