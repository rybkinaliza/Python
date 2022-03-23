#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
from datetime import date


# In[3]:


DB_NAME = "biblio"


# In[4]:


connection = sqlite3.connect(DB_NAME)


# In[5]:


cursor = connection.cursor()


# In[6]:


connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

cursor.execute(
    ''' DROP TABLE IF EXISTS Book '''
)

cursor.execute(
    '''
    CREATE TABLE Book(
        id INT PRIMARY KEY NOT NULL,
        title TEXT,
        author TEXT,
        publish_year INT
    )
    '''
)

cursor.execute(
    '''
    INSERT INTO Book VALUES
    (1, 'Harry Potter and the Philosopher''s Stone', 'J. K. Rowling', 1997),
    (2, 'Методы решения задач в общем курсе физики, Механика', 'Корявов В.П.', 2007),
    (3, 'Batman: Gotham by Gaslight', 'Brian Augustyn, Mike Mignola', 1989),
    (4, 'Мёртвые души', 'Н. В. Гоголь', 1842),
    (5, 'The Running Man', 'Richard Bachman', 1982)
    '''
)

connection.commit()


# In[7]:


cursor.execute(
    ''' DROP TABLE IF EXISTS Reader '''
)

cursor.execute(
    '''
    CREATE TABLE Reader(
        id INT PRIMARY KEY NOT NULL,
        name TEXT
    )
    '''
)

cursor.execute(
    '''
    INSERT INTO Reader VALUES
    (1, 'V.V. Petrovich'),
    (2, 'Alexanderr'),
    (3, 'Arkadiy Svidrigaylov'),
    (4, 'Vitalya'),
    (5, 'Noname')
    '''
)


# In[8]:


cursor.execute(
    ''' DROP TABLE IF EXISTS Record '''
)

cursor.execute(
    '''
    CREATE TABLE Record(
        id INT PRIMARY KEY NOT NULL,
        reader_id INT REFERENCES Readers(id) NOT NULL,
        book_id INT REFERENCES Books(id) NOT NULL,
        taking_date TEXT,
        returning_date TEXT
    )
    '''
)

cursor.execute(
    '''
    INSERT INTO Record VALUES
    (1, 3, 4, '1842-02-14', '1842-07-01'),
    (2, 4, 4, '1996-10-26', NULL),
    (3, 1, 2, '2006-06-13', '2006-06-14'),
    (4, 1, 1, '2006-06-14', '2006-06-15'),
    (5, 1, 3, '2006-06-15', '2006-07-20'),
    (6, 2, 5, '1985-10-11', '1987-12-25'),
    (7, 5, 3, '2001-03-15', NULL),
    (8, 5, 3, '2002-09-19', '2002-09-25')
    '''
)


# In[10]:


def select_books():
    a = []
    for row in cursor.execute("SELECT * FROM Book"):
        a.append(row)
    return a


# In[11]:


select_books()


# In[12]:


def select_readers():
    a = []
    for row in cursor.execute("SELECT * FROM Reader"):
        a.append(row)
    return a


# In[13]:


select_readers()


# In[14]:


def insert_book(id, name, author, year, conn = connection): 
    cursor.execute(
    "INSERT INTO Book VALUES (?, ?, ?, ?)", (id, name, author, year)
    )
    conn.commit()


# In[15]:


insert_book(7, 'mem', 'kek', 2001)


# In[16]:


select_books()


# In[17]:


def insert_reader(id, name, conn = connection): 
    cursor.execute(
    "INSERT INTO Reader VALUES (?, ?)", (id, name)
    )
    conn.commit()


# In[18]:


insert_reader(6, 'Liza')


# In[19]:


select_readers()


# In[20]:


def select_records():
    a = []
    for row in cursor.execute("SELECT * FROM Record"):
        a.append(row)
    return a


# In[21]:


def issue_book(id, reader_id, book_id, returning_date = None, conn=connection):
    cursor.execute(
    "INSERT INTO Record VALUES (?,?,?,?,?)", (id, reader_id, book_id, str(date.today()), returning_date)
    )
    conn.commit()


# In[22]:


select_records()


# In[23]:


issue_book(9, 2, 3)
select_records()


# In[24]:


def take_book(id, conn=connection):
    cursor.execute("UPDATE Record SET returning_date = (?) where id = (?)", (str(date.today()), id))
    conn.commit()


# In[25]:


take_book(9)
select_records()


# In[ ]:




