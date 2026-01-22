"""Neovim synchronization for terminal theme changes."""
import os
import glob
import subprocess
from typing import List
from pathlib import Path

try:
    from pynvim import attach
    PYNVIM_AVAILABLE = True
except ImportError:
    PYNVIM_AVAILABLE = False


class NeovimSync:
    """Handles synchronization of colorscheme with running Neovim instances."""
    
    @staticmethod
    def find_nvim_sockets() -> List[str]:
        """Find all Neovim socket files."""
        if not PYNVIM_AVAILABLE:
            return []
            
        sockets = []
        
        # Check /tmp directory for nvim sockets
        try:
            for item in os.listdir('/tmp'):
                if item.startswith('nvim'):
                    socket_path = os.path.join('/tmp', item, '0')
                    if os.path.exists(socket_path):
                        sockets.append(socket_path)
        except (PermissionError, OSError):
            pass
        
        # Check common socket locations
        socket_paths = [
            # User's runtime directory
            Path.home() / '.local' / 'share' / 'nvim' / 'nvim*.sock',
            # XDG runtime directory
            Path(os.environ.get('XDG_RUNTIME_DIR', '/tmp')) / 'nvim*',
            # Direct /tmp patterns
            Path('/tmp') / 'nvim-*.sock',
            Path('/tmp') / 'nvimsocket',
        ]
        
        for pattern in socket_paths:
            try:
                for socket in glob.glob(str(pattern)):
                    if os.path.exists(socket):
                        sockets.append(socket)
            except (PermissionError, OSError):
                pass
        
        # Try to find sockets using lsof
        try:
            result = subprocess.run(
                ['lsof', '-c', 'nvim', '-a', '-U'],
                capture_output=True,
                text=True
            )
            for line in result.stdout.splitlines():
                parts = line.split()
                for part in parts:
                    if '/nvim' in part and (part.endswith('.sock') or '/nvim.' in part):
                        if os.path.exists(part):
                            sockets.append(part)
        except:
            pass
        
        return list(set(sockets))  # Remove duplicates
    
    @staticmethod
    def sync_colorscheme():
        """Send :SyncColorscheme to all running Neovim instances."""
        if not PYNVIM_AVAILABLE:
            return
            
        sockets = NeovimSync.find_nvim_sockets()
        
        for socket_path in sockets:
            try:
                # Connect to Neovim instance
                nvim = attach('socket', path=socket_path)
                
                # Execute the command
                nvim.command('SyncColorscheme')
                
            except Exception:
                # Silently ignore errors (socket might be stale, etc.)
                pass