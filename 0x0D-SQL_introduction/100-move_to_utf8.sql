-- Alter the charset
-- Step 1: Change the character set of the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 2: Select the database
USE hbtn_0c_0;

-- Step 3: Change the character set of each table and its columns
-- Note: This part requires altering each table individually.
-- Below is an example for the `first_table`. Repeat as necessary for other tables.

-- Change the default character set of the table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the character set of specific columns
ALTER TABLE first_table MODIFY name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
