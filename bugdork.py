#!/usr/bin/env python3
"""
BugDork - CMD-Based Google Dork Tool for Bug Hunting

Author: Vishal
GitHub: https://github.com/asur2103/bugdork
"""

import argparse
import os
import webbrowser
from pyfiglet import figlet_format
from termcolor import cprint

def banner() -> None:
    """
    Print the ASCII banner with colors.
    """
    cprint(figlet_format("BugDork", font="slant"), "cyan")
    cprint("Author: Vishal | CMD-Based Google Dork Tool for Bug Hunting\n", "yellow")

def load_dorks(dork_type: str) -> list[str]:
    """
    Load dork queries from corresponding file in dorks/ directory.
    
    Args:
        dork_type (str): The dork category/type
    
    Returns:
        list[str]: List of dork query templates
    """
    filepath = os.path.join("dorks", f"{dork_type}.txt")
    if not os.path.isfile(filepath):
        cprint(f"[!] Dork file not found: {filepath}", "red")
        return []
    with open(filepath, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def list_dork_types() -> None:
    """
    List all available dork types by reading the dorks/ directory.
    """
    dorks_dir = "dorks"
    if not os.path.isdir(dorks_dir):
        cprint(f"[!] Dorks directory not found: {dorks_dir}", "red")
        return

    cprint("[*] Available dork categories:\n", "green")
    for filename in sorted(os.listdir(dorks_dir)):
        if filename.endswith(".txt"):
            cprint(f"  - {filename[:-4]}", "cyan")
    print()
    cprint("Usage example:", "yellow")
    cprint("  python bugdork.py --domain example.com --type login\n", "yellow")

def generate_dorks(domain: str, dork_type: str, open_in_browser: bool = False) -> None:
    """
    Generate Google dork URLs for the given domain and dork type.
    
    Args:
        domain (str): Target domain
        dork_type (str): Dork category/type
        open_in_browser (bool): Whether to open URLs in browser
    """
    dorks = load_dorks(dork_type)
    if not dorks:
        cprint("[!] No dorks loaded. Exiting.", "red")
        return

    cprint(f"[+] Generating Google Dorks for domain: {domain} (Category: {dork_type})\n", "green")
    for query_template in dorks:
        query = query_template.format(domain=domain)
        url = f"https://www.google.com/search?q={query}"
        cprint(f"[DORK] {query}", "white")
        if open_in_browser:
            webbrowser.open(url)

def main() -> None:
    """
    Main entry point of the tool.
    """
    parser = argparse.ArgumentParser(
        description="BugDork - CMD-Based Google Dork Tool for Bug Hunting"
    )
    parser.add_argument(
        "--domain", type=str, help="Target domain (e.g. example.com)"
    )
    parser.add_argument(
        "--type", type=str, help="Dork category (e.g. login, config, directories)"
    )
    parser.add_argument(
        "--open", action="store_true", help="Open dork URLs in the default browser"
    )
    parser.add_argument(
        "--list", action="store_true", help="List all available dork categories"
    )

    args = parser.parse_args()

    banner()

    if args.list:
        list_dork_types()
        return

    if not args.domain or not args.type:
        cprint("[!] Error: --domain and --type are required arguments unless --list is used.\n", "red")
        parser.print_help()
        return

    generate_dorks(args.domain, args.type, args.open)

if __name__ == "__main__":
    main()
