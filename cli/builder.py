import colorama
from colorama import Fore, Style
import click
import os
import shutil
import subprocess

colorama.init(autoreset=True)

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")

def success(msg):
    click.echo(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")

def fail(msg):
    click.echo(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")

def info(msg):
    click.echo(f"{Fore.YELLOW}➡️ {msg}{Style.RESET_ALL}")

def create_project_logic(template, name, path, git):
    template_path = os.path.join(TEMPLATE_DIR, template)

    if not os.path.exists(template_path):
        fail(f"template: {template} wasn't found!")
        return False

    project_path = os.path.join(path, name)
    if os.path.exists(project_path):
        fail(f"project folder: {project_path} already exists!")
        return False

    try:
        info(f"copying {template} template to {project_path}...")
        shutil.copytree(template_path, project_path)
        success(f"project {name} is created successfully!")

        if git:
            info("running git init...")
            try:
                subprocess.run(["git", "init"], cwd=project_path, check=True)
                success("Git repo made successfully!")
            except subprocess.CalledProcessError:
                fail("something went wrong on running git init")
                return False
            except FileNotFoundError:
                fail("Git is not found!")
                return False

        return True

    except Exception as e:
        fail(f"Error in process: {e}")
        if os.path.exists(project_path):
            shutil.rmtree(project_path)
        return False

@click.group()
def builder():
    """A template file manager with PY"""
    pass

@click.command("new")
@click.option('--template', '-t', required=True, help="the chosen template, like pure-python.")
@click.option('--name', '-n', required=True, help="the project name.")
@click.option('--path', '-p', default=".", help="the project path. default is '.'.")
@click.option('--git', '-g', is_flag=True, help="using git init.")
def create_project_command(template, name, path, git):
    success = create_project_logic(template, name, path, git)
    if not success:
        exit(1)

builder.add_command(create_project_command)

def main():
    builder()

if __name__ == "__main__":
    main()
