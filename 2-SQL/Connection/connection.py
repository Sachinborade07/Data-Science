#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:32:38 2024

@author: Sachin Borade
"""

# for connection with python to sql we use psycopg2 
import psycopg2 as pg2


# Creating the connection with PostgreSQL
# password is what you settted

conn = pg2.connect(database='dvdrental',user='postgres',password='root', host='localhost', port='5432')

# Establish connection and start cursor to be ready 
cur = conn.cursor()

# lets execute the query 
cur.execute("SELECT * FROM payment")

# Return a tuple of the first row as Python object
cur.fetchone()

# Return N number of rows 
cur.fetchmany(10)

# Return all rows at once
cur.fetchall()


# to save and index result 
data = cur.fetchmany(10)

conn.close()