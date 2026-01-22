"""Shader management for ghostty configuration."""
from .utils import load_json, read_config, write_config, SHADERS_JSON

class ShaderManager:
    def __init__(self):
        self.reload()
    
    def reload(self):
        """Reload shaders from JSON file."""
        data = load_json(SHADERS_JSON)
        self.shaders = data.get("shaders", {})
    
    def get_active(self):
        """Get list of active shader paths from config."""
        lines = read_config()
        active = []
        
        for line in lines:
            line = line.strip()
            if line.startswith("custom-shader = ") and not line.startswith("#"):
                path = line.split("=", 1)[1].strip()
                active.append(path)
        
        return active
    
    def get_all(self):
        """Get all available shaders."""
        return self.shaders
    
    def find_shader_by_path(self, path):
        """Find shader ID by its path."""
        for shader_id, info in self.shaders.items():
            if info["path"] == path:
                return shader_id
        return None
    
    def list_with_status(self):
        """List all shaders with their ON/OFF status."""
        active_paths = self.get_active()
        results = []
        
        # Find max lengths for formatting
        max_id_len = max(len(sid) for sid in self.shaders.keys())
        
        for shader_id, info in self.shaders.items():
            is_active = info["path"] in active_paths
            status = "ON " if is_active else "OFF"
            results.append({
                "id": shader_id,
                "name": info["name"],
                "status": status,
                "description": info["description"],
                "active": is_active
            })
        
        # Sort by category then name
        results.sort(key=lambda x: (not x["active"], x["id"]))
        
        return results, max_id_len
    
    def toggle(self, shader_id):
        """Toggle a shader on/off in the config."""
        if shader_id not in self.shaders:
            # Try partial match
            matches = [sid for sid in self.shaders if shader_id.lower() in sid.lower()]
            if len(matches) == 1:
                shader_id = matches[0]
            elif len(matches) > 1:
                raise ValueError(f"Multiple matches for '{shader_id}': {', '.join(matches)}")
            else:
                raise ValueError(f"Shader '{shader_id}' not found")
        
        shader_info = self.shaders[shader_id]
        shader_path = shader_info["path"]
        active_paths = self.get_active()
        
        if shader_path in active_paths:
            # Turn OFF - comment out the line
            self._remove_from_config(shader_path)
            return shader_info["name"], False
        else:
            # Turn ON - add or uncomment the line
            self._add_to_config(shader_path)
            return shader_info["name"], True
    
    def _add_to_config(self, shader_path):
        """Add shader line to end of config."""
        lines = read_config()
        shader_line = f"custom-shader = {shader_path}\n"
        
        # Check if shader already exists
        for line in lines:
            if line.strip() == f"custom-shader = {shader_path}":
                return  # Already active, nothing to do
        
        # Add blank line before shader if last line isn't empty
        if lines and lines[-1].strip():
            lines.append("\n")
        
        lines.append(shader_line)
        write_config(lines)
    
    def _remove_from_config(self, shader_path):
        """Remove shader line from config."""
        lines = read_config()
        shader_line = f"custom-shader = {shader_path}"
        
        # Filter out the shader line
        new_lines = []
        shader_found = False
        skip_next_blank = False
        
        for i, line in enumerate(lines):
            if line.strip() == shader_line:
                shader_found = True
                # Check if next line is blank, if so skip it too
                if i + 1 < len(lines) and not lines[i + 1].strip():
                    skip_next_blank = True
                continue
            
            if skip_next_blank and not line.strip():
                skip_next_blank = False
                continue
                
            new_lines.append(line)
        
        if not shader_found:
            raise ValueError(f"Shader not found in config: {shader_path}")
        
        write_config(new_lines)
    
    def remove_all(self):
        """Remove all active shaders from config."""
        lines = read_config()
        new_lines = []
        
        for line in lines:
            if line.strip().startswith("custom-shader = "):
                continue
            new_lines.append(line)
        
        write_config(new_lines)
    
    def show_info(self):
        """Return formatted info about shaders."""
        active = self.get_active()
        shader_list, max_id_len = self.list_with_status()
        
        info = ["Shaders:"]
        
        for shader in shader_list:
            line = f"{shader['id']:<{max_id_len}}  {shader['status']}  {shader['description']}"
            info.append(line)
        
        info.append(f"\nActive: {len(active)} shaders")
        
        return "\n".join(info)