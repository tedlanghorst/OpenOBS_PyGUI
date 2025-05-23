from abc import ABC, abstractmethod


class BaseSensor(ABC):
    def __init__(self, name: str, parent_frame):
        self.name = name
        self.configure_gui(parent_frame)

    @abstractmethod
    def configure_gui(self, parent_frame):
        """Configure the GUI elements specific to this sensor."""
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def get_settings_words(self):
        """Build the settings string to send to the device."""
        raise NotImplementedError("Subclasses must implement this method.")
