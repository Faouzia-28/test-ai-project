# Test AI Model Project

A sample AI project for testing PromptLedger's GitHub integration and webhook sync.

## Project Structure

- `prompts/` - AI model prompts
- `models/` - Model configurations  
- `tests/` - Test cases for prompts

## Testing with PromptLedger

This repo is set up to sync with PromptLedger. Each commit to tracked paths will:
1. Create a new version
2. Trigger regression evaluations
3. Post commit status back to GitHub
