Number Classification API
API Overview

The Number Classification API takes a number and returns interesting mathematical properties about it, including whether it’s prime, whether it’s an Armstrong number, and its parity (odd or even). It also fetches a fun fact about the number from the Numbers API.

### Available Endpoints

**GET** `/api/classify-number?number=<number>`

- **Description**: Classifies the number and returns properties, digit sum, and a fun fact.
- **Query Parameter**: `number` (required) - The number to classify.

How to Install and Run the API
Prerequisites

- Python 3.x
- Flask
- Requests library

Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/number-classification-api.git
   cd number-classification-api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API:

   ```bash
   python app.py
   ```

   The app will run on `http://0.0.0.0:5000`.

Example Requests and Responses
Example 1: Valid Request

**Request**:
```bash
curl http://<your-deployment-link>/api/classify-number?number=371
```

**Response**:
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

Example 2: Invalid Request (Non-numeric Input)

**Request**:
```bash
curl http://<your-deployment-link>/api/classify-number?number=abc
```

**Response**:
```json
{
  "number": "abc",
  "error": true
}
```

Deployment Link

You can access the live API at:

[http://<your-deployment-link>](http://<your-deployment-link>)

Author Information

- **Author**: [Your Name](https://github.com/yourusername)
- **Email**: [your-email@example.com](mailto:your-email@example.com)


---

This project was developed as part of the DevOps Stage 1 task for the classification of numbers and their properties.
