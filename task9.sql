  CREATe table items_count_by_size AS
  SELECT size, COUNT(DISTINCT size) as item_count
  FROM duplicate_items, item_attributes
  GROUP BY size