# End-to-End Book Data Pipeline & Analytics System

## 1. Project Overview

This project is an end-to-end book data pipeline developed using Python. It collects book information from the Books to Scrape website, stores the data in a SQLite database, provides REST APIs using FastAPI, and performs data processing and visualization using Pandas and Matplotlib.

The project demonstrates the complete flow of data from web scraping to database storage, API access, data processing, CSV export, and visualization.

## 2. End-to-End Pipeline

```text
Books to Scrape
       ↓
Web Scraping
(scraper.py)
       ↓
SQLite Database
(books.db)
       ↓
FastAPI REST API
(main.py)
       ↓
Python API Client
(client.py)
       ↓
Pandas DataFrame
       ↓
CSV Export + Visualization
       ↓
Price vs Rating Graph
