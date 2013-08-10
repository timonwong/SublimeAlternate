========================
SublimeAlternate Plugin
========================

Introduction
============
SublimeAlternate is a simple working in progress plugin for Sublime Text 2. It provides simple ways to alternate
files (like swithing .c to .h) by keyboard shortcuts quickly.

Installation
============
With the Package Control plugin
-------------------------------
The easiest way to install SublimeAStyleFormatter is through `Package Control
<http://wbond.net/sublime_packages/package_control>`_.

Once you have Package Control installed, restart Sublime Text 2.

- Bring up the Command Pattle (``Ctrl+Shift+P`` on Windows and Linux. ``Command+Shift+P`` on OS X). 
- Type "Install" and select "Package Control: Install Package".
- Select "SublimeAStyleFormatter" from list.

The advantage of using Package Control is that it will keep SublimeAStyleFormatter up to date.


Manual Install
--------------
**Without Git:**
`Download
<https://github.com/timonwong/SublimeAlternate>`_ 
the latest source code, and extract to the Packages directory.

**With Git:**
Type the following command in your Sublime Text 2 Packages directory::

         git clone git://github.com/timonwong/SublimeAlternate.git

The "Packages" directory is located at:

    :Windows:    ``%APPDATA%\Sublime Text 2\Packages\``
    :Linux:      ``~/.config/sublime-text-2/Packages/``
    :OS X:       ``~/Library/Application Support/Sublime Text 2/Packages/``

Usage
=====

Key Bindings
------------
The default key bindings for this plugin:

   :alt+o:       Alternate file

What's New
==========

v1.1 (3/1/2012)

- Add ability to choose which file to open while multiple matches are found.


License
=======
This plugin is using MIT License.

::

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
