# Feedback Agent Skill

An Agent Skill for collecting, structuring, and managing user feedback about features, bugs, or improvements.

## Overview

This repository contains a 'feedback' skill following the [Agent Skills](https://agentskills.io/) specification. The skill helps AI agents systematically collect and organize user feedback in a structured format.

## Skill Structure

```
skills/
└── feedback/
    ├── SKILL.md              # Main skill definition and instructions
    ├── scripts/
    │   └── create_feedback.py  # Python script for creating feedback files
    └── references/
        └── TEMPLATE.md       # Feedback templates for different types
```

## Feedback Types Supported

- **Bug Reports**: Issues and problems that need fixing
- **Feature Requests**: New functionality suggestions
- **Improvements**: Enhancements to existing features
- **General Feedback**: User experience comments and observations

## Usage

This skill is designed to be used by AI agents that support the Agent Skills format. When activated, the agent will:

1. Identify the type of feedback being provided
2. Gather relevant structured information
3. Format the feedback using consistent templates
4. Create organized feedback files

## Installation

### For Claude Code (Using This Repository Directly)

This repository includes a symbolic link from `.claude/skills` to the `skills/` directory. To use it:

```bash
git clone https://github.com/LesterThomas/test-github-skill-feedback.git
cd test-github-skill-feedback
```

Claude Code will automatically discover the skill via the `.claude/skills` symlink.

If the symlink doesn't work on your system, create it manually:

```bash
cd test-github-skill-feedback
ln -s ../skills .claude/skills
```

### For Other AI Agents

1. Clone this repository or copy the `skills/feedback/` directory
2. Place it in your agent's skills directory
3. The agent will automatically discover and load the skill

## License

MIT
