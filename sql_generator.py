def generate_sql(prompt):

    if not prompt:
        return "-- Enter a query description."

    text = prompt.lower()

    # ==========================================
    # Average Salary
    # ==========================================

    if "average salary" in text or "avg salary" in text:

        return """
SELECT AVG(Salary) AS Average_Salary
FROM employees;
"""

    # ==========================================
    # Salary by Department
    # ==========================================

    elif "department" in text and "salary" in text:

        return """
SELECT Department,
AVG(Salary) AS Average_Salary
FROM employees
GROUP BY Department;
"""

    # ==========================================
    # Top Salary
    # ==========================================

    elif "top" in text and "salary" in text:

        return """
SELECT *
FROM employees
ORDER BY Salary DESC
LIMIT 5;
"""

    # ==========================================
    # Employee Count
    # ==========================================

    elif "count" in text or "employees" in text:

        return """
SELECT COUNT(*) AS Total_Employees
FROM employees;
"""

    # ==========================================
    # Missing Values
    # ==========================================

    elif "missing" in text or "null" in text:

        return """
-- SQL databases don't have a universal query for missing values.
-- Replace Column_Name with your column.

SELECT *
FROM employees
WHERE Column_Name IS NULL;
"""

    # ==========================================
    # Duplicate Records
    # ==========================================

    elif "duplicate" in text:

        return """
SELECT EmployeeID,
COUNT(*)
FROM employees
GROUP BY EmployeeID
HAVING COUNT(*) > 1;
"""

    # ==========================================
    # Highest Experience
    # ==========================================

    elif "experience" in text:

        return """
SELECT *
FROM employees
ORDER BY Experience DESC
LIMIT 1;
"""

    # ==========================================
    # Average Age
    # ==========================================

    elif "age" in text:

        return """
SELECT AVG(Age)
FROM employees;
"""

    # ==========================================
    # Default
    # ==========================================

    return """
-- Query not recognized.

Example Prompts:

Average Salary

Top Salary

Employee Count

Duplicate Records

Salary by Department

Average Age

Highest Experience
"""