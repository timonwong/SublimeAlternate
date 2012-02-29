"""
Copyright (c) 2012 Timon Wong

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sublime
import sublime_plugin
import os.path

g_alternate_mapping = {}


def add_alternate_mapping(extension, alternates):
    global g_alternate_mapping
    g_alternate_mapping[extension] = alternates


def load_settings():
    settings = sublime.load_settings("SublimeAlternate.sublime-settings")
    mappings = settings.get("sublime_alternate_extension_mappings", [])
    global g_alternate_mapping
    for mapping in mappings:
        if "ext" not in mapping:
            continue
        if "alts" not in mapping:
            continue
        ext = mapping["ext"]
        alts = mapping["alts"]
        g_alternate_mapping[ext] = alts

load_settings()


def get_alternate_file_list(fullpath):
    filename = os.path.basename(fullpath)
    alt_file_list = []

    for ext, alt_exts in g_alternate_mapping.items():
        ext_len = len(ext)
        if ext_len > len(filename):
            continue
        # Check whether "basename[.ext]" acutal matches
        # Since there are some extensions contains more than one dots (".aspx.cs"),
        #   so we cannot just use splitext here
        if filename[-ext_len:] != ext or filename[-ext_len - 1] != '.':
            continue
        # Get basename
        # '1' taks a 'dot'
        basename_len = len(filename) - ext_len - 1
        basename = filename[:basename_len]
        for alt_ext in alt_exts:
            alt_filename = "%s.%s" % (basename, alt_ext)
            alt_file_list.append(alt_filename)
    return alt_file_list


class AlternateFileCommand(sublime_plugin.WindowCommand):
    def resolve_alt_file_list(self, alt_file_list):
        window = self.window
        view = window.active_view()
        self.instance_file_list = []

        # Same folder first
        for alt_file in alt_file_list:
            # Same folder as view
            folder = os.path.dirname(view.file_name())
            path = os.path.join(folder, alt_file)
            if os.path.isfile(path):
                self.instance_file_list.append(path)

        if len(self.instance_file_list) == 1:
            path = self.instance_file_list[0]
            window.open_file(path)
            self.instance_file_list = []
            return

        # Search deeper
        for alt_file in alt_file_list:
            for folder in window.folders():
                path = os.path.join(folder, alt_file)
                if os.path.isfile(path):
                    self.instance_file_list.append(path)

        # Show alternates, let user choose
        window.show_quick_panel(self.instance_file_list, self._quick_panel_on_done)

    def _quick_panel_on_done(self, picked):
        if picked == -1:
            return
        filepath = self.instance_file_list[picked]
        self.window.open_file(filepath)

    def run(self):
        view = self.window.active_view()
        fullpath = view.file_name()
        alt_file_list = get_alternate_file_list(fullpath)
        self.resolve_alt_file_list(alt_file_list)
