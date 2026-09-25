
# Artists Commissions Analytics

An end-to-end Data Engineering and Analytics project designed to explore the business performance of an independent digital artist.

The project transforms historical commission records and other business data into a structured analytical environment, with the goal of understanding revenue, customer behavior, demand, pricing, and operational performance.

Unlike a purely synthetic portfolio exercise, this project originates from a real business and is developed in collaboration with the artist herself.

**Status:** In development

---

## 1. Project Overview

Independent artists often manage their commissions through spreadsheets, online forms, emails, and multiple social platforms.

While these tools work well individually, they make it difficult to obtain a unified view of the business.

This project aims to consolidate these fragmented sources into a reproducible data pipeline and provide actionable insights through analytical models and Power BI dashboards.

The initial focus is on historical commission data from 2025 onward, with further integrations planned.

### Business objectives

- Understand revenue trends and commission demand.
- Identify the most profitable commission categories.
- Analyze customer retention and repeat purchases.
- Evaluate pricing and payment-related fees.
- Investigate commission lead times and workload.
- Understand which acquisition channels generate valuable customers.
- Compare pricing and commission models with other independent artists.

The ultimate goal is to support better-informed decisions about pricing, scheduling, customer relationships, and business growth.

---

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data extraction and loading |
| PostgreSQL | Relational data storage |
| Docker / Docker Compose | Containerized infrastructure |
| dbt | Data transformation and analytical modeling |
| SQL | Data cleaning, transformation, and analysis |
| Power BI | Business intelligence and visualization |
| Git / GitHub | Version control and documentation |

The project follows a modular ELT-oriented architecture, separating raw data ingestion from analytical transformations.

---

## 3. Data Sources

### Historical commission records

The primary source is a private Excel workbook containing annual worksheets from 2025 to 2029.

It includes information such as:

- Customer identifiers and contact information
- Commission descriptions
- Order dates and deadlines
- Commission status and priority
- Pricing and PayPal fees
- Net revenue
- Sales channels
- Operational notes

Some worksheets contain future planning templates rather than completed transactions.

The source also contains month separators, empty commission slots, and other non-transactional rows. These must be distinguished from actual commissions during transformation.

### Commission request form

The artist uses an online form to collect commission requests.

Available fields include:

- Customer type
- Acquisition channel
- Requested commission category
- Preferred booking date
- Deadline
- Additional characters and background requirements
- Commercial licensing
- Exclusivity and sharing permissions
- Additional project details

Historical submissions are being evaluated as a potential additional data source.

If available, these records could allow analysis of the conversion process from initial request to accepted commission.

### Website and pricing information

The artist's website provides information about available services, commission categories, pricing, additional options, and commercial licensing.

Website: https://www.thesleepingfoxy.it/

### Potential future sources

- Instagram and other social platform metrics
- Patreon data
- Historical commission requests
- Publicly available competitor pricing information

These integrations are planned and are not yet part of the implemented pipeline.

---

## 4. Architecture

The project separates source ingestion, data transformation, and business intelligence into distinct layers.

    Private Excel Workbook
              |
              v
       Python Extractor
              |
              v
       PostgreSQL RAW
              |
              v
         dbt Staging
              |
              v
       Analytical Models
              |
              v
          Data Marts
              |
              v
            Power BI

Future integrations will extend the ingestion layer to additional sources.

### RAW layer

Preserves the original information extracted from the Excel workbook.

Source metadata is retained to support traceability and debugging.

### Staging layer

Standardizes source fields, handles inconsistent formatting, identifies different row types, and prepares the data for downstream modeling.

### Core analytical layer

Planned relational models will represent business entities such as customers, commission requests, commissions, and payments.

### Data marts

Business-oriented models will support KPIs and analytical dashboards.

---

## 5. Current Implementation

The first phase of the project focuses on building a reliable Excel-to-PostgreSQL ingestion pipeline.

### Completed

- Repository and project structure initialized.
- PostgreSQL environment configured using Docker.
- RAW database schema created.
- Python Excel extractor implemented.
- Source columns mapped across different annual worksheets.
- Empty Excel values converted into database NULL values.
- Transactional full-refresh loading implemented.
- Source worksheet and row metadata preserved.
- Initial dbt project, source definition, and staging model configured.

The pipeline currently loads **420 source rows** across the five annual worksheets.

These are raw worksheet records, not 420 actual commission transactions.

Each raw record is traceable through its source worksheet and original row number.

### Current development focus

The next transformation step is to classify source rows into meaningful categories:

- Commission candidates
- Month headers
- Empty or planning slots
- Known source anomalies

Source anomalies should be handled in the staging layer without modifying the original RAW dataset.

---

## 6. Analytical Questions

The project is guided by business questions rather than by dashboard creation alone.

### Revenue and performance

- How does commission revenue evolve over time?
- Which commission categories generate the most revenue?
- What is the average commission value?
- How much revenue is lost to payment processing fees?
- Are there identifiable seasonal trends?

### Customer behavior

- How many unique customers does the artist serve?
- What percentage of customers return?
- How much revenue comes from repeat customers?
- How does customer spending evolve over time?

### Commission operations

- How many commissions are accepted and completed?
- How long does it take to complete a commission?
- Which categories require longer delivery times?
- How frequently are deadlines missed or rescheduled?
- How does workload change throughout the year?

### Acquisition and conversion

Subject to the availability of historical request data:

- Where do potential customers discover the artist?
- How many requests become accepted commissions?
- Which channels generate the most revenue?
- Which acquisition channels bring repeat customers?

### Pricing and competitive analysis

A future research component will compare publicly available information from other independent artists.

Questions include:

- How do commission prices differ across comparable artists?
- How are additional characters, backgrounds, and commercial licenses priced?
- How do artists structure commission slots and availability?
- Are there observable relationships between audience size, pricing, and service offerings?

---

## 7. Development Roadmap

| Phase | Description | Status |
|---|---|---|
| 1 | Repository and environment setup | Completed |
| 2 | Docker and PostgreSQL setup | Completed |
| 3 | RAW database schema | Completed |
| 4 | Excel extraction and loading | Completed |
| 5 | dbt initialization | Completed |
| 6 | Staging transformations and classification | In progress |
| 7 | Core relational models | Planned |
| 8 | Customer and request matching | Planned |
| 9 | Analytical data marts | Planned |
| 10 | Power BI dashboards | Planned |
| 11 | Data quality and automated tests | Planned |
| 12 | Synthetic public dataset | Planned |
| 13 | Final documentation and portfolio release | Planned |

The roadmap may evolve as additional business requirements and source data are validated with the artist.

---

## 8. Data Privacy

**The original dataset contains private business and customer information and is not included in this repository.**

Real customer names, email addresses, social media handles, private communications, and financial records must not be published.

The repository is intended to contain:

- Source code
- SQL and dbt models
- Infrastructure configuration
- Documentation
- Synthetic or properly anonymized example data

Original source files and credentials are excluded from version control.

A synthetic dataset is planned to make the project publicly reproducible without exposing the artist's private information.

Until that dataset is available, the complete pipeline requires access to the private source workbook.

---

## 9. Development Approach

This project is developed incrementally, with direct input from the business stakeholder.

Data quality issues, ambiguous fields, and business assumptions are validated with the artist whenever possible rather than resolved through unsupported assumptions.

The development process prioritizes:

1. Understanding the business problem.
2. Inspecting and validating source data.
3. Building reproducible ingestion pipelines.
4. Modeling meaningful business entities.
5. Implementing analytical transformations.
6. Delivering actionable insights.

The emphasis is on both engineering reliability and practical business value.

---

## Author

**Alex Cruceru**

Data Engineering · Python · SQL · PostgreSQL · Docker · dbt · Power BI

[GitHub](https://github.com/Alexcruci) · [LinkedIn](https://www.linkedin.com/in/alexcruci/)
