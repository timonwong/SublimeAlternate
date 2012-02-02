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

import sublime, sublime_plugin
import os.path

g_alternate_mapping = {}

def add_alternate_mapping(extension, alternates):
    global g_alternate_mapping
    g_alternate_mapping[extension] = alternates

def load_settings():
    settings = sublime.load_settings("Alternate.sublime-settings")
    mappings = settings.get("alternate_extension_mappings", [])
    for mapping in mappings:
        if not mapping.has_key("ext"):
            continue
        if not mapping.has_key("alts"):
            continue
        ext  = mapping["ext"]
        alts = mapping["alts"]
        add_alternate_mapping(ext, alts)

load_settings()

def get_alternate_file_list(fullpath):
    dir = os.path.dirname(fullpath)
    filename = os.path.basename(fullpath)
    alt_file_list = []

    for ext, alt_exts in g_alternate_mapping.items():
        ext_len = len(ext)
        if ext_len > len(filename): 
            continue
        # Check whether "basename[.ext]" acutal matches
        # Since there are some extensions contains more dots (".aspx.cs"), 
        #   so we cannot just use splitext here
        if filename[-ext_len:] != ext or filename[-ext_len - 1] != '.': 
            continue
        # Get basename
        basename_len = len(filename) - ext_len - 1 # '1' taks a 'dot'
        basename = filename[:basename_len]
        for alt_ext in alt_exts:
            alt_filename = "%s.%s" % (basename, alt_ext)
            alt_fullpath = os.path.join(dir, alt_filename)
            alt_file_list.append(alt_fullpath)
    return alt_file_list

def get_available_file_list(alt_file_list):
    avail_file_list = []
    for alt_file in alt_file_list:
        if os.path.exists(alt_file):
            avail_file_list.append(alt_file)
    return avail_file_list

# Open the first matches file only
def open_one_available_file(avail_file_list, window, views):
    if len(avail_file_list) == 0:
        return False
    filename = avail_file_list[0]
    # Check if the file is already open but inactived.
    for view in views:
        if view.file_name() == filename:
            # Switch to view
            window.focus_view(view)
            return
    # Open file
    window.open_file(filename)

class AlternateFileCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        fullpath = view.file_name()
        alt_file_list = get_alternate_file_list(fullpath)
        avail_file_list = get_available_file_list(alt_file_list)
        open_one_available_file(avail_file_list, self.window, self.window.views())
