select_all_female_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE sex = 'F';
"""

select_all_alive_brown_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE color = 'Brown' AND alive = 1;
"""

select_all_bears_return_name_and_age_ordered_by_age_descending = """
    SELECT name, age
    FROM bears
    ORDER BY age DESC;
"""

select_all_bears_return_name_and_age_with_limit = """
    SELECT name, age
    FROM bears
    LIMIT 5;
"""
