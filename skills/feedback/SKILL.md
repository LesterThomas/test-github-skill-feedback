---
name: feedback
description: Collect, structure, and manage user feedback about features, bugs, or improvements. Use when users want to provide feedback, report issues, suggest improvements, or when you need to gather structured input from users.
license: MIT
metadata:
  author: lesterThomas
  version: "1.0"
---

# Feedback Skill

This skill helps agents collect and structure user feedback in a consistent, organized way.

## When to use this skill

Use this skill when:
- Users want to provide feedback about a feature or experience
- Users report bugs or issues
- Users suggest improvements or new features
- You need to gather structured input about user preferences
- You need to document user concerns or requests

## Instructions

### 1. Identify the feedback type

First, determine what type of feedback the user is providing:
- **Bug Report**: Something isn't working as expected
- **Feature Request**: User wants new functionality
- **Improvement**: Suggestion to enhance existing functionality
- **General Feedback**: Comments about user experience or opinions

### 2. Gather structured information

Collect relevant details based on the feedback type:

#### For Bug Reports:
- Description of the issue
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (OS, version, etc.)
- Screenshots or error messages if available

#### For Feature Requests:
- Description of desired functionality
- Use case or problem it solves
- Priority level (nice-to-have, important, critical)
- Any relevant examples or references

#### For Improvements:
- What currently exists
- Proposed improvement
- Expected benefit
- Any trade-offs to consider

#### For General Feedback:
- Topic or area of feedback
- Specific comments or observations
- Sentiment (positive, negative, neutral)
- Actionable items if any

### 3. Structure the feedback

Format the collected feedback in a clear, consistent structure:

```markdown
# Feedback: [Title]

**Type**: [Bug Report | Feature Request | Improvement | General Feedback]
**Date**: [YYYY-MM-DD]
**Submitted by**: [User identifier if available]

## Description
[Detailed description of the feedback]

## Details
[Relevant details based on feedback type]

## Additional Context
[Any other relevant information]

## Status
- [ ] Submitted
- [ ] Under Review
- [ ] In Progress
- [ ] Completed
```

### 4. Save or output the feedback

Create a feedback file or document with the structured information. Use a consistent naming convention like:
- `feedback-YYYY-MM-DD-brief-title.md`

### 5. Provide confirmation

After collecting and structuring the feedback, confirm with the user that you've captured their input correctly and let them know what happens next.

## Examples

### Example 1: Bug Report

User: "The login button doesn't work on mobile devices"

Agent should:
1. Identify this as a bug report
2. Ask clarifying questions about device type, browser, error messages
3. Structure the feedback with reproduction steps
4. Save to a feedback file

### Example 2: Feature Request

User: "It would be great if we could export data to CSV"

Agent should:
1. Identify this as a feature request
2. Ask about use case and specific data they want to export
3. Structure the request with priority and benefits
4. Document the request

## Best Practices

- Always thank the user for their feedback
- Ask clarifying questions politely
- Don't make promises about implementation timelines
- Keep feedback files organized and searchable
- Use consistent formatting across all feedback items
- Tag feedback with relevant categories or labels when possible
