Declarative Data Science
==========

As ML is practiced today, Data Scientist or an ML Scientist would write the models in a particular language (eg Python), and a Production Engineer would rewrite them in a different language or reimplement them in a different tech stack -- scalability being the primary concern. This is called as the two language problem. One way to deal with the two language problem is to unify the tech stack. Languages like Julia claim that same piece of code can scale from a laptop to a cluster. Frameworks like Apache Spark also support multiple languages, and scale from a single CPU system to a cluster. At MLSquare, we are transpiling an ML model developed in Python to a Deep Learning counterpart, saved in ONNX format. ONNX is one of the standard formats available for representing and storing Deep Learning models.  So, ONNX is like jar file in the Java world, and tensfor flow is the JVM equivalent.

But regardless of how such paradigms address the “two language problem”, they still expect someone to write code explicitly. And it is not just about models and their scalability. An important aspect of ML model development is getting the right data, and model management (managing model evolution). Many practitioners estimate that more than 80% of developer time goes in the ETL (Extract, Transform, Load) jobs. And this pieces are always coded by the developers. The problem is, developers should only be concerned with “what” they need and not “how” they should get the data. This problem is largely addressed by the databases world with standards like SQL. Now, SQL is the defacto DSL for ETL. Many databases, including NoSQL databases support SQL for querying and retrieving the data.That means that Data Scientist can leverage SQL for asking what they need and offload the “getting” part to the database’s compute engines (In case, a database can not speak SQL, Spark can be used as the intermediate OLAP engine).

Question is: can we not declaratively specify the entire pipeline?


Approach:

At its core, an ML Pipeline is a DAG (Directed Acyclic Graph), where edges are data flows, and nodes are computational units. By borrowing ideas from dot, cypher and SQL, we can create a DSL to 

Read, Create, update, Delete -- full graph or subgraphs
Clone/Import a graph and update in full or parts
Express the ETL declaratively
Express Models declaratively

Few solutions are already implemented. But they need to be refined and tidied. See draft solutions here. A DAG for ML Pipelines is also available here and its parser here

Prerequisites
Language: Python
Parsing module: pyparsing or something similar
Idea about YAML, JSON
Basic understanding of the Backus-Naur form
Basic understanding of dot, cypher, sql
Basic understanding of deploying solutions on the cloud using GCP (or similar)


.. toctree::
	Chapter 2.1 <s01>
	Chapter 2.2 <s02>

