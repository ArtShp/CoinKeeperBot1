from typing import Dict, List

import db


class Categories:
    def __init__(self) -> List[Dict]:
        self._categories = self._load_categories()

    def _load_categories(self) -> List[Dict]:
        categories = db.fetch_all('category', 'codename name is_base_expense aliases'.split())
        self._fill_aliases(categories)
        return categories

    def _fill_aliases(self, categories) -> List[Dict]:
        for index, category in enumerate(categories):
            aliases = category['aliases'].split(',')
            aliases = list(filter(None, map(str.strip, aliases)))
            aliases.append(category['codename'])
            aliases.append(category['name'])
            categories[index]['aliases'] = aliases

    def get_all_categories(self) -> List[Dict]:
        return self._categories

    def get_category(self, cn: str) -> str:
        find = None
        other_category = None
        for category in self._categories:
            if category['codename'] == 'other':
                other_category = category
            for alias in category['aliases']:
                if cn in alias:
                    find = category
        if not find:
            find = other_category
        return find
