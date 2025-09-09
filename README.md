# Finance Advisor - Stock Close Predictor 
 
?? A FastAPI-based ML project that predicts stock closing prices using Gradient Boosting. 
 
## Endpoints 
- /  Health check 
- /docs  Swagger API docs 
- /predict  Make predictions (POST) 
 
## Example Request 
```json 
{ 
  "open": 123.45, 
  "high": 130.00, 
  "low": 120.50, 
  "volume": 500000 
} 
``` 
