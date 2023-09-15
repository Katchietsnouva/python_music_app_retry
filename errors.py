PS C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry> python app.py
pygame 2.5.1 (SDL 2.28.2, Python 3.11.5)
Hello from the pygame community. https://www.pygame.org/contribute.html
PLAY
PLAY
Traceback (most recent call last):
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\app.py", line 125, in <module>
    root.mainloop()
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\venv\Lib\site-packages\customtkinter\windows\ctk_tk.py", line 163, in mainloop
    super().mainloop(*args, **kwargs)
  File "C:\Python311\Lib\tkinter\__init__.py", line 1485, in mainloop
    self.tk.mainloop(n)
KeyboardInterrupt
Exception in thread Thread-2 (progress):
Exception in thread Thread-1 (progress):
Traceback (most recent call last):
  File "C:\Python311\Lib\threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "C:\Python311\Lib\threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\app.py", line 63, in progress
    progressbar.set(pygame.mixer.music.get_pos()/1000000)
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\venv\Lib\site-packages\customtkinter\windows\widgets\ctk_progressbar.py", line 245, in set  
    self._draw(no_color_updates=True)
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\venv\Lib\site-packages\customtkinter\windows\widgets\ctk_progressbar.py", line 128, in _draw
    requires_recoloring = self._draw_engine.draw_rounded_progress_bar_with_border(self._apply_widget_scaling(self._current_width),
Traceback (most recent call last):
  File "C:\Python311\Lib\threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "C:\Python311\Lib\threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\app.py", line 63, in progress
    progressbar.set(pygame.mixer.music.get_pos()/1000000)
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\venv\Lib\site-packages\customtkinter\windows\widgets\ctk_progressbar.py", line 245, in set
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\venv\Lib\site-packages\customtkinter\windows\widgets\core_rendering\draw_engine.py", line 721, in draw_rounded_progress_bar_with_border
    self._draw(no_color_updates=True)
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\venv\Lib\site-packages\customtkinter\windows\widgets\ctk_progressbar.py", line 128, in _draw
    requires_recoloring = self._draw_engine.draw_rounded_progress_bar_with_border(self._apply_widget_scaling(self._current_width),
    return self.__draw_rounded_progress_bar_with_border_font_shapes(width, height, corner_radius, border_width, inner_corner_radius,
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\venv\Lib\site-packages\customtkinter\windows\widgets\core_rendering\draw_engine.py", line 721, in draw_rounded_progress_bar_with_border
    return self.__draw_rounded_progress_bar_with_border_font_shapes(width, height, corner_radius, border_width, inner_corner_radius,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\venv\Lib\site-packages\customtkinter\windows\widgets\core_rendering\draw_engine.py", line 773, in __draw_rounded_progress_bar_with_border_font_shapes
    if not self._canvas.find_withtag("progress_oval_1_a"):
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry\venv\Lib\site-packages\customtkinter\windows\widgets\core_rendering\draw_engine.py", line 773, in __draw_rounded_progress_bar_with_border_font_shapes
  File "C:\Python311\Lib\tkinter\__init__.py", line 2922, in find_withtag
    if not self._canvas.find_withtag("progress_oval_1_a"):
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python311\Lib\tkinter\__init__.py", line 2922, in find_withtag
    return self.find('withtag', tagOrId)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    return self.find('withtag', tagOrId)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python311\Lib\tkinter\__init__.py", line 2889, in find
  File "C:\Python311\Lib\tkinter\__init__.py", line 2889, in find
    self.tk.call((self._w, 'find') + args)) or ()
    self.tk.call((self._w, 'find') + args)) or ()
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: main thread is not in main loop
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: main thread is not in main loop
PS C:\Users\katchietsnouvaniccur\Documents\Python_Projects\python_music_app_retry>


