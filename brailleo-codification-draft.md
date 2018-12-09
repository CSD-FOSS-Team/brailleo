# code implementation draft


### Features
- "Easy Mode": toggle option that prints Greek (for now) characters,
  corresponding to the analogous keypresses recieved as input from the user.
  (Instead of printing out the Braille ones)

  1)

- Option to zoom according to one's preference and add script to automatically
  zoom some amount on startup

  - Play around with colored text as well

- Work on a minimal GUI that's cross-platform (mandatory) and feautures a
  textbox which provides:

  1) copy/paste buffer
  2) copy/paste to clipboard buffer

- Make locale-specific dictionaries (?) importable so as to ensure portability
  and customizability

- Ascertain that extended Unicode (about U+2000..) is compatible with user's
  font (not a problem if a GUI is implemented)

  - If not, add compatible fonts in requirements and in Pipfile and include
    them in setup.py

- Find out which text editors/browsers support braille unicode and make a list

   - Maybe have a prompt for the popular ones(?)

- add caps lock
