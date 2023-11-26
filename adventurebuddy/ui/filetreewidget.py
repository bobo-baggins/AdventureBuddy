import pathlib

from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget


class FileTreeWidget(QTreeWidget):
    def __init__(self, path: pathlib.Path | str, parent: QWidget = None):
        """A widget which holds entries from the filesystem as a tree.

        Parameters
        ----------
        path : pathlib.Path | str
            Path to search for filesystem objects
        parent : QWidget
            The parent of this widget
        """
        super().__init__(parent)
        self.root = pathlib.Path(path)
        self.refresh()

    def refresh(self):
        """Clear out the FileTreeWidget, and repopulate it with objects from the filesystem."""
        self.clear()
        self.addTopLevelItems(self.items_from_path(self.root))

    def items_from_path(self, path: pathlib.Path) -> list[QTreeWidgetItem]:
        """Generate a list of item widgets for each filesystem object from the given path.

        The result is sorted, with directories coming before files.

        Parameters
        ----------
        path : pathlib.Path
            Path to recurse through for filesystem objects

        Returns
        -------
        list[QTreeWidgetItem]
            List of widgets to populate the file tree
        """
        files = []
        directories = []
        for item in path.iterdir():
            entry = QTreeWidgetItem(None, [str(item.relative_to(self.root))])
            if item.is_file():
                files.append(entry)
            elif item.is_dir():
                entry.addChildren(self.items_from_path(item))
                directories.append(entry)
            else:
                raise ValueError("Unknown file type encountered")

        return sorted(directories) + sorted(files)
