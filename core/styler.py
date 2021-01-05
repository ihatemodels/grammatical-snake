from rich.console import Console
from rich.box import ASCII2
from rich.panel import Panel
from rich.text import Text

console = Console(color_system="auto")


class Styler:

    padding = (1, 5)

    def print(self, text: Text):

        panel = Panel.fit(
            text, border_style="bold #00ccff", padding=self.padding,
            box=ASCII2, width=90, safe_box=True,
        )

        console.print(panel)

