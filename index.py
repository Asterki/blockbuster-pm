from models.inventory import InventoryModel


class App:
    def __init__(self):
        self.inventory = InventoryModel()

        self.inventory.export_to_excel('users')


if __name__ == "__main__":
    App()
