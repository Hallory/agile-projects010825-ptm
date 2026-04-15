import os
import re
whitelist = {'.csv', '.doc', '.pdf', '.xlsx'}

def check_extension(file, whitelist=whitelist) -> bool:
    if file is None:
        return False
    
    if isinstance(file, str):
        name = file
    else:
        if hasattr(file, 'name'):
            name = file.name
            if not name:
                return False
        else:
            return False
        
    name = os.path.basename(name)
    ext = os.path.splitext(name)[1].lower()
    return ext in whitelist


def check_file_size(file, max_mb=2) -> bool:
    if file is None:
        return False
    if isinstance(file, str):
        try:
            file_size = os.path.getsize(file)
        except FileNotFoundError:
            return False
    elif hasattr(file, 'size'):
        file_size = file.size
        if not isinstance(file_size, (int, float)):
            return False
    else:
        return False

    return file_size <= max_mb * 1024 * 1024


def create_file_path(project_name: str, file_name: str) -> str:
    project_name = re.sub(r'[^a-zA-Z0-9_-]+', '_', project_name)
    project_name = re.sub(r'_+', '_', project_name).strip('_')
    
    clean_name = os.path.basename(file_name)
    
    return os.path.join('documents', project_name, clean_name)
    
    
def save_file(file_path: str, file_content) -> str:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        if hasattr(file_content, "chunks"):
            for chunk in file_content.chunks():
                f.write(chunk)

        elif hasattr(file_content, "read"):
            f.write(file_content.read())

        else:
            f.write(file_content)
            
    return file_path