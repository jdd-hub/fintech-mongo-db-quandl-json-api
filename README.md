# fintech-mongo-db-quandl-josn-api

This repository contains my latest work ingesting stock market data using the Quandl API with the JSON documents stored in a MongoDB database for further processing.

Get millions of financial and economic datasets from hundreds of publishers via a single free API. The source for financial, economic, and alternative datasets, serving investment professionals.

To visual data, you need high quality, credible and accurate data sources. Quandl provides and an array of data sets for personal (free) and professional use.

As part of my Data Engineering professional development, I am developing an array of data pipelines intended to extract, transform and load data from various sources. Such as this Quandl API, CSV, JSON and database such as Google BigQuery, Microsft SQL Server and PostgreSQL, to name a few.

Some pipelines are developed just for my Data Engineering professional development. I practice working with a variety of data sources solving specific challenges that come as part of handling and building data pipelines from the ground up.

At its present state has been developed into a fully-fledged distributable Python package using Object-Oriented Programming principles. The data source has been switched from the standard API to the JSON API with the JSON documents stored in a MongoDB JSON database for further processing with output intended for a dashboard which I am developing at a later stage.

The package consists of a MongoDB class containing all of the functionality required for interaction with the database. The Markets class consists of a series of CRUD functions necessary for interaction with the individual markets and stock data collections. The markets class inherits the connection for interaction with the database. The insert_markets and fetch markets are simply processes which do as they are named, one inserts the individual stock market reference details and codes required by the API to be able to fetch and store the latest stock performance data. 
