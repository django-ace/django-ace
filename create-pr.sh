#!/bin/bash

# create-pr.sh - Automated PR creation script for django-ace
# Usage: ./create-pr.sh [branch-name] [pr-title] [commit-message]

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    print_error "GitHub CLI (gh) is not installed. Install it with: brew install gh"
    exit 1
fi

# Get parameters or prompt for them
if [ $# -eq 0 ]; then
    echo "=== Django-Ace PR Creation Script ==="
    echo
    read -p "Enter branch name (e.g., add-new-feature): " BRANCH_NAME
    read -p "Enter PR title: " PR_TITLE
    read -p "Enter commit message: " COMMIT_MESSAGE
elif [ $# -eq 3 ]; then
    BRANCH_NAME="$1"
    PR_TITLE="$2"
    COMMIT_MESSAGE="$3"
else
    echo "Usage: $0 [branch-name] [pr-title] [commit-message]"
    echo "   or: $0 (for interactive mode)"
    exit 1
fi

# Validate inputs
if [ -z "$BRANCH_NAME" ] || [ -z "$PR_TITLE" ] || [ -z "$COMMIT_MESSAGE" ]; then
    print_error "All parameters are required"
    exit 1
fi

print_status "Starting PR creation process..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "Not in a git repository"
    exit 1
fi

# Check if we have uncommitted changes
if ! git diff-index --quiet HEAD --; then
    print_status "You have uncommitted changes. Staging all changes..."
    git add .
fi

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
print_status "Current branch: $CURRENT_BRANCH"

# If we're not on the feature branch, create and switch to it
if [ "$CURRENT_BRANCH" != "$BRANCH_NAME" ]; then
    if git show-ref --verify --quiet refs/heads/"$BRANCH_NAME"; then
        print_warning "Branch $BRANCH_NAME already exists. Switching to it..."
        git checkout "$BRANCH_NAME"
    else
        print_status "Creating new branch: $BRANCH_NAME"
        git checkout -b "$BRANCH_NAME"
    fi
fi

# Check if there are changes to commit
if git diff-index --quiet HEAD --; then
    print_warning "No changes to commit"
else
    print_status "Committing changes..."
    git commit -m "$COMMIT_MESSAGE"
    print_success "Changes committed"
fi

# Push the branch
print_status "Pushing branch to origin..."
if git push -u origin "$BRANCH_NAME" 2>/dev/null; then
    print_success "Branch pushed successfully"
else
    print_status "Branch already up to date"
fi

# Set default repository if not set
print_status "Checking GitHub CLI configuration..."
if ! gh repo set-default --help &> /dev/null; then
    print_error "GitHub CLI not properly configured. Run: gh auth login"
    exit 1
fi

# Try to set default repo (will skip if already set)
gh repo set-default django-ace/django-ace 2>/dev/null || true

# Create the pull request
print_status "Creating pull request..."
if [ -f "PR_SUMMARY.md" ]; then
    print_status "Using PR_SUMMARY.md for PR description"
    gh pr create --title "$PR_TITLE" --body-file PR_SUMMARY.md
else
    print_status "Creating PR with basic description"
    gh pr create --title "$PR_TITLE" --body "## Summary

$COMMIT_MESSAGE

## Changes
- TODO: Describe your changes here

## Testing
- TODO: Describe how to test your changes

## Backward Compatibility
- TODO: Confirm backward compatibility or describe breaking changes

🤖 Generated with create-pr.sh script"
fi

print_success "Pull request created successfully!"

# Show PR status
print_status "PR Status:"
gh pr status

print_success "Done! Your PR is ready for review."
echo
echo "Next steps:"
echo "1. Check the PR URL above and verify everything looks correct"
echo "2. Add any additional reviewers if needed"
echo "3. Watch for feedback and be ready to make changes"
echo
echo "Useful commands:"
echo "  gh pr status                    # Check PR status"
echo "  gh pr view                      # View your PR"
echo "  gh pr edit                      # Edit PR title/description"
echo "  git checkout main               # Switch back to main branch"