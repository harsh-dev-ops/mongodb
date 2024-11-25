# MongoDB Examples: PyMongo, Beanie, Motor, and FastAPI  

This repository demonstrates how to work with **MongoDB** in Python using four powerful tools: **PyMongo**, **Beanie**, **Motor**, and **FastAPI**. Each folder contains examples of CRUD operations, schema modeling, and advanced features.

---

## Features  
- **PyMongo**: Direct interaction with MongoDB for CRUD and aggregation operations.  
- **Beanie**: An ODM leveraging Pydantic for schema modeling and asynchronous workflows.  
- **Motor**: An asynchronous MongoDB driver for high-performance applications.  
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python, based on standard Python type hints.
---

## Prerequisites  
- Python 3.10 or higher  
- MongoDB installed locally or available via a cloud service like [MongoDB Atlas](https://www.mongodb.com/atlas).
- Docker (Optional) 

---

## Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/harsh-dev-ops/mongodb.git  
   cd mongodb  
   ```

2. Set up a virtual environment: 
    ### Linux/macOS
   ```bash
   python -m venv venv  
   source venv/bin/activate  
   ```
    ### Windows
   ``` bash
   python -m venv venv
   venv\Scripts\activate  
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```

---

## Usage  

### 1. **PyMongo**  
Navigate to the `pymongo/` folder to find examples of:  
- Connecting to a MongoDB database  
- Performing CRUD operations  
<!-- - Using aggregation pipelines   -->

Run an example:  
```bash
cd pymongo
docker compose up
uvicorn app.main:app --reload
```

---

### 2. **Beanie**  
Navigate to the `beanie/` folder to explore:  
- Defining models with Pydantic  
- Asynchronous CRUD operations  
- Advanced features like indexing and migrations  

Run an example:  
```bash
cd beanie
docker compose up
uvicorn app.main:app --reload
```

---

### 3. **Motor**  
Navigate to the `motor/` folder to see:  
- Establishing an asynchronous MongoDB connection  
- Using async/await for CRUD and aggregation  
- Integrating with FastAPI (optional)  

Run:  
```bash
cd motor
docker compose up
uvicorn app.main:app --reload
```

Once the server is running, visit:  
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

<!-- 
## Folder Structure  

```plaintext
mongodb-examples/  
├── pymongo/  
│   ├── basic_crud.py  
│   ├── aggregation_example.py  
├── beanie/  
│   ├── basic_crud.py  
│   ├── models.py  
├── motor/  
│   ├── basic_crud.py  
│   ├── async_aggregation.py  
├── requirements.txt  
└── README.md  
``` -->

---

## Dependencies  
The `requirements.txt` file includes:  
- PyMongo  
- Beanie  
- Motor  
- FastAPI  
- Uvicorn (for running the FastAPI app)  
- Pydantic   

Install all dependencies:  
```bash
pip install -r requirements.txt  
```

---

## Contributing  
Contributions are welcome! Please open an issue or submit a pull request if you find any bugs or have feature suggestions.  

---

## License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---

## Contact  
For questions or feedback, contact **[Harsh Singh](mailto:harshkushwah2011@gmail.com)**.  
```

Let me know if you'd like to make further tweaks!
