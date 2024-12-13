from pathlib import Path
import yaml
import os


def scan_md_files(root_dir):
    for md_file in Path(root_dir).rglob("*.md"):
        try:
            # Get relative path
            rel_path = md_file.relative_to(root_dir)

            # Get file size
            file_size = os.path.getsize(md_file)

            # Read and parse frontmatter
            content = md_file.read_text(encoding='utf-8')
            parts = content.split('---', 2)

            title = "no title"
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1])
                if frontmatter and isinstance(frontmatter, dict):
                    title = frontmatter.get('title', "no title")

            print(f"{rel_path},{title},{file_size}")

        except Exception as e:
            print(f"{rel_path},no title,0")


# Usage
if __name__ == "__main__":
    directory = ""
    scan_md_files(directory)
