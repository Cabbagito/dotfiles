"""Synchronization utilities for config changes."""
from .ghostty_reload import GhosttyReload
from .neovim_sync import NeovimSync


def sync_all():
    """Sync configuration changes to Ghostty and Neovim."""
    # First reload Ghostty configuration
    GhosttyReload.reload_config()
    
    # Then sync colorscheme with Neovim instances
    NeovimSync.sync_colorscheme()