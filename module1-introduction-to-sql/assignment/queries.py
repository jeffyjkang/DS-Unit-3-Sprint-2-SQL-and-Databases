
total_characters = 'SELECT COUNT(*) FROM charactercreator_character'

total_subclass = '''
SELECT
*
FROM (
SELECT COUNT(*) AS cleric_count
FROM charactercreator_cleric
)
CROSS JOIN (
SELECT COUNT(*) AS fighter_count
FROM charactercreator_fighter
)
CROSS JOIN (
SELECT COUNT(*) AS mage_count
FROM charactercreator_mage
)
CROSS JOIN (
SELECT COUNT(*) AS necromancer_count
FROM charactercreator_necromancer
)
CROSS JOIN (
SELECT COUNT(*) AS thief_count
FROM charactercreator_thief
)
'''

total_items = 'SELECT COUNT(*) FROM armory_item'

total_weapons = 'SELECT COUNT(*) FROM armory_weapon'

total_non_weapons = '''
SELECT
total_items - total_weapons as total_non_weapons
FROM (
SELECT COUNT(*) AS total_items
FROM armory_item
)
CROSS JOIN (
SELECT COUNT(*) AS total_weapons
FROM armory_weapon
)
'''

character_items = '''
SELECT
character_id, COUNT(character_id) AS item_count
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20
'''

character_weapons = '''
SELECT
character_id, count(character_id) AS weapon_count
FROM charactercreator_character_inventory i
INNER JOIN armory_weapon w
WHERE w.item_ptr_id = i.item_id
GROUP BY character_id
LIMIT 20
'''

avg_character_items = '''
SELECT
AVG(item_count) AS avg_item_count
FROM (
SELECT
character_id, COUNT(character_id) AS item_count
FROM charactercreator_character_inventory
GROUP BY character_id
)
'''

avg_character_weapons = '''
SELECT
AVG(weapon_count) AS avg_weapon_count
FROM (
SELECT
character_id, count(character_id) AS weapon_count
FROM charactercreator_character_inventory i
INNER JOIN armory_weapon w
WHERE w.item_ptr_id = i.item_id
GROUP BY character_id
)
'''
