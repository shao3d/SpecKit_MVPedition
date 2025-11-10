<div align="center">
    <h1>🌱 Spec Kit</h1>
    <h3><em>Build high-quality software faster.</em></h3>
</div>

<p align="center">
    <strong>A lightweight toolkit for spec-driven development.</strong>
</p>

<p align="center">
    <a href="https://github.com/shao3d/SpecKit_MyEdition/blob/main/LICENSE"><img src="https://img.shields.io/github/license/shao3d/SpecKit_MyEdition" alt="License"/></a>
    <a href="https://github.com/shao3d/SpecKit_MyEdition/stargazers"><img src="https://img.shields.io/github/stars/shao3d/SpecKit_MyEdition?style=social" alt="GitHub stars"/></a>
</p>

---

## 🤔 What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional software development. For decades, code has been king — specifications were just scaffolding we built and discarded once the "real work" of coding began. Spec-Driven Development changes this: **specifications become executable**, directly generating working implementations rather than just guiding them.

## ⚡ Get Started

This guide describes the lightweight, MVP-focused workflow.

### 1. Install the CLI

Install the tool once using `uv`. This will make the `specify` command available system-wide.
```bash
uv tool install specify-cli --from git+https://github.com/shao3d/SpecKit_MyEdition.git
```
To upgrade, run the same command again with `--force`.

### 2. Initialize Your Project

Navigate to your projects directory and run the `init` command. It will create a new folder with all the necessary templates.
```bash
# Go to your development folder
cd ~/Documents/Projects

# Create the project
specify init my-new-project
```

### 3. Start the Manual Workflow

This tool prepares a project for a conversational, manual workflow with an AI assistant like Gemini CLI or Claude.

1.  Navigate into your new project folder:
    ```bash
    cd my-new-project
    ```
2.  Create a brief file (e.g., `brief.md`) describing your project.
3.  Launch your AI assistant (e.g., `gemini`).
4.  Give the assistant its first instruction to start the process:
    ```
    Let's start. Read the instructions from `./templates/commands/specify.md` and my brief from `./brief.md`, then create a draft of spec.md.
    ```
The assistant will then guide you through the three stages: creating the `spec.md`, `plan.md`, and `tasks.md` files.

## 🔧 Specify CLI Reference

The `specify` command-line tool is used to initialize a new MVP project.

### Commands

| Command | Description                                          |
|---------|------------------------------------------------------|
| `init`  | Initialize a new MVP project from the bundled template. |
| `check` | Checks for the installation of `git`.                  |

### `init` Examples

```bash
# Create a new project in a new directory
specify init my-project

# Create a project in the current directory
specify init .

# Create a project without initializing a git repository
specify init my-project --no-git
```

## 🔍 Troubleshooting

### Git Credential Manager on Linux

If you're having issues with Git authentication on Linux, you can install Git Credential Manager:

```bash
#!/usr/bin/env bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```

## 👥 Maintainer

- [shao3d](https://github.com/shao3d)

## 💬 Support

For support, please open a [GitHub issue](https://github.com/shao3d/SpecKit_MyEdition/issues/new). We welcome bug reports, feature requests, and questions about using Spec-Driven Development.

## 📄 License

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](./LICENSE) file for the full terms.