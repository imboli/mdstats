import yaml
from pathlib import Path


def scan_md_frontmatter_yaml(root_dir):
    results = []

    for md_file in Path(root_dir).rglob("*.md"):
        try:
            content = md_file.read_text(encoding='utf-8')
            # Split on first and second '---'
            parts = content.split('---', 2)
            if len(parts) >= 3:
                # Parse the frontmatter as YAML
                frontmatter = yaml.safe_load(parts[1])
                title = frontmatter.get('title')
                results.append((md_file, title))

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return results


if __name__ == "__main__":
    directory = ""
    files_with_titles = scan_md_frontmatter_yaml(directory)

    for file_path, title in files_with_titles:
        if title:
            print(f"{file_path}: {title}")
        else:
            print(f"{file_path}: No title found")