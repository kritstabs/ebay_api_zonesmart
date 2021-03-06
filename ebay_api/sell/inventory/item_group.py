from .base import InventoryAPI
from .offer import OfferAPI


class InventoryItemGroupAPI(InventoryAPI):
    resource = "inventory_item_group"


class CreateOrReplaceInventoryItemGroup(InventoryItemGroupAPI):
    """
    Docs:
    https://developer.ebay.com/api-docs/sell/inventory/resources/inventory_item_group/methods/createOrReplaceInventoryItemGroup
    """  # noqa

    method_type = "PUT"
    required_path_params = ["inventoryItemGroupKey"]

    def get_success_message(self):
        return (
            f"Группа товаров успешно создана "
            f"(inventoryItemGroupKey: {self.path_params['inventoryItemGroupKey']})"
        )

    def get_error_message(self):
        return (
            f"Не удалось создать группу товаров "
            f"(inventoryItemGroupKey: {self.path_params['inventoryItemGroupKey']})"
        )


class UpdateInventoryItemGroup(CreateOrReplaceInventoryItemGroup):
    """
    Docs:
    https://developer.ebay.com/api-docs/sell/inventory/resources/inventory_item_group/methods/createOrReplaceInventoryItemGroup
    """  # noqa

    def get_success_message(self):
        return (
            f"Группа товаров успешно обновлена "
            f"(inventoryItemGroupKey: {self.path_params['inventoryItemGroupKey']})"
        )

    def get_error_message(self):
        return (
            f"Не удалось обновить группу товаров "
            f"(inventoryItemGroupKey: {self.path_params['inventoryItemGroupKey']})"
        )


class DeleteInventoryItemGroup(InventoryItemGroupAPI):
    """
    Docs:
    https://developer.ebay.com/api-docs/sell/inventory/resources/inventory_item_group/methods/deleteInventoryItemGroup
    """

    method_type = "DELETE"
    required_path_params = ["inventoryItemGroupKey"]

    def get_success_message(self):
        return (
            f"Группа товаров успешно удалена "
            f"(inventoryItemGroupKey: {self.path_params['inventoryItemGroupKey']})"
        )

    def get_error_message(self):
        return (
            f"Не удалось удалить группу товаров "
            f"(inventoryItemGroupKey: {self.path_params['inventoryItemGroupKey']})"
        )


class GetInventoryItemGroup(InventoryItemGroupAPI):
    """
    Docs:
    https://developer.ebay.com/api-docs/sell/inventory/resources/inventory_item_group/methods/getInventoryItemGroup
    """

    method_type = "GET"
    required_path_params = ["inventoryItemGroupKey"]


class PublishOfferByInventoryItemGroup(OfferAPI):
    """
    Docs:
    https://developer.ebay.com/api-docs/sell/inventory/resources/offer/methods/publishOfferByInventoryItemGroup
    """

    method_type = "POST"
    url_postfix = "publish_by_inventory_item_group"


class WithdrawOfferByInventoryItemGroup(OfferAPI):
    """
    Docs:
    https://developer.ebay.com/api-docs/sell/inventory/resources/offer/methods/withdrawOfferByInventoryItemGroup
    """

    method_type = "POST"
    url_postfix = "withdraw_by_inventory_item_group"
