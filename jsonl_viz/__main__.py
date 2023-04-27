import rich
import fire
from threading import Event
from keyboard import KeyboardEvent
import keyboard
from jsonl_viz.jsonl_iterator import JsonlIterator

application_lifetime = Event()

JL_ITERATOR: JsonlIterator


def on_press(e: KeyboardEvent, force=False):
    global JL_ITERATOR

    prev_line = JL_ITERATOR.current_line_idx
    if e.name == "q":
        application_lifetime.set()
        return
    elif e.name == "up":
        JL_ITERATOR.backward()
    elif e.name == "down":
        JL_ITERATOR.forward()

    if prev_line != JL_ITERATOR.current_line_idx or force:
        rich.get_console().clear()
        rich.print(JL_ITERATOR.current_line_idx)
        rich.print_json(JL_ITERATOR.current())


def cli_main(file_path: str):
    global JL_ITERATOR
    JL_ITERATOR = JsonlIterator(file_path)

    # synthetically trigger refresh
    on_press(KeyboardEvent(None, 0), force=True)

    keyboard.on_press(on_press)
    application_lifetime.wait()


def main():
    fire.Fire(cli_main)


if __name__ == "__main__":
    fire.Fire(cli_main)
