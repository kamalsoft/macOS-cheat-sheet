# Contributing to macOS Mastered

Thank you for considering contributing to **macOS Mastered**! We welcome contributions from everyone, whether it's fixing a typo, adding a new tool, or improving the setup script.

## How to Contribute

### 1. Fork the Repository
Click the "Fork" button at the top right of the repository page to create your own copy of the project.

### 2. Create a Branch
Create a new branch for your changes. Use a descriptive name:
```bash
git checkout -b feature/add-new-tool
# or
git checkout -b fix/typo-in-readme
```

### 3. Make Your Changes
- **Cheat Sheet (`index.md`):** Ensure you follow the existing formatting (emoji usage, headers, and tables).
- **Scripts (`setup.sh`):** Test your scripts locally. Ensure they are idempotent (safe to run multiple times) and include comments.

### 4. Commit and Push
Commit your changes with a clear message:
```bash
git commit -m "Add Raycast to Productivity Apps section"
git push origin feature/add-new-tool
```

### 5. Submit a Pull Request
Go to the original repository and open a Pull Request (PR) from your forked branch. Provide a brief description of what you changed and why.

## Guidelines

- **Accuracy:** Verify that commands and shortcuts work on the latest macOS versions (Sonoma/Ventura).
- **Safety:** Do not submit scripts that download unverified binaries or disable critical security features (like SIP) without heavy warnings.
- **Style:** Keep the tone professional yet accessible.

Thank you for helping us master macOS! 🚀