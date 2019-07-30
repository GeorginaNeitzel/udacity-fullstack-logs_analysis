# Logs Analysis
 This is the first project of the Udacity Full Stack Nanodegree. In this project, a large database with over a million logs is analyzed.

## Installation

#### Requirements
Prior to the project, the following software has to be installed
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Git](https://git-scm.com/downloads)

#### Setup
* Clone the nanodegree [repo](https://github.com/udacity/fullstack-nanodegree-vm)

#### Run this project
* Navigate to the vagrant folder via `cd fullstack/vagrant` and launch vagrant using **vagrant up** 
* Login to VM via **vagrant ssh** and change into vagrant diriectory `cd /vagrant`
* Place `script.py` in your vagrant directory and run it via `./script.py` 

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
