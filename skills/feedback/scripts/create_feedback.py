#!/usr/bin/env python3
"""
Feedback creation script
Helps create structured feedback files
"""

import sys
import os
from datetime import datetime

FEEDBACK_TYPES = {
    '1': 'Bug Report',
    '2': 'Feature Request',
    '3': 'Improvement',
    '4': 'General Feedback'
}

def create_feedback_file(feedback_type, title, content, output_dir='feedback'):
    """Create a structured feedback file"""

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate filename
    date_str = datetime.now().strftime('%Y-%m-%d')
    safe_title = title.lower().replace(' ', '-')[:50]
    filename = f"feedback-{date_str}-{safe_title}.md"
    filepath = os.path.join(output_dir, filename)

    # Create the file content
    file_content = f"""# Feedback: {title}

**Type**: {feedback_type}
**Date**: {date_str}

## Description
{content}

## Status
- [x] Submitted
- [ ] Under Review
- [ ] In Progress
- [ ] Completed
"""

    # Write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(file_content)

    return filepath

def main():
    print("=== Feedback Creation Tool ===\n")

    # Get feedback type
    print("Select feedback type:")
    for key, value in FEEDBACK_TYPES.items():
        print(f"  {key}. {value}")

    type_choice = input("\nEnter choice (1-4): ").strip()
    feedback_type = FEEDBACK_TYPES.get(type_choice, 'General Feedback')

    # Get title
    title = input("\nEnter feedback title: ").strip()
    if not title:
        print("Error: Title is required")
        sys.exit(1)

    # Get content
    print("\nEnter feedback description (press Ctrl+D or Ctrl+Z when done):")
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    content = '\n'.join(lines)

    if not content.strip():
        print("Error: Description is required")
        sys.exit(1)

    # Get output directory
    output_dir = input("\nEnter output directory (default: 'feedback'): ").strip()
    if not output_dir:
        output_dir = 'feedback'

    # Create the file
    filepath = create_feedback_file(feedback_type, title, content, output_dir)

    print(f"\n✓ Feedback file created: {filepath}")

if __name__ == '__main__':
    main()
