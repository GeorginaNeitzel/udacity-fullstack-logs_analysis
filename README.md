# Logs Analysis
 This is the first project of the Udacity Full Stack Nanodegree. In this project, a large database with over a million logs is analyzed.

## Installation

#### Requirements
* Python 2.7
* Vagrant
* VirtualBox

#### Setup
* Download the VM
* Download the database, unzip it and move it to your vagrant directory

#### Run this project
* run vagrant in vm via **vagrant up** 
* login to vm via **vagrant ssh** and change into vagrant dir
* place the python script in your vagrant directory and run it via `./script.py` 

## Database

The database contains the following tables, variables and relations:

### public.articles

The articles table includes the articles:


 Column |           Type           |         Modifiers                       
--------|--------------------------|---------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     | 
 body   | text                     | 
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)

Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
    
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)


### public.authors

The authors table includes information about the authors of articles.

 Column |  Type   |                      Modifiers                       
--------|---------|------------------------------------------------------
 name   | text    | not null
 bio    | text    | 
 id     | integer | not null default nextval('authors_id_seq'::regclass)

Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
    
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)


### public.log

The log table includes one entry for each time a user has accessed the site.

 Column |           Type           |                    Modifiers                     
--------|--------------------------|--------------------------------------------------
 path   | text                     | 
 ip     | inet                     | 
 method | text                     | 
 status | text                     | 
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('log_id_seq'::regclass)

Indexes:
    "log_pkey" PRIMARY KEY, btree (id)
