#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "typer",
#     "rich",
#     "platformdirs",
#     "readchar",
# ]
# ///
"""
Specify CLI - MVP Edition

Usage:
    specify init <project-name>
    specify init .
    specify init --here
"""

import os
import subprocess
import sys
import shutil
from pathlib import Path
from typing import Optional, Tuple

import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from typer.core import TyperGroup

# --- Helper Functions & Classes ---

console = Console()

BANNER = """
███████╗██████╗ ███████╗ ██████╗██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██║██╔════╝╚██╗ ██╔╝
███████╗██████╔╝█████╗  ██║     ██║█████╗   ╚████╔╝ 
╚════██║██╔═══╝ ██╔══╝  ██║     ██║██╔══╝    ╚██╔╝  
███████║██║     ███████╗╚██████╗██║██║        ██║   
╚══════╝╚═╝     ╚══════╝ ╚═════╝╚═╝╚═╝        ╚═╝   
"""

TAGLINE = "GitHub Spec Kit - MVP Development Toolkit"

class BannerGroup(TyperGroup):
    """Custom group that shows banner before help."""
    def format_help(self, ctx, formatter):
        show_banner()
        super().format_help(ctx, formatter)

app = typer.Typer(
    name="specify",
    help="Setup tool for Specify MVP development projects",
    add_completion=False,
    invoke_without_command=True,
    cls=BannerGroup,
)

def show_banner():
    """Display the ASCII art banner."""
    banner_lines = BANNER.strip().split('\n')
    colors = ["bright_blue", "blue", "cyan", "bright_cyan", "white", "bright_white"]
    styled_banner = Text()
    for i, line in enumerate(banner_lines):
        color = colors[i % len(colors)]
        styled_banner.append(line + "\n", style=color)
    console.print(Align.center(styled_banner))
    console.print(Align.center(Text(TAGLINE, style="italic bright_yellow")))
    console.print()

def check_tool(tool: str) -> bool:
    """Check if a tool is installed."""
    return shutil.which(tool) is not None

def is_git_repo(path: Path = None) -> bool:
    """Check if the specified path is inside a git repository."""
    if path is None:
        path = Path.cwd()
    if not path.is_dir():
        return False
    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            capture_output=True,
            cwd=path,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def init_git_repo(project_path: Path) -> Tuple[bool, Optional[str]]:
    """Initialize a git repository in the specified path."""
    try:
        original_cwd = Path.cwd()
        os.chdir(project_path)
        console.print("[cyan]Initializing git repository...[/cyan]")
        subprocess.run(["git", "init"], check=True, capture_output=True, text=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True, text=True)
        subprocess.run(["git", "commit", "-m", "Initial commit from Specify MVP template"], check=True, capture_output=True, text=True)
        console.print("[green]✓[/green] Git repository initialized")
        return True, None
    except subprocess.CalledProcessError as e:
        error_msg = f"Command: {' '.join(e.cmd)}\nExit code: {e.returncode}\nError: {e.stderr.strip()}"
        console.print(f"[red]Error initializing git repository:[/red] {e}")
        return False, error_msg
    finally:
        os.chdir(original_cwd)

def generate_constitution(project_path: Path):
    """Generates Constitution.md from template in the project root."""
    try:
        template_path = Path(__file__).parent / "templates" / "constitution-template.md"
        constitution_path = project_path / "Constitution.md"

        if template_path.exists():
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()

            with open(constitution_path, 'w', encoding='utf-8') as f:
                f.write(content)

            console.print(f"[green]✓[/green] Constitution.md created at {constitution_path}")
        else:
            console.print(f"[yellow]Warning: Constitution template not found at {template_path}[/yellow]")
    except Exception as e:
        console.print(f"[red]Error generating Constitution.md: {e}[/red]")

def copy_local_template(project_path: Path, is_current_dir: bool):
    """Copies the local template directory to the new project."""
    try:
        source_path = Path(__file__).parent / "templates"
        if not source_path.is_dir():
            raise FileNotFoundError(f"Templates directory not found at {source_path}")

        dest_specify_path = project_path / ".specify"
        dest_templates_path = dest_specify_path / "templates"

        if not is_current_dir:
            project_path.mkdir(parents=True, exist_ok=True)

        dest_specify_path.mkdir(exist_ok=True)
        
        if dest_templates_path.exists():
            shutil.rmtree(dest_templates_path)
            
        shutil.copytree(source_path, dest_templates_path)
        console.print(f"[green]✓[/green] Templates copied to {dest_templates_path}")

        # Generate Constitution.md from template
        generate_constitution(project_path)

        return project_path
    except Exception as e:
        console.print(f"[red]Error copying local template: {e}[/red]")
        if not is_current_dir and project_path.exists():
            shutil.rmtree(project_path)
        raise typer.Exit(1)

# --- Typer App & Commands ---

@app.callback()
def callback(ctx: typer.Context):
    """Show banner when no subcommand is provided."""
    if ctx.invoked_subcommand is None and "--help" not in sys.argv and "-h" not in sys.argv:
        show_banner()
        console.print(Align.center("[dim]Run 'specify --help' for usage information[/dim]"))
        console.print()

@app.command()
def init(
    project_name: str = typer.Argument(None, help="Name for your new project directory (optional if using --here, or use '.' for current directory)"),
    no_git: bool = typer.Option(False, "--no-git", help="Skip git repository initialization"),
    here: bool = typer.Option(False, "--here", help="Initialize project in the current directory instead of creating a new one"),
    force: bool = typer.Option(False, "--force", help="Force merge/overwrite when using --here (skip confirmation)"),
):
    """
    Initialize a new Specify MVP project from the bundled template.
    
    This command will:
    1. Create a new project directory (or use the current one).
    2. Copy the bundled MVP templates into the project's '.specify' directory.
    3. Initialize a git repository (unless --no-git is used).
    
    Examples:
        specify init my-project
        specify init my-project --no-git
        specify init .                     # Initialize in current directory
        specify init --here                # Alternative syntax for current directory
        specify init --here --force        # Skip confirmation when current directory not empty
    """
    show_banner()

    if project_name == ".":
        here = True
        project_name = None

    if here and project_name:
        console.print("[red]Error:[/red] Cannot specify both project name and --here flag")
        raise typer.Exit(1)

    if not here and not project_name:
        console.print("[red]Error:[/red] Must specify a project name, use '.' for current directory, or use --here flag")
        raise typer.Exit(1)

    if here:
        project_name = Path.cwd().name
        project_path = Path.cwd()
        if any(project_path.iterdir()):
            console.print(f"[yellow]Warning:[/yellow] Current directory is not empty.")
            console.print("[yellow]Template files will be merged, potentially overwriting existing files.[/yellow]")
            if not force and not typer.confirm("Do you want to continue?"):
                console.print("[yellow]Operation cancelled[/yellow]")
                raise typer.Exit(0)
    else:
        project_path = Path(project_name).resolve()
        if project_path.exists():
            console.print(Panel(f"Directory '[cyan]{project_name}[/cyan]' already exists.", title="[red]Directory Conflict[/red]"))
            raise typer.Exit(1)

    # --- Main Execution ---
    console.print(Panel(f"Project: [green]{project_name}[/green]\nTarget Path: [dim]{project_path}[/dim]", title="Specify MVP Project Setup", border_style="cyan"))
    console.print("[cyan]Creating project from local MVP template...[/cyan]")

    try:
        copy_local_template(project_path, here)

        git_error_message = None
        if not no_git:
            should_init_git = check_tool("git")
            if not should_init_git:
                console.print("[yellow]Git not found - will skip repository initialization.[/yellow]")
            elif is_git_repo(project_path):
                console.print("[green]✓[/green] Git repository already exists.")
            else:
                success, error_msg = init_git_repo(project_path)
                if not success:
                    git_error_message = error_msg
        else:
            console.print("[yellow]Skipping git initialization due to --no-git flag.[/yellow]")

    except Exception as e:
        console.print(Panel(f"Initialization failed: {e}", title="Failure", border_style="red"))
        if not here and project_path.exists():
            shutil.rmtree(project_path)
        raise typer.Exit(1)

    console.print("\n[bold green]Project ready.[/bold green]")
    
    if git_error_message:
        console.print(Panel(f"[yellow]Warning:[/yellow] Git repository initialization failed\n\n{git_error_message}", title="[red]Git Initialization Failed[/red]"))

    steps_lines = [
        "1. Go to the project folder: " + (f"[cyan]cd {project_name}[/cyan]" if not here else "[cyan]You're already there![/cyan]"),
        "2. Put the [cyan]brief.md[/cyan] file of your new project in the project folder",
        "3. Launch your AI agent (e.g., Claude Code, Codex, Gemini CLI, etc)",
        "4. Start the process with a prompt like:",
        "   [dim]\"Let's start. Read the instructions from specify.md and my brief.md and we'll together interactivly create a draft of spec.md.\"[/dim]"
    ]
    console.print(Panel("\n".join(steps_lines), title="Next Steps", border_style="cyan", padding=(1,2)))

@app.command()
def check():
    """Check that required tools are installed."""
    show_banner()
    console.print("[bold]Checking for installed tools...[/bold]\n")
    
    git_ok = check_tool("git")
    
    if git_ok:
        console.print("[green]✓[/green] Git is installed.")
    else:
        console.print("[yellow]✗[/yellow] Git is not installed. (Recommended for version control)")

    console.print("\n[bold green]Specify CLI is ready to use![/bold green]")

def main():
    app()

if __name__ == "__main__":
    main()
