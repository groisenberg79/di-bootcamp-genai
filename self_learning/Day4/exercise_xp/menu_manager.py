import db
from menu_item import MenuItem

class MenuManager:
    
    @classmethod
    def get_by_name(cls, name: str) -> MenuItem | None:
        sql = """
        SELECT item_name, item_price
        FROM menu_items
        WHERE item_name = %s;
        """
        item = db.run_select_one(sql, (name,))
        if item is not None:
            return MenuItem(item[0], item[1])
        return None

    @classmethod
    def all_items(cls) -> list[MenuItem]:
        sql = """
        SELECT item_name, item_price
        FROM menu_items
        ORDER BY item_name;;
        """
        items = db.run_select_all(sql)
        return [MenuItem(item[0], item[1]) for item in items]