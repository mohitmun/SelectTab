import sublime, sublime_plugin

class SelectTabCommand(sublime_plugin.WindowCommand):
  def run(self, tab, *args):
    current_window = self.window
    target_view_index = int(tab) - 1
    current_views = current_window.views()
    if target_view_index == 8:
      current_window.focus_view(current_views[len(current_views) - 1])
    else:
      if target_view_index < len(current_views):
        current_window.focus_view(current_views[target_view_index])