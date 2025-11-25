# NASA Asteroids Data Engineering Project

This project explores NASA's Near Earth Object (NEO) API to build a **data engineering pipeline** around asteroid information.  
The goal is to practice and showcase skills in:
- Python development
- Data engineering workflows
- Project management with GitHub
- Documentation and communication

At this stage, the project is in its **early discovery phase**. The focus is on understanding the NASA API and designing the architecture for data ingestion, storage, and analysis.

---

## Objectives
- Learn how to interact with NASA's asteroid API
- Design a scalable data pipeline for ingestion and transformation
- Store and organize data for analysis
- Explore potential insights (e.g., asteroid frequency, size distribution, close approaches)

---

## Planned Tech Stack
- **Python** for data ingestion and processing
- **Pandas / PySpark** for transformations
- **SQL / Data Warehouse** (to be defined)
- **Visualization tools** (e.g., Jupyter, dashboards)

---

## Project Structure (initial draft)
<pre>
nasa-asteroids/
│
├── docs/                     # Deeper documentation
├── logs/                     # Logs from code runs
├── notebooks/                # Jupyter notebooks for exploration & prototyping
├── tests/                    # Unit tests
│   ├── unit/                 # Python code unit tests
│   └── integration/          # integration tests
│       └── postman/          # Postman JSON files for API testing
|
├── src/                      # Source code (Python modules, pipeline scripts)
│   ├── custom_logger/        # Custom module for Python logger
│   └── core/                 # Core script of the project
│       └── main.py           # Main script for running the project
│
├── .gitignore                # Git ignore rules
├── CHANGELOG.md              # Track project changes
├── CONTRIBUTING.md           # Contribution guidelines
├── LICENSE                   # License file
├── NOTICE                    # Legal and attribution notices
├── README.md                 # Main project landing page
└── requirements.txt          # Dependencies

</pre>




---

## Roadmap
- [x] Create repository and project board
- [x] Set up initial documentation structure
- [x] Explore NASA API endpoints
- [ ] Build first ingestion script
- [ ] Add testing and CI/CD
- [ ] Develop transformation pipeline
- [ ] Create visualizations and insights

---

## Contributing
This is a personal learning project. Contribution guidelines are available in [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License
This project is licensed under the Apache 2.0 License – see the [LICENSE](LICENSE) file for details.
